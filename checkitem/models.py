from django.db import models
from dropdown.models import Itemname, ListNumber, NumberList, Person, Locations, CheckList
from django.utils.html import format_html

# Create your models here.

class CheckItem(models.Model):
    # user = models.CharField(max_length=50, blank=True, null=True, verbose_name='ผู้ตรวจเช็ค')
    DAMAGE_CHOICES = [
        ("ชำรุด", "ชำรุด"),
        ("เสื่อม", "เสื่อม"),
        ("สูญไป", "สูญไป"),
        ("ไม่ใช้", "ไม่ใช้"),
        ("ใช้อยู่", "ใช้อยู่"),
    ]

    user_check = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ผู้ตรวจเช็ค', related_name='user_check_items')
    # Itemname = models.ForeignKey(Itemname, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ครุภัณฑ์')
    # NumberList = models.ForeignKey(NumberList, on_delete=models.CASCADE, blank=True, null=True, verbose_name='เลขครุภัณฑ์' )
    listnumber = models.ForeignKey(ListNumber, on_delete=models.CASCADE, blank=True, null=True, verbose_name='รายการครุภัณฑ์และเลขครุภัณฑ์' )
    note_list = models.CharField(max_length=250, blank=True, null=True, verbose_name='หมายเหตุ(รายการครุภัณฑ์)')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ผู้รับผิดชอบ', related_name='person_items')
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE, blank=True, null=True, verbose_name='สถานที่ใช้งานในปัจจุบัน')
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='ยี่ห้อ/รุ่น')
    # CheckList = models.ForeignKey(CheckList, on_delete=models.CASCADE, blank=True, null=True, verbose_name='สถานะที่ตรวจพบ' )
    checkList = models.CharField(max_length=10, choices=DAMAGE_CHOICES, blank=True, null=True, verbose_name="สถานะที่ตรวจพบ")
    note = models.CharField(max_length=250, blank=True, null=True, verbose_name='หมายเหตุ')
    date_check = models.DateTimeField(blank=True, null=True, verbose_name='วันที่ตรวจสอบ')
    year = models.CharField(max_length=4, blank=True, null=True, default='2566', verbose_name='ปีที่ตรวจ')
    image_1 = models.ImageField(upload_to='upload', blank=True, null=True, verbose_name='รูป 1')
    image_2 = models.ImageField(upload_to='upload', blank=True, null=True, verbose_name='รูป 2')
    image_3 = models.ImageField(upload_to='upload', blank=True, null=True, verbose_name='รูป 3')

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'ตรวจสอบครุภัณฑ์'

    # def __str__(self):
    #     return self.Itemname

    def show_image(self):
        if self.image_1:
            return format_html('<img src="'+self.image_1.url +'" height="40px">')
        return ''
    show_image.allow_tags = True
    