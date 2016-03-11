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
    category = models.ForeignKey(Category)
    page_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=128, default=0)
    answer = models.CharField(max_length=128, default=0)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __unicode__(self) : #Python2, use __str__ on Python3
        return self.title

class UserProfile(models.Model) :
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images' , blank=True)
    def __unicode__( self) :
        return self.user.username