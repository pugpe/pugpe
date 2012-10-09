# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sponsor'
        db.create_table('events_sponsor', (
            ('partner_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['events.Partner'], unique=True, primary_key=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('events', ['Sponsor'])

        # Adding model 'Partner'
        db.create_table('events_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('events', ['Partner'])

        # Adding model 'Support'
        db.create_table('events_support', (
            ('partner_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['events.Partner'], unique=True, primary_key=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('events', ['Support'])

        # Adding M2M table for field partners on 'Event'
        db.create_table('events_event_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['events.event'], null=False)),
            ('partner', models.ForeignKey(orm['events.partner'], null=False))
        ))
        db.create_unique('events_event_partners', ['event_id', 'partner_id'])

    def backwards(self, orm):
        # Deleting model 'Sponsor'
        db.delete_table('events_sponsor')

        # Deleting model 'Partner'
        db.delete_table('events_partner')

        # Deleting model 'Support'
        db.delete_table('events_support')

        # Removing M2M table for field partners on 'Event'
        db.delete_table('events_event_partners')

    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'full_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geo.Location']"}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['events.Partner']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'submission_deadline': ('django.db.models.fields.DateTimeField', [], {})
        },
        'events.eventtalk': {
            'Meta': {'object_name': 'EventTalk'},
            'end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['submission.Talk']"})
        },
        'events.partner': {
            'Meta': {'object_name': 'Partner'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'events.sponsor': {
            'Meta': {'object_name': 'Sponsor', '_ormbases': ['events.Partner']},
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'partner_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['events.Partner']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'events.support': {
            'Meta': {'object_name': 'Support', '_ormbases': ['events.Partner']},
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'partner_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['events.Partner']", 'unique': 'True', 'primary_key': 'True'})
        },
        'geo.location': {
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
        'submission.talk': {
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