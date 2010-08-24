# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Page.images'
        db.add_column('info_page', 'images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Img'], null=True, blank=True), keep_default=False)

        # Adding field 'Page.scripts'
        db.add_column('info_page', 'scripts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Js'], null=True, blank=True), keep_default=False)

        # Adding field 'Page.stylesheets'
        db.add_column('info_page', 'stylesheets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Css'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field stylesheets on 'Page'
        db.delete_table('info_page_stylesheets')

        # Removing M2M table for field scripts on 'Page'
        db.delete_table('info_page_scripts')

        # Removing M2M table for field images on 'Page'
        db.delete_table('info_page_images')


    def backwards(self, orm):
        
        # Deleting field 'Page.images'
        db.delete_column('info_page', 'images_id')

        # Deleting field 'Page.scripts'
        db.delete_column('info_page', 'scripts_id')

        # Deleting field 'Page.stylesheets'
        db.delete_column('info_page', 'stylesheets_id')

        # Adding M2M table for field stylesheets on 'Page'
        db.create_table('info_page_stylesheets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['info.page'], null=False)),
            ('css', models.ForeignKey(orm['assets.css'], null=False))
        ))
        db.create_unique('info_page_stylesheets', ['page_id', 'css_id'])

        # Adding M2M table for field scripts on 'Page'
        db.create_table('info_page_scripts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['info.page'], null=False)),
            ('js', models.ForeignKey(orm['assets.js'], null=False))
        ))
        db.create_unique('info_page_scripts', ['page_id', 'js_id'])

        # Adding M2M table for field images on 'Page'
        db.create_table('info_page_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['info.page'], null=False)),
            ('img', models.ForeignKey(orm['assets.img'], null=False))
        ))
        db.create_unique('info_page_images', ['page_id', 'img_id'])


    models = {
        'assets.css': {
            'Meta': {'object_name': 'Css'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/css'", 'max_length': '100', 'recursive': 'True'})
        },
        'assets.img': {
            'Meta': {'object_name': 'Img'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['assets.ImgSrc']", 'symmetrical': 'False'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'})
        },
        'assets.imgsrc': {
            'Meta': {'object_name': 'ImgSrc'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'src': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'assets.js': {
            'Meta': {'object_name': 'Js'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/js'", 'max_length': '100', 'recursive': 'True'})
        },
        'info.page': {
            'Meta': {'object_name': 'Page'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Img']", 'null': 'True', 'blank': 'True'}),
            'scripts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Js']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'stylesheets': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Css']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['info']
