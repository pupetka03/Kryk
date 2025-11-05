from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)



    


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="publications")
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)


    class Meta:
        ordering = ["-created_at"]



    
    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_title = slugify(self.title)
            self.slug = f"{transliterated_title}-{uuid.uuid4()}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.user}, {self.text}, {self.created_at}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'publication')

    def __str__(self):
        return f'{self.user.username}, {self.created_at}'
    



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.user}, {self.text}'

