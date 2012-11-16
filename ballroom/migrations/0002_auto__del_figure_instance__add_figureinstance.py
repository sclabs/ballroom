# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Figure_Instance'
        db.delete_table('ballroom_figure_instance')

        # Adding model 'FigureInstance'
        db.create_table('ballroom_figureinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('figure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['ballroom.Figure'])),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figure_instances', to=orm['ballroom.Routine'])),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ballroom', ['FigureInstance'])


    def backwards(self, orm):
        # Adding model 'Figure_Instance'
        db.create_table('ballroom_figure_instance', (
            ('index', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('figure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['ballroom.Figure'])),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figure_instances', to=orm['ballroom.Routine'])),
        ))
        db.send_create_signal('ballroom', ['Figure_Instance'])

        # Deleting model 'FigureInstance'
        db.delete_table('ballroom_figureinstance')


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
        'ballroom.dance': {
            'Meta': {'object_name': 'Dance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dances'", 'to': "orm['ballroom.Style']"})
        },
        'ballroom.figure': {
            'Meta': {'object_name': 'Figure'},
            'alt_count': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'count': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'cross_phrase': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figures'", 'to': "orm['ballroom.Dance']"}),
            'end_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_options'", 'to': "orm['ballroom.Position']"}),
            'follow_steps': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_steps': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figures'", 'to': "orm['ballroom.Level']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'into_options'", 'to': "orm['ballroom.Position']"})
        },
        'ballroom.figureinstance': {
            'Meta': {'object_name': 'FigureInstance'},
            'figure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['ballroom.Figure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figure_instances'", 'to': "orm['ballroom.Routine']"})
        },
        'ballroom.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'ballroom.position': {
            'Meta': {'object_name': 'Position'},
            'follow_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'hold': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inside_partner': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lead_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'ballroom.profile': {
            'Meta': {'object_name': 'Profile'},
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorited_by'", 'symmetrical': 'False', 'to': "orm['ballroom.Routine']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': "orm['ballroom.Profile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profiles'", 'to': "orm['auth.User']"})
        },
        'ballroom.routine': {
            'Meta': {'object_name': 'Routine'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'routines_created'", 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'routines_editable'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ballroom.Figure']", 'through': "orm['ballroom.FigureInstance']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'ballroom.style': {
            'Meta': {'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'ballroom.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['ballroom.Routine']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ballroom']