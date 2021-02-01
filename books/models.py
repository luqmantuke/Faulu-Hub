from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from FAULU_HUB.utils import unique_slug_generator
from django.urls import reverse
from ckeditor.fields import RichTextField

class Level(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Books(models.Model):
    POPULARITY_CHOICE = (('Popular', 'popular'), ('Normal', 'normal'))
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=250, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.FileField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    popular = models.CharField(max_length=20, choices=POPULARITY_CHOICE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Books)