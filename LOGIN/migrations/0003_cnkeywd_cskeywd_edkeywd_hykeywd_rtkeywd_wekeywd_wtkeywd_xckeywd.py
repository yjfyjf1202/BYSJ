# Generated by Django 3.1.6 on 2021-03-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0002_auto_20210301_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('cnkeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CsKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('cskeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EdKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('edkeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HyKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('hykeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RtKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('rtkeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WeKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('wekeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WtKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('wtkeywd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='XcKeyWd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('xckeywd', models.CharField(max_length=255)),
            ],
        ),
    ]
