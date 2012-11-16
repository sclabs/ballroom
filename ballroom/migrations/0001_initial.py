# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table('ballroom_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('ballroom', ['Level'])

        # Adding model 'Style'
        db.create_table('ballroom_style', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('ballroom', ['Style'])

        # Adding model 'Dance'
        db.create_table('ballroom_dance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dances', to=orm['ballroom.Style'])),
        ))
        db.send_create_signal('ballroom', ['Dance'])

        # Adding model 'Position'
        db.create_table('ballroom_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lead_weight', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('follow_weight', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('hold', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('inside_partner', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('ballroom', ['Position'])

        # Adding model 'Figure'
        db.create_table('ballroom_figure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dance', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figures', to=orm['ballroom.Dance'])),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figures', to=orm['ballroom.Level'])),
            ('cross_phrase', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('start_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='into_options', to=orm['ballroom.Position'])),
            ('end_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_options', to=orm['ballroom.Position'])),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('alt_count', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('lead_steps', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('follow_steps', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ballroom', ['Figure'])

        # Adding model 'Routine'
        db.create_table('ballroom_routine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='routines_created', to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ballroom', ['Routine'])

        # Adding M2M table for field editors on 'Routine'
        db.create_table('ballroom_routine_editors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('routine', models.ForeignKey(orm['ballroom.routine'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('ballroom_routine_editors', ['routine_id', 'user_id'])

        # Adding model 'Video'
        db.create_table('ballroom_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['ballroom.Routine'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ballroom', ['Video'])

        # Adding model 'Profile'
        db.create_table('ballroom_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profiles', to=orm['auth.User'])),
        ))
        db.send_create_signal('ballroom', ['Profile'])

        # Adding M2M table for field friends on 'Profile'
        db.create_table('ballroom_profile_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_profile', models.ForeignKey(orm['ballroom.profile'], null=False)),
            ('to_profile', models.ForeignKey(orm['ballroom.profile'], null=False))
        ))
        db.create_unique('ballroom_profile_friends', ['from_profile_id', 'to_profile_id'])

        # Adding M2M table for field favorites on 'Profile'
        db.create_table('ballroom_profile_favorites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['ballroom.profile'], null=False)),
            ('routine', models.ForeignKey(orm['ballroom.routine'], null=False))
        ))
        db.create_unique('ballroom_profile_favorites', ['profile_id', 'routine_id'])

        # Adding model 'Figure_Instance'
        db.create_table('ballroom_figure_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('figure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['ballroom.Figure'])),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figure_instances', to=orm['ballroom.Routine'])),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ballroom', ['Figure_Instance'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table('ballroom_level')

        # Deleting model 'Style'
        db.delete_table('ballroom_style')

        # Deleting model 'Dance'
        db.delete_table('ballroom_dance')

        # Deleting model 'Position'
        db.delete_table('ballroom_position')

        # Deleting model 'Figure'
        db.delete_table('ballroom_figure')

        # Deleting model 'Routine'
        db.delete_table('ballroom_routine')

        # Removing M2M table for field editors on 'Routine'
        db.delete_table('ballroom_routine_editors')

        # Deleting model 'Video'
        db.delete_table('ballroom_video')

        # Deleting model 'Profile'
        db.delete_table('ballroom_profile')

        # Removing M2M table for field friends on 'Profile'
        db.delete_table('ballroom_profile_friends')

        # Removing M2M table for field favorites on 'Profile'
        db.delete_table('ballroom_profile_favorites')

        # Deleting model 'Figure_Instance'
        db.delete_table('ballroom_figure_instance')


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
        'ballroom.figure_instance': {
            'Meta': {'object_name': 'Figure_Instance'},
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
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ballroom.Figure']", 'through': "orm['ballroom.Figure_Instance']", 'symmetrical': 'False'}),
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