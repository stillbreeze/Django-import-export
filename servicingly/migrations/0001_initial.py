# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AclTitle', models.CharField(max_length=255, verbose_name='ACL title')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brandTitle', models.CharField(max_length=255, verbose_name='Brand title')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryTitle', models.CharField(max_length=255, verbose_name='Category title')),
                ('brand', models.ForeignKey(to='servicingly.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productTitle', models.CharField(max_length=255, verbose_name='Product title')),
                ('brand', models.ForeignKey(to='servicingly.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productDetailTitle', models.CharField(max_length=255, verbose_name='Product detail title')),
                ('product', models.ForeignKey(to='servicingly.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleTitle', models.CharField(max_length=255, verbose_name='Role title')),
            ],
        ),
        migrations.CreateModel(
            name='RoleMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleMappingTitle', models.CharField(max_length=255, verbose_name='Role mapping title')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceCenterTitle', models.CharField(max_length=255, verbose_name='Service center title')),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticketCategoryTitle', models.CharField(max_length=255, verbose_name='Ticket category title')),
            ],
        ),
    ]
