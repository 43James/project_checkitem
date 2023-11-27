from django.db import models

# Create your models here.
class Itemname(models.Model):
    list = models.CharField(max_length=250, verbose_name='รายการครุภัณฑ์')
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการครุภัณฑ์'

    def __str__(self):
        return self.list
    

class ListNumber(models.Model):
    list = models.CharField(max_length=100, verbose_name='รายการครุภัณฑ์')
    unit = models.CharField(max_length=2, verbose_name='หน่วย')
    type_1 = models.CharField(max_length=5, verbose_name='ประเภท')
    type_2 = models.CharField(max_length=5, verbose_name='ชนิด')
    type_3 = models.CharField(max_length=5, verbose_name='ลักษณะ')
    degree = models.CharField(max_length=10, verbose_name='ลำดับ/ปี')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการครุภัณฑ์และเลขครุภัณฑ์'

    def __str__(self):
        # return str(self.unit) + str(self.type_1) + str(self.type_2) + str(self.type_3) + str(self.degree)
        return f"{self.list} | {self.unit} | {self.type_1} | {self.type_2} | {self.type_3} | {self.degree}"
    

class NumberList(models.Model):
    unit = models.CharField(max_length=2, verbose_name='หน่วย')
    type_1 = models.CharField(max_length=5, verbose_name='ประเภท')
    type_2 = models.CharField(max_length=5, verbose_name='ชนิด')
    type_3 = models.CharField(max_length=5, verbose_name='ลักษณะ')
    degree = models.CharField(max_length=10, verbose_name='ลำดับ/ปี')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการเลขครุภัณฑ์'

    def __str__(self):
        # return str(self.unit) + str(self.type_1) + str(self.type_2) + str(self.type_3) + str(self.degree)
        return f"{self.unit} | {self.type_1} | {self.type_2} | {self.type_3} | {self.degree}"


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='ผู้รับผิดชอบ')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการผู้รับผิดชอบ'

    def __str__(self):
        return self.name
    

class Locations(models.Model):
    location = models.CharField(max_length=100, verbose_name='สถานที่ตั้ง')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการสถานที่ตั้ง'

    def __str__(self):
        return self.location
    

class CheckList(models.Model):
    check_list = models.CharField(max_length=10, blank=True, null=True, verbose_name='รายการเสียหายใช้อยู่หรือไม่ใช้')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'รายการเสียหายใช้อยู่หรือไม่ใช้'

    def __str__(self):
        return self.check_list