# Generated by Django 4.2.7 on 2023-11-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkitem', '0002_checkitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkitem',
            name='status',
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='CheckList',
            field=models.CharField(blank=True, choices=[('ชำรุด', 'ชำรุด'), ('เสื่อม', 'เสื่อม'), ('สูญไป', 'สูญไป'), ('ไม่ใช้', 'ไม่ใช้'), ('ใช้อยู่', 'ใช้อยู่')], max_length=10, null=True, verbose_name='สถานะที่ตรวจพบ'),
        ),
    ]
