# Generated by Django 4.2.7 on 2023-11-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkitem', '0006_alter_checkitem_imgge_1_alter_checkitem_imgge_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkitem',
            old_name='imgge_1',
            new_name='image_1',
        ),
        migrations.RenameField(
            model_name='checkitem',
            old_name='imgge_2',
            new_name='image_2',
        ),
        migrations.RenameField(
            model_name='checkitem',
            old_name='imgge_3',
            new_name='image_3',
        ),
    ]
