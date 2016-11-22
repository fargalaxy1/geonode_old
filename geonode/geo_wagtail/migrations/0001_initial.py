# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo_wagtail_Page',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('main_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('map', models.ForeignKey(related_name='geo_wagtail_set', blank=True, to='maps.Map', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('intro', models.CharField(max_length=250)),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('maps', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='maps.Map', null=True)),
            ],
            options={
                'verbose_name': 'Homepage',
            },
            bases=('wagtailcore.page',),
        ),
    ]
