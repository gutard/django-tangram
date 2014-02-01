# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Unite.fg2_resultat'
        db.add_column(u'tangram_unite', 'fg2_resultat',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Unite.fg2_resultat'
        db.delete_column(u'tangram_unite', 'fg2_resultat')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tangram.unite': {
            'Meta': {'object_name': 'Unite'},
            'branche': ('django.db.models.fields.IntegerField', [], {}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'effectif': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'etat_explogram': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg1_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg1_projet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg1_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg2_adresses': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_elus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg2_propositions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_resultat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg2_votants': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg3_date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg3_forme': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg3_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg3_temps': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg4_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg4_materiel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_partenaire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_reunions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg4_roles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_taches': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg5_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg5_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fg5_texte': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg5_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg6_date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg6_descriptif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg6_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg6_positifs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg6_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg7_autre': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg7_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg7_ecran': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_espace': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg7_expo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_install': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg7_micro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_presentation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg7_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscr_congram': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'inscr_explogram': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'inscr_tangram': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theme_explogram': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['tangram']