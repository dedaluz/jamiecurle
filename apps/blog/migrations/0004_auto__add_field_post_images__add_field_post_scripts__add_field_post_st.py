# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.images'
        db.add_column('blog_post', 'images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Img'], null=True, blank=True), keep_default=False)

        # Adding field 'Post.scripts'
        db.add_column('blog_post', 'scripts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Js'], null=True, blank=True), keep_default=False)

        # Adding field 'Post.stylesheets'
        db.add_column('blog_post', 'stylesheets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Css'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field stylesheets on 'Post'
        db.delete_table('blog_post_stylesheets')

        # Removing M2M table for field scripts on 'Post'
        db.delete_table('blog_post_scripts')

        # Removing M2M table for field images on 'Post'
        db.delete_table('blog_post_images')


    def backwards(self, orm):
        
        # Deleting field 'Post.images'
        db.delete_column('blog_post', 'images_id')

        # Deleting field 'Post.scripts'
        db.delete_column('blog_post', 'scripts_id')

        # Deleting field 'Post.stylesheets'
        db.delete_column('blog_post', 'stylesheets_id')

        # Adding M2M table for field stylesheets on 'Post'
        db.create_table('blog_post_stylesheets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('css', models.ForeignKey(orm['assets.css'], null=False))
        ))
        db.create_unique('blog_post_stylesheets', ['post_id', 'css_id'])

        # Adding M2M table for field scripts on 'Post'
        db.create_table('blog_post_scripts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('js', models.ForeignKey(orm['assets.js'], null=False))
        ))
        db.create_unique('blog_post_scripts', ['post_id', 'js_id'])

        # Adding M2M table for field images on 'Post'
        db.create_table('blog_post_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('img', models.ForeignKey(orm['assets.img'], null=False))
        ))
        db.create_unique('blog_post_images', ['post_id', 'img_id'])


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
        'blog.post': {
            'Meta': {'object_name': 'Post'},
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
            'stylesheets': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assets.Css']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']
