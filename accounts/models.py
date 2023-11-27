from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField()
    class Meta:
        ordering = ['-id']


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='', verbose_name='เพศ')
    work_group = models.CharField(max_length=150, verbose_name='กลุ่มงาน')
    position = models.CharField(max_length=150, verbose_name='ตำแหน่ง')
    phone = models.CharField(max_length=10, verbose_name='เบอร์โทรศัพท์มือถือ')
    img = models.ImageField(upload_to='Image_users', default='', verbose_name='รูปโปรไฟล์')
    updatedAt = models.DateTimeField(auto_now=True, blank=False)
   
    def __str__(self):
        return str(self.user) + str(self.gender) + str(self.position) + self.phone

    def image(self):
        if self.img:
            return format_html('<img src="' + self.img.url + '" height="40px">')
        return ''
    image.allow_tags = True