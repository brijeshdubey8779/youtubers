# Generated by Django 4.2.2 on 2023-06-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_slider_butoon_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='butoon_link',
            new_name='button_link',
        ),
    ]
