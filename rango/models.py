#coding=utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model) :
    name = models.CharField( max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __unicode__(self) :
        return self.name
class Page(models.Model) :
    category = models.ForeignKey(Category)#所属科目（选项）
    page_id = models.IntegerField(unique=True,default=0)#题目的唯一ID
    stage = models.CharField(max_length=128)#所属阶段（选项）
    mytype = models.CharField(max_length=28, default=0)#题目类型（选项单选、多选、判断、填空、简答、代码、实操）
    key = models.CharField(max_length=28, default=0)#关键字
    level = models.CharField(max_length=28, default=0)#难度等级（选项ABCD）
    body = models.CharField(max_length=128, default=0)#题干
    option_A = models.CharField(max_length=128, default=0)#A 选项
    option_B = models.CharField(max_length=128, default=0)#B 选项
    option_C = models.CharField(max_length=128, default=0)#C 选项
    option_D = models.CharField(max_length=128, default=0)#D 选项
    option_E = models.CharField(max_length=128, default=0)#E 选项
    option_F = models.CharField(max_length=128, default=0)#F 选项  
    information = models.CharField(max_length=28, default=0)#所属知识点（读关联  分隔;）
    answer = models.CharField(max_length=128, default=0)#答案
    explain = models.CharField(max_length=1028, default=0)#答案说明
    author = models.CharField(max_length=1028, default=0)#出题人
    def __unicode__(self) : #Python2, use __str__ on Python3
        return self.page_id

class UserProfile(models.Model) :
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images' , blank=True)
    def __unicode__( self) :
        return self.user.username