# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table('socialeditor_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('socialeditor', ['Level'])

        # Adding model 'Style'
        db.create_table('socialeditor_style', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('socialeditor', ['Style'])

        # Adding model 'Dance'
        db.create_table('socialeditor_dance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dances', to=orm['socialeditor.Style'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('espana_cani', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('socialeditor', ['Dance'])

        # Adding model 'Position'
        db.create_table('socialeditor_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lead_weight', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('follow_weight', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('hold', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('inside_partner', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('socialeditor', ['Position'])

        # Adding model 'Figure'
        db.create_table('socialeditor_figure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dance', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figures', to=orm['socialeditor.Dance'])),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figures', to=orm['socialeditor.Level'])),
            ('mirror_figure', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['socialeditor.Figure'], unique=True, null=True)),
            ('cross_phrase', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('start_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='into_options', to=orm['socialeditor.Position'])),
            ('end_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_options', to=orm['socialeditor.Position'])),
            ('rotation', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('alt_count', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('lead_steps', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('follow_steps', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('socialeditor', ['Figure'])

        # Adding model 'Routine'
        db.create_table('socialeditor_routine', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10, primary_key=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='routines_created', to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('socialeditor', ['Routine'])

        # Adding M2M table for field editors on 'Routine'
        db.create_table('socialeditor_routine_editors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('routine', models.ForeignKey(orm['socialeditor.routine'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('socialeditor_routine_editors', ['routine_id', 'user_id'])

        # Adding model 'Video'
        db.create_table('socialeditor_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['socialeditor.Routine'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('socialeditor', ['Video'])

        # Adding model 'Profile'
        db.create_table('socialeditor_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profiles', to=orm['auth.User'])),
        ))
        db.send_create_signal('socialeditor', ['Profile'])

        # Adding M2M table for field friends on 'Profile'
        db.create_table('socialeditor_profile_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_profile', models.ForeignKey(orm['socialeditor.profile'], null=False)),
            ('to_profile', models.ForeignKey(orm['socialeditor.profile'], null=False))
        ))
        db.create_unique('socialeditor_profile_friends', ['from_profile_id', 'to_profile_id'])

        # Adding M2M table for field favorite_routines on 'Profile'
        db.create_table('socialeditor_profile_favorite_routines', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['socialeditor.profile'], null=False)),
            ('routine', models.ForeignKey(orm['socialeditor.routine'], null=False))
        ))
        db.create_unique('socialeditor_profile_favorite_routines', ['profile_id', 'routine_id'])

        # Adding M2M table for field favorite_figures on 'Profile'
        db.create_table('socialeditor_profile_favorite_figures', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['socialeditor.profile'], null=False)),
            ('figure', models.ForeignKey(orm['socialeditor.figure'], null=False))
        ))
        db.create_unique('socialeditor_profile_favorite_figures', ['profile_id', 'figure_id'])

        # Adding model 'FigureInstance'
        db.create_table('socialeditor_figureinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('figure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['socialeditor.Figure'])),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='figure_instances', to=orm['socialeditor.Routine'])),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('socialeditor', ['FigureInstance'])

        # Adding model 'Annotation'
        db.create_table('socialeditor_annotation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('routine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='annotations', to=orm['socialeditor.Routine'])),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('end', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('socialeditor', ['Annotation'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table('socialeditor_level')

        # Deleting model 'Style'
        db.delete_table('socialeditor_style')

        # Deleting model 'Dance'
        db.delete_table('socialeditor_dance')

        # Deleting model 'Position'
        db.delete_table('socialeditor_position')

        # Deleting model 'Figure'
        db.delete_table('socialeditor_figure')

        # Deleting model 'Routine'
        db.delete_table('socialeditor_routine')

        # Removing M2M table for field editors on 'Routine'
        db.delete_table('socialeditor_routine_editors')

        # Deleting model 'Video'
        db.delete_table('socialeditor_video')

        # Deleting model 'Profile'
        db.delete_table('socialeditor_profile')

        # Removing M2M table for field friends on 'Profile'
        db.delete_table('socialeditor_profile_friends')

        # Removing M2M table for field favorite_routines on 'Profile'
        db.delete_table('socialeditor_profile_favorite_routines')

        # Removing M2M table for field favorite_figures on 'Profile'
        db.delete_table('socialeditor_profile_favorite_figures')

        # Deleting model 'FigureInstance'
        db.delete_table('socialeditor_figureinstance')

        # Deleting model 'Annotation'
        db.delete_table('socialeditor_annotation')


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
        'socialeditor.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'end': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'annotations'", 'to': "orm['socialeditor.Routine']"}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'socialeditor.dance': {
            'Meta': {'object_name': 'Dance'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'espana_cani': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dances'", 'to': "orm['socialeditor.Style']"})
        },
        'socialeditor.figure': {
            'Meta': {'object_name': 'Figure'},
            'alt_count': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'count': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'cross_phrase': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figures'", 'to': "orm['socialeditor.Dance']"}),
            'end_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_options'", 'to': "orm['socialeditor.Position']"}),
            'follow_steps': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_steps': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figures'", 'to': "orm['socialeditor.Level']"}),
            'mirror_figure': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['socialeditor.Figure']", 'unique': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rotation': ('django.db.models.fields.IntegerField', [], {}),
            'start_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'into_options'", 'to': "orm['socialeditor.Position']"})
        },
        'socialeditor.figureinstance': {
            'Meta': {'object_name': 'FigureInstance'},
            'figure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['socialeditor.Figure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'figure_instances'", 'to': "orm['socialeditor.Routine']"})
        },
        'socialeditor.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'socialeditor.position': {
            'Meta': {'object_name': 'Position'},
            'follow_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'hold': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inside_partner': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lead_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'socialeditor.profile': {
            'Meta': {'object_name': 'Profile'},
            'favorite_figures': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['socialeditor.Figure']"}),
            'favorite_routines': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorited_by'", 'symmetrical': 'False', 'to': "orm['socialeditor.Routine']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': "orm['socialeditor.Profile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profiles'", 'to': "orm['auth.User']"})
        },
        'socialeditor.routine': {
            'Meta': {'object_name': 'Routine'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'routines_created'", 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'routines_editable'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'figures': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['socialeditor.Figure']", 'through': "orm['socialeditor.FigureInstance']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'primary_key': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'socialeditor.style': {
            'Meta': {'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'socialeditor.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['socialeditor.Routine']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['socialeditor']