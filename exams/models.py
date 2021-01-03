from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from FAULU_HUB.utils import unique_slug_generator
from django.urls import reverse

exams_choices = [
    ('Necta', 'Necta'),
    ('Non-Necta', 'Non-Necta')
]


class ExamsType(models.Model):
    type = models.CharField(max_length=50, choices=exams_choices)
    def __str__(self):
        return self.type
    


class Form(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()


    def __str__(self):
        return self.name


class Subject(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/subject', null=True)
    
    
    def __str__(self):
        return self.name
    

class ExamContent(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    exams_type = models.ForeignKey(ExamsType, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/notes', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def get_absolute_url(self):
        return reverse("exam_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

def slug_generator(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 


pre_save.connect(slug_generator, sender = ExamContent)
