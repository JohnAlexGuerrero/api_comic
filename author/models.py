from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to="authors/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

