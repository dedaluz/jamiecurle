# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Script'
        db.create_table('blog_script', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.FilePathField')(path='%s/blog/js', max_length=100, recursive=True)),
        ))
        db.send_create_signal('blog', ['Script'])

        # Adding model 'StyleSheet'
        db.create_table('blog_stylesheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.FilePathField')(path='%s/blog/css', max_length=100, recursive=True)),
        ))
        db.send_create_signal('blog', ['StyleSheet'])

        # Changing field 'Photo.author'
        db.alter_column('blog_photo', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Adding M2M table for field stylesheets on 'Post'
        db.create_table('blog_post_stylesheets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('stylesheet', models.ForeignKey(orm['blog.stylesheet'], null=False))
        ))
        db.create_unique('blog_post_stylesheets', ['post_id', 'stylesheet_id'])

        # Adding M2M table for field scripts on 'Post'
        db.create_table('blog_post_scripts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('script', models.ForeignKey(orm['blog.script'], null=False))
        ))
        db.create_unique('blog_post_scripts', ['post_id', 'script_id'])


    def backwards(self, orm):
        
        # Deleting model 'Script'
        db.delete_table('blog_script')

        # Deleting model 'StyleSheet'
        db.delete_table('blog_stylesheet')

        # Changing field 'Photo.author'
        db.alter_column('blog_photo', 'author', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True))

        # Removing M2M table for field stylesheets on 'Post'
        db.delete_table('blog_post_stylesheets')

        # Removing M2M table for field scripts on 'Post'
        db.delete_table('blog_post_scripts')


    models = {
        'blog.photo': {
            'Meta': {'object_name': 'Photo'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Post']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scripts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Script']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'stylesheets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.StyleSheet']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.script': {
            'Meta': {'object_name': 'Script'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'%s/blog/js'", 'max_length': '100', 'recursive': 'True'})
        },
        'blog.stylesheet': {
            'Meta': {'object_name': 'StyleSheet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'%s/blog/css'", 'max_length': '100', 'recursive': 'True'})
        }
    }

    complete_apps = ['blog']
