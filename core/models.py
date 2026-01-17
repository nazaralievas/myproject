from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Фильм: {self.name}'


class Comment(models.Model):
    text = models.TextField()
    user = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
