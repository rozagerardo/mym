import logging
import os
import sys
from os.path import join as opj

import openerp
from openerp.osv import osv
from openerp.tools import convert_file

_logger = logging.getLogger(__name__)

class view(osv.osv):
    _inherit = "ir.module.module"

    def import_module(self, cr, uid, module, path, context=None):
        known_mods = self.browse(cr, uid, self.search(cr, uid, []))
        known_mods_names = dict([(m.name, m) for m in known_mods])

        mod = known_mods_names.get(module)
        terp = openerp.modules.load_information_from_description_file(module, mod_path=path)
        values = self.get_values_from_terp(terp)

        unmet_dependencies = set(terp['depends']).difference(known_mods_names.keys())
        if unmet_dependencies:
            raise Exception("Unmet module dependencies: %s" % ', '.join(unmet_dependencies))

        if mod:
            self.write(cr, uid, mod.id, values)
            mode = 'update'
        else:
            assert terp.get('installable', True), "Module not installable"
            self.create(cr, uid, dict(name=module, state='uninstalled', **values))
            mode = 'init'

        for kind in ['data', 'init_xml', 'update_xml']:
            for filename in terp[kind]:
                _logger.info("module %s: loading %s", module, filename)
                noupdate = False
                if filename.endswith('.csv') and kind in ('init', 'init_xml'):
                    noupdate = True
                pathname = opj(path, filename)
                idref = {}
                convert_file(cr, module, filename, idref, mode=mode, noupdate=noupdate, kind=kind, pathname=pathname)

        path_static = opj(path, 'static')
        ir_attach = self.pool['ir.attachment']
        if os.path.isdir(path_static):
            for root, _, files in os.walk(path_static):
                for static_file in files:
                    full_path = opj(root, static_file)
                    with open(full_path, 'r') as fp:
                        data = fp.read().encode('base64')
                    url_path = '/%s%s' % (module, full_path.split(path)[1].replace(os.path.sep, '/'))
                    url_path = url_path.decode(sys.getfilesystemencoding())
                    filename = os.path.split(url_path)[1]
                    values = dict(
                        name=filename,
                        datas_fname=filename,
                        url=url_path,
                        res_model='ir.ui.view',
                        type='binary',
                        datas=data,
                    )
                    att_id = ir_attach.search(cr, uid, [('url', '=', url_path), ('type', '=', 'binary'), ('res_model', '=', 'ir.ui.view')], context=context)
                    if att_id:
                        ir_attach.write(cr, uid, att_id, values, context=context)
                    else:
                        ir_attach.create(cr, uid, values, context=context)

        return True
