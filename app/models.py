from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    body = models.TextField(null=False,blank=False)
    image = models.FileField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def result_title(self):
        return self.title[:100].upper() + " ..."

    def result_body(self):
        return self.body[:100].upper() + ' ...'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class Photo(models.Model):
    name = models.CharField(max_length=200, null=False,blank=False)
    photo = models.FileField(upload_to='photo', blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
