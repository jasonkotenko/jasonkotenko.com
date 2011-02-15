# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Resource'
        db.create_table('library_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('URL', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('library', ['Resource'])

        # Adding M2M table for field related on 'Resource'
        db.create_table('library_resource_related', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['library.resource'], null=False)),
            ('post', models.ForeignKey(orm['posts.post'], null=False))
        ))
        db.create_unique('library_resource_related', ['resource_id', 'post_id'])

        # Adding model 'Book'
        db.create_table('library_book', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Resource'], unique=True, primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('library', ['Book'])

        # Adding model 'Article'
        db.create_table('library_article', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Resource'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('library', ['Article'])

        # Adding model 'Technology'
        db.create_table('library_technology', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Resource'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('library', ['Technology'])

        # Adding M2M table for field articles on 'Technology'
        db.create_table('library_technology_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('technology', models.ForeignKey(orm['library.technology'], null=False)),
            ('article', models.ForeignKey(orm['library.article'], null=False))
        ))
        db.create_unique('library_technology_articles', ['technology_id', 'article_id'])

        # Adding model 'Library'
        db.create_table('library_library', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('introduction', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('library', ['Library'])

        # Adding M2M table for field books on 'Library'
        db.create_table('library_library_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('library', models.ForeignKey(orm['library.library'], null=False)),
            ('book', models.ForeignKey(orm['library.book'], null=False))
        ))
        db.create_unique('library_library_books', ['library_id', 'book_id'])

        # Adding M2M table for field articles on 'Library'
        db.create_table('library_library_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('library', models.ForeignKey(orm['library.library'], null=False)),
            ('article', models.ForeignKey(orm['library.article'], null=False))
        ))
        db.create_unique('library_library_articles', ['library_id', 'article_id'])

        # Adding M2M table for field technologies on 'Library'
        db.create_table('library_library_technologies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('library', models.ForeignKey(orm['library.library'], null=False)),
            ('technology', models.ForeignKey(orm['library.technology'], null=False))
        ))
        db.create_unique('library_library_technologies', ['library_id', 'technology_id'])


    def backwards(self, orm):
        
        # Deleting model 'Resource'
        db.delete_table('library_resource')

        # Removing M2M table for field related on 'Resource'
        db.delete_table('library_resource_related')

        # Deleting model 'Book'
        db.delete_table('library_book')

        # Deleting model 'Article'
        db.delete_table('library_article')

        # Deleting model 'Technology'
        db.delete_table('library_technology')

        # Removing M2M table for field articles on 'Technology'
        db.delete_table('library_technology_articles')

        # Deleting model 'Library'
        db.delete_table('library_library')

        # Removing M2M table for field books on 'Library'
        db.delete_table('library_library_books')

        # Removing M2M table for field articles on 'Library'
        db.delete_table('library_library_articles')

        # Removing M2M table for field technologies on 'Library'
        db.delete_table('library_library_technologies')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'library.article': {
            'Meta': {'ordering': "['title']", 'object_name': 'Article', '_ormbases': ['library.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['library.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'library.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book', '_ormbases': ['library.Resource']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['library.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'library.library': {
            'Meta': {'object_name': 'Library'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['library.Article']", 'null': 'True', 'blank': 'True'}),
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['library.Book']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['library.Technology']", 'null': 'True', 'blank': 'True'})
        },
        'library.resource': {
            'Meta': {'ordering': "['title']", 'object_name': 'Resource'},
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['posts.Post']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'library.technology': {
            'Meta': {'ordering': "['title']", 'object_name': 'Technology', '_ormbases': ['library.Resource']},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Article']", 'symmetrical': 'False'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['library.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'up_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['library']
