from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta(object):
        db_table = 'Category'
    name= models.CharField ('name', max_length=50 ,blank=False ,null=False)
    created_at = models.DateTimeField('created datetime', auto_now_add=True)
    updated_at = models.DateTimeField('updated datetime', auto_now=True)
    
    def __str__(self):
        return self.name
    
    
        
