# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manifest'
        db.create_table(u'orders_manifest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300, db_index=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(default='root', max_length=300)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Company'])),
            ('csv_upload', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('lock_task', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('rollover_from_previous', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'orders', ['Manifest'])

        # Adding M2M table for field allowed_suppliers on 'Manifest'
        m2m_table_name = db.shorten_name(u'orders_manifest_allowed_suppliers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manifest', models.ForeignKey(orm[u'orders.manifest'], null=False)),
            ('supplier', models.ForeignKey(orm[u'suppliers.supplier'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manifest_id', 'supplier_id'])

        # Adding model 'Invoice'
        db.create_table(u'orders_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('manifest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Manifest'])),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=300, db_index=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('internal_reference', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('reissue', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reissues', null=True, to=orm['orders.Invoice'])),
            ('date_imported', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'orders', ['Invoice'])

        # Adding model 'InvoiceLine'
        db.create_table(u'orders_invoiceline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lines', to=orm['orders.Invoice'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=300, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('declared_value', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('actual_value', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('delivery_revenue', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['suppliers.Supplier'], null=True, blank=True)),
            ('ordered_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('progress_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('item_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2)),
            ('delivery_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2)),
            ('remote_delivery_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2)),
            ('prepaid_inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Inventory'], null=True, blank=True)),
            ('delayed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'orders', ['InvoiceLine'])

        # Adding model 'Quote'
        db.create_table(u'orders_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quotes', to=orm['products.Product'])),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quotes', to=orm['suppliers.Supplier'])),
            ('manifest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quotes', to=orm['orders.Manifest'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'orders', ['Quote'])

        # Adding unique constraint on 'Quote', fields ['product', 'supplier', 'manifest']
        db.create_unique(u'orders_quote', ['product_id', 'supplier_id', 'manifest_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Quote', fields ['product', 'supplier', 'manifest']
        db.delete_unique(u'orders_quote', ['product_id', 'supplier_id', 'manifest_id'])

        # Deleting model 'Manifest'
        db.delete_table(u'orders_manifest')

        # Removing M2M table for field allowed_suppliers on 'Manifest'
        db.delete_table(db.shorten_name(u'orders_manifest_allowed_suppliers'))

        # Deleting model 'Invoice'
        db.delete_table(u'orders_invoice')

        # Deleting model 'InvoiceLine'
        db.delete_table(u'orders_invoiceline')

        # Deleting model 'Quote'
        db.delete_table(u'orders_quote')


    models = {
        u'core.company': {
            'Meta': {'object_name': 'Company'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'company_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'customer_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'customer_email_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'supplier_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'supplier_email_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'transactional_bcc_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        u'orders.invoice': {
            'Meta': {'ordering': "['order_number']", 'object_name': 'Invoice'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'date_imported': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_reference': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Manifest']"}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reissue': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reissues'", 'null': 'True', 'to': u"orm['orders.Invoice']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'orders.invoiceline': {
            'Meta': {'ordering': "('invoice', 'product')", 'object_name': 'InvoiceLine'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'actual_value': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'declared_value': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'delayed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delivery_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'delivery_revenue': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lines'", 'to': u"orm['orders.Invoice']"}),
            'item_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ordered_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'prepaid_inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Inventory']", 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'progress_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'remote_delivery_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['suppliers.Supplier']", 'null': 'True', 'blank': 'True'})
        },
        u'orders.manifest': {
            'Meta': {'object_name': 'Manifest'},
            'allowed_suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['suppliers.Supplier']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'csv_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lock_task': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'rollover_from_previous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '300'})
        },
        u'orders.quote': {
            'Meta': {'ordering': "('product', 'supplier')", 'unique_together': "(('product', 'supplier', 'manifest'),)", 'object_name': 'Quote'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quotes'", 'to': u"orm['orders.Manifest']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quotes'", 'to': u"orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quotes'", 'to': u"orm['suppliers.Supplier']"})
        },
        u'products.bundle': {
            'Meta': {'object_name': 'Bundle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bundled_products'", 'symmetrical': 'False', 'to': u"orm['products.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'products.inventory': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Inventory'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Company']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['suppliers.Supplier']"})
        },
        u'products.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'allowed_suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'allowed_products'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['suppliers.Supplier']"}),
            'bundle': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['products.Bundle']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300', 'db_index': 'True'}),
            'packing_comment': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'requires_serial_number': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'null': 'True', 'max_digits': '20', 'decimal_places': '3', 'blank': 'True'})
        },
        u'suppliers.supplier': {
            'Meta': {'ordering': "['name']", 'object_name': 'Supplier'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'colour': ('django.db.models.fields.CharField', [], {'default': "'#000099'", 'max_length': '30'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_disclaimer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '1.0', 'max_digits': '4', 'decimal_places': '3'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']