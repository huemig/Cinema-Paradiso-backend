from django.db import models
from cloudinary.models import CloudinaryField
from apps.Category.models import Category



class Movies(models.Model):
    
    MY_CHOICES = (
        ('Newly Released','Newly Released'),
        ("Coming Soon", 'Coming Soon')
    )

    class Meta(object):
        db_table = 'Movies'
    image = CloudinaryField('image', blank=False )
    image_mobile = CloudinaryField('image mobile', blank=False)
    title = models.CharField('title', blank=False, max_length=35)
    description = models.TextField('description', blank=True, max_length=1000)
    movie_duration = models.IntegerField(blank=False)
    trailer_link= models.URLField(max_length=350)
    created_at = models.DateTimeField( 'created datetime', auto_now_add=True)
    updated_at = models.DateTimeField('created datetime', auto_now=True)
    state= models.CharField('state', default='USA', blank=False, max_length=20)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_type = models.CharField(
        'Release Type', blank=False,null=False,max_length=50,choices=MY_CHOICES
    )
    