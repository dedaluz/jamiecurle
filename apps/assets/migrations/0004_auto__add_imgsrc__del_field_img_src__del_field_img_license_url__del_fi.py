# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ImgSrc'
        db.create_table('assets_imgsrc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('src', self.gf('apps.utils.fields.ImageWithThumbsField')(blank=False)),
        ))
        db.send_create_signal('assets', ['ImgSrc'])

        # Deleting field 'Img.src'
        db.delete_column('assets_img', 'src')

        # Deleting field 'Img.license_url'
        db.delete_column('assets_img', 'license_url')

        # Deleting field 'Img.description'
        db.delete_column('assets_img', 'description')

        # Deleting field 'Img.author'
        db.delete_column('assets_img', 'author')

        # Deleting field 'Img.title'
        db.delete_column('assets_img', 'title')

        # Deleting field 'Img.created'
        db.delete_column('assets_img', 'created')

        # Adding field 'Img.order'
        db.add_column('assets_img', 'order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=10), keep_default=False)

        # Adding M2M table for field image on 'Img'
        db.create_table('assets_img_image', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('img', models.ForeignKey(orm['assets.img'], null=False)),
            ('imgsrc', models.ForeignKey(orm['assets.imgsrc'], null=False))
        ))
        db.create_unique('assets_img_image', ['img_id', 'imgsrc_id'])


    def backwards(self, orm):
        
        # Deleting model 'ImgSrc'
        db.delete_table('assets_imgsrc')

        # Adding field 'Img.src'
        db.add_column('assets_img', 'src', self.gf('apps.utils.fields.ImageWithThumbsField')(default='none.png', blank=False), keep_default=False)

        # Adding field 'Img.license_url'
        db.add_column('assets_img', 'license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Img.description'
        db.add_column('assets_img', 'description', self.gf('django.db.models.fields.TextField')(default='none.png', blank=True), keep_default=False)

        # Adding field 'Img.author'
        db.add_column('assets_img', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Img.title'
        db.add_column('assets_img', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Img.created'
        db.add_column('assets_img', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 8, 23), blank=True), keep_default=False)

        # Deleting field 'Img.order'
        db.delete_column('assets_img', 'order')

        # Removing M2M table for field image on 'Img'
        db.delete_table('assets_img_image')


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
        }
    }

    complete_apps = ['assets']
