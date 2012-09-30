# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventTalk'
        db.create_table('events_eventtalk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Talk'])),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('events', ['EventTalk'])

        # Adding field 'Event.pub_date'
        db.add_column('events_event', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 9, 29, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Location.pub_date'
        db.add_column('events_location', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 9, 29, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Talk.event'
        db.delete_column('events_talk', 'event_id')

    def backwards(self, orm):
        # Deleting model 'EventTalk'
        db.delete_table('events_eventtalk')

        # Deleting field 'Event.pub_date'
        db.delete_column('events_event', 'pub_date')

        # Deleting field 'Location.pub_date'
        db.delete_column('events_location', 'pub_date')

        # Adding field 'Talk.event'
        db.add_column('events_talk', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Event']),
                      keep_default=False)

    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'full_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Location']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'events.eventtalk': {
            'Meta': {'object_name': 'EventTalk'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Talk']"})
        },
        'events.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'events.talk': {
            'Meta': {'object_name': 'Talk'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'macro_theme': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'talk_once': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['events']