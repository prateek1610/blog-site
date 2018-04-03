from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Register(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name=models.CharField(max_length=250)
    age=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100),MinValueValidator(0)]
        )
    def __str__(self):
        return self.user.username

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    topic=models.CharField(max_length=300)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publishing(self):
        self.publish_date=timezone.now()
        self.save()

    def comments_approve(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments')
    author=models.CharField(max_length=300)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save
    
    def get_absolute_url(self):
        return reverse("post_list")  

    def __str__(self):
        return self.text
