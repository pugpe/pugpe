# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attendee.event'
        db.add_column('cert_attendee', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Event']),
                      keep_default=False)

        # Removing M2M table for field events on 'Attendee'
        db.delete_table('cert_attendee_events')

        # Adding unique constraint on 'Attendee', fields ['email', 'event']
        db.create_unique('cert_attendee', ['email', 'event_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'Attendee', fields ['email', 'event']
        db.delete_unique('cert_attendee', ['email', 'event_id'])

        # Deleting field 'Attendee.event'
        db.delete_column('cert_attendee', 'event_id')

        # Adding M2M table for field events on 'Attendee'
        db.create_table('cert_attendee_events', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('attendee', models.ForeignKey(orm['cert.attendee'], null=False)),
            ('event', models.ForeignKey(orm['events.event'], null=False))
        ))
        db.create_unique('cert_attendee_events', ['attendee_id', 'event_id'])

    models = {
        'cert.attendee': {
            'Meta': {'unique_together': "(('email', 'event'),)", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'cert.signature': {
            'Meta': {'object_name': 'Signature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'full_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geo.Location']"}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['events.Partner']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cert.Signature']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'submission_deadline': ('django.db.models.fields.DateTimeField', [], {})
        },
        'events.partner': {
            'Meta': {'object_name': 'Partner'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['cert']