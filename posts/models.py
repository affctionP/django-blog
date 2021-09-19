from config import settings


from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import files
from django.utils.text import slugify
from django.utils import timezone
import datetime

import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Create your models here.

class IpAddress(models.Model):
	ip_address = models .GenericIPAddressField()
	pub_date= models. DateTimeField()
	class Meta:
		verbose_name = "آی‌پی"
		verbose_name_plural = "آی‌پی ها"
		ordering = ['pub_date']

	def __str__(self):
		return self.ip_address





class Category(models.Model):
	name=models.CharField(max_length=50 , verbose_name="عنوان دسته بندی")
	slug=models.SlugField()

	class Meta :
		verbose_name = "دسته بندی"
		verbose_name_plural="دسته بندی ها"
		

	def __str__(self):
		return self.name
	
	

	def get_absolute_url(self):
		return reverse('posts:listed-by-cat', args=[self.slug])
"""@deconstructible
class  image_path(object):
	def __init__(self,path) -> None:
		self.sub_path = path
	def __call__(self,instance,filename):
		ext = filename.split()[-1]
		if instance.id:
			filename = f'{instance.id}.{ext}'

		else:
			filename = f'{uuid4()}.{ext}'
		return os.path.join(self.sub_path,str (instance.id),filename)"""
			


class PostModel(models.Model):
	def image_path(instance , filename):
		path_u = "image"
		ext = filename.split()[-1]
	

		if instance.id:
			filename = f'{instance.id}.{ext}'

		else:
			filename = f'{uuid4()}.{ext}'
		return os.path.join(path_u,filename)




	

	CHOICES=(
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		
	)

	title = models.CharField (max_length=200, verbose_name="عنوان")
	body =  models.TextField (verbose_name="متن ")
	category = models.ForeignKey(Category,related_name="posts",verbose_name="دسته بندی نوشته",null=True,on_delete=models.SET_NULL, blank=True)
	created = models.DateTimeField(auto_now_add=True )
	#created = jmodels.jDateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now=True,verbose_name="زمان اخرین تغییر")
	#updated = jmodels.jDateTimeField(auto_now=True,verbose_name="زمان اخرین تغییر")
	thumnail = models.ImageField (verbose_name="تصویر" ,max_length=255, null=True,blank=True,upload_to =image_path) 
	auther = models.ForeignKey (User ,verbose_name="نویسنده" ,on_delete=models.CASCADE )
	slug = models.SlugField(unique=True,allow_unicode=True)
	publish = models.DateTimeField(default=timezone.now(),verbose_name="زمان انتشار")
	#publish = jmodels.jDateTimeField(default=timezone.now,verbose_name="زمان انتشار")
	status = models.CharField(max_length=1,verbose_name=",وضصیت",choices=CHOICES,default='d')
	views = models.ManyToManyField(IpAddress,through="hits",blank=True,verbose_name="بازدید ها ",related_name="views")
	
	def save (self,*args,**kwargs):
		if not self.slug:
			self.slug=slugify(self.title, allow_unicode=True) 
		super(PostModel,self).save(*args,**kwargs)
	

	def get_absolute_url(self):

		return reverse('posts:single', args=[str(self.slug)])

	class Meta:
		verbose_name="پست"
		verbose_name_plural = "پست ها"
		ordering = ['-publish']
	@property
	def img_url(self):
		if self.thumnail and hasattr(self.thumnail, 'url'):
			return self.thumnail.url



	def __str__(self):
		return self.title

class Comment(models.Model):
	text=models.TextField(verbose_name="متن دیدگاه")
	name = models.CharField(max_length=100,verbose_name="نام کاربر",blank=True)
	email = models.EmailField(verbose_name="ایمیل")
	post = models.ForeignKey(PostModel, null=True, on_delete=models.SET_NULL, related_name="comments", verbose_name="پست")
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False, verbose_name="تایید")
	reply = models.ForeignKey('self' , null=True, blank=True, related_name='replies',verbose_name= "پاسخ کاربران",on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name = "نظر"
		verbose_name_plural = "نظرات"
		# sort comments in chronological order by default
		ordering = ['created']


	def full_name (self):
		if self.name:
			return self.name
		else :
			return "کاربر ناشناس"


	def __str__(self):
		return " {} گفته است ".format(self.full_name(),self.created)

class hits(models.Model):
	ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
	post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
	creted = models.DateTimeField (auto_now_add=True)


class Note(models.Model):
	CHOICES=(
		('h', 'مخفی'),		 # draft
		('s', "نمایش در سایت"),		
	)
	body = models.TextField( verbose_name= "متن")
	status = models.CharField(max_length=1,choices=CHOICES,default='h')
	class Meta :
		verbose_name = "نوشته کوتاه "
		verbose_name_plural ="نوشته های کوتاه"
	def __str__(self):
		return "نوشته ی"+str(self.id)





