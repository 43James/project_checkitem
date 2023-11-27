# Generated by Django 4.2.7 on 2023-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_list', models.CharField(blank=True, max_length=10, null=True, verbose_name='รายการเสียหายใช้อยู่หรือไม่ใช้')),
            ],
            options={
                'verbose_name_plural': 'รายการเสียหายใช้อยู่หรือไม่ใช้',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Itemname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=250, verbose_name='รายการครุภัณฑ์')),
            ],
            options={
                'verbose_name_plural': 'รายการครุภัณฑ์',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, verbose_name='สถานที่ตั้ง')),
            ],
            options={
                'verbose_name_plural': 'รายการสถานที่ตั้ง',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='NumberList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=2, verbose_name='หน่วย')),
                ('type_1', models.CharField(max_length=5, verbose_name='ประเภท')),
                ('type_2', models.CharField(max_length=5, verbose_name='ชนิด')),
                ('type_3', models.CharField(max_length=5, verbose_name='ลักษณะ')),
                ('degree', models.CharField(max_length=10, verbose_name='ลำดับ/ปี')),
            ],
            options={
                'verbose_name_plural': 'รายการเลขครุภัณฑ์',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ผู้รับผิดชอบ')),
            ],
            options={
                'verbose_name_plural': 'รายการผู้รับผิดชอบ',
                'ordering': ('id',),
            },
        ),
    ]