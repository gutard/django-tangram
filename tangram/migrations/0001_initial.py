# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unite'
        db.create_table(u'tangram_unite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branche', self.gf('django.db.models.fields.IntegerField')()),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('inscr_explogram', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('inscr_congram', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('inscr_tangram', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('theme_explogram', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('etat_explogram', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('effectif', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('fg1_theme', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg1_projet', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg2_votants', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg2_elus', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg2_adresses', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg2_propositions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg3_date', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg3_temps', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg3_forme', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg4_theme', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg4_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg4_taches', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg4_roles', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg4_partenaire', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg4_materiel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg4_reunions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg5_theme', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg5_texte', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg5_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('fg6_theme', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg6_date', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg6_descriptif', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg6_positifs', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg7_theme', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fg7_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fg7_install', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg7_presentation', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg7_espace', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fg7_micro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg7_ecran', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg7_expo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fg7_autre', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'tangram', ['Unite'])


    def backwards(self, orm):
        # Deleting model 'Unite'
        db.delete_table(u'tangram_unite')


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
            'fg1_projet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg1_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg2_adresses': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_elus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_propositions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg2_votants': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg3_date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg3_forme': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg3_temps': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg4_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg4_materiel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_partenaire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_reunions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg4_roles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_taches': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg4_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg5_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fg5_texte': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg5_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg6_date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg6_descriptif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg6_positifs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg6_theme': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fg7_autre': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg7_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fg7_ecran': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_espace': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg7_expo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fg7_install': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fg7_micro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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