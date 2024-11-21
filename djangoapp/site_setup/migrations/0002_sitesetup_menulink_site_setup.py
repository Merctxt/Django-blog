# Generated by Django 5.1.3 on 2024-11-21 21:58

import django.db.models.deletion
import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=255)),
                ('show_header', models.BooleanField(default=True)),
                ('show_search', models.BooleanField(default=True)),
                ('show_menu', models.BooleanField(default=True)),
                ('show_description', models.BooleanField(default=True)),
                ('show_pagination', models.BooleanField(default=True)),
                ('show_footer', models.BooleanField(default=True)),
                ('favicon', models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validators.validate_png])),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
            },
        ),
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup'),
        ),
    ]
