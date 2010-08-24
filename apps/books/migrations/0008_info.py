# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Book.images'
        db.add_column('books_book', 'images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Img'], null=True, blank=True), keep_default=False)

        # Adding field 'Book.scripts'
        db.add_column('books_book', 'scripts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Js'], null=True, blank=True), keep_default=False)

        # Adding field 'Book.stylesheets'
        db.add_column('books_book', 'stylesheets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Css'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field stylesheets on 'Book'
        db.delete_table('books_book_stylesheets')

        # Removing M2M table for field scripts on 'Book'
        db.delete_table('books_book_scripts')

        # Removing M2M table for field images on 'Book'
        db.delete_table('books_book_images')


    def backwards(self, orm):
        
        # Deleting field 'Book.images'
        db.delete_column('books_book', 'images_id')

        # Deleting field 'Book.scripts'
        db.delete_column('books_book', 'scripts_id')

        # Deleting field 'Book.stylesheets'
        db.delete_column('books_book', 'stylesheets_id')

        # Adding M2M table for field stylesheets on 'Book'
        db.create_table('books_book_stylesheets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('css', models.ForeignKey(orm['assets.css'], null=False))
        ))
        db.create_unique('books_book_stylesheets', ['book_id', 'css_id'])

        # Adding M2M table for field scripts on 'Book'
        db.create_table('books_book_scripts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('js', models.ForeignKey(orm['assets.js'], null=False))
        ))
        db.create_unique('books_book_scripts', ['book_id', 'js_id'])

        # Adding M2M table for field images on 'Book'
        db.create_table('books_book_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('img', models.ForeignKey(orm['assets.img'], null=False))
        ))
        db.create_unique('books_book_images', ['book_id', 'img_id'])


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
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Img']", 'null': 'True', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'purchased': ('django.db.models.fields.DateField', [], {}),
            'scripts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Js']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'stylesheets': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Css']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['books']
