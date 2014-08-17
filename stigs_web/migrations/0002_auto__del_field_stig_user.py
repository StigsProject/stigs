# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Stig.user'
        db.delete_column(u'stigs_web_stig', 'user_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Stig.user'
        raise RuntimeError("Cannot reverse this migration. 'Stig.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Stig.user'
        db.add_column(u'stigs_web_stig', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'stigs_web.stig': {
            'Meta': {'object_name': 'Stig'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['stigs_web']