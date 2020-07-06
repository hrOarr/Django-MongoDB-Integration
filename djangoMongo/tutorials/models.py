from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tutorial(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,null=True)
    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(null=True)
    img1 = models.ImageField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    @property
    def author_full_name(self):
        try:
            return f'{self.author.first_name} {self.author.last_name}'
        except:
            return "Name Not Set"

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
