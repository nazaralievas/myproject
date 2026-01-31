from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    date_created = models.DateTimeField(auto_now_add=True)
    name_lower = models.CharField(max_length=255, editable=False, null=True)

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        super(Movie, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return f"Фильм: {self.name}"


from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
