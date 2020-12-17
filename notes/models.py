from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from FAULU_HUB.utils import unique_slug_generator
from django.urls import reverse

class Form(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()

    

    def __str__(self):
        return self.name


class Subject(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/subject', null=True)
    
    
    def __str__(self):
        return self.name
    

class Content(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/notes', null=True)

    def get_absolute_url(self):
        return reverse("content_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

def slug_generator(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 


pre_save.connect(slug_generator, sender = Content)