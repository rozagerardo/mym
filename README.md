### Run odoo:
```
python odoo.py -w nzpass -r mymadmin --addons-path=addons --db-filter=mym-db$
```

### Cosas a configurar:
1. BD inicial
2. Modulos a usar: Facturacion (impuestos) / Ventas / Almacenes / MRP
3. Opcions de Settings:
  1. Permitir añadir gastos de envío (?)
  2. Usar tarifas para adaptar los precios a cada cliente (?)
  3. Lanzar órdenes de entrega automáticas desde los pedidos de venta (?)
  4. Gestionar pagos de cliente (?)
3. Listados de precios (regular, Meli(?), etsy(?))
4. Adelanto o Sena (abajo)
5. Inventario Yeso
6. Transportistas (?)

### Add 'Adelanto o Sena:
1. Crear usuario `dev` con permisos tecnicos
2. Loguearse con usuario `dev`
3. Seguir estos pasos:
https://www.odoo.com/es_ES/forum/ayuda-1/solved-how-to-add-field-into-quotation-sale-order-pdf-98720
  1. Agregar Campo a modelo de sale.order
  2. Agregar campo a View (QView -> saleorder.document) del reporte de sale.report_order
  3. Agregar field a Interfaz de usuario ': Vista de formulario de sale.order.form

### Dump database:
* Dump all (with metadata):
```
docker-compose exec -T mym-db pg_dumpall -c -U mymadmin | gzip > dump_`date +%d-%m-%Y"_"%H_%M_%S`.gz
```

[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/8.0.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/8.0-docs-8f8f8f.svg?style=flat)](http://www.odoo.com/documentation/8.0) 
[![Help](http://img.shields.io/badge/8.0-help-8f8f8f.svg?style=flat)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/8.0-nightly-8f8f8f.svg?style=flat)](http://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>, <a href="https://www.odoo.com/page/website-builder">Website Builder</a>, <a href="https://www.odoo.com/page/e-commerce">eCommerce</a>, <a href="https://www.odoo.com/page/project-management">Project Management</a>, <a href="https://www.odoo.com/page/accounting">Billing &amp; Accounting</a>, <a href="https://www.odoo.com/page/point-of-sale">Point of Sale</a>, <a href="https://www.odoo.com/page/employees">Human Resources</a>, Marketing, Manufacturing, Purchase Management, ...  

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.


Getting started with Odoo
-------------------------
For a standard installation please follow the <a href="https://www.odoo.com/documentation/8.0/setup/install.html">Setup instructions</a>
from the documentation.

If you are a developer you may type the following command at your terminal:

    wget -O- https://raw.githubusercontent.com/odoo/odoo/8.0/odoo.py | python

Then follow <a href="https://www.odoo.com/documentation/8.0/tutorials.html">the developer tutorials</a>


For Odoo employees
------------------

To add the odoo-dev remote use this command:

    $ ./odoo.py setup_git_dev

To fetch odoo merge pull requests refs use this command:

    $ ./odoo.py setup_git_review

