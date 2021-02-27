from django.db import models
from embed_video.fields import EmbedVideoField
from FAULU_HUB.utils import unique_slug_generator
from django.urls import reverse
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField


class FormClass(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Subject(models.Model):
    name = models.CharField(max_length=1000)
    form = models.ForeignKey(FormClass, on_delete=models.CASCADE, related_name='subject_form')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='videos', null=True)
    form = models.ForeignKey(FormClass, on_delete=models.CASCADE, related_name='topic_subject_form')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topic_subject')
    slug = models.SlugField(null=True, blank=True)
    video = EmbedVideoField(null=True)  # same like models.URLField()
    order = models.PositiveIntegerField(null=True)
    body = RichTextField(blank=True, null=True)
    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name




def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Topic)