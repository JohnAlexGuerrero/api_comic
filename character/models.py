from django.db import models

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'famale'),
    ('U', 'unknown'),
)

SPECIES_CHOICES = (
    ('H', 'human'),
    ('D', 'dios'),
    ('M', 'mutant'),
    ('U', 'unknown'),
)

class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, blank=True, null=True)
    species = models.CharField(choices=SPECIES_CHOICES, max_length=50)
    is_hero = models.BooleanField()
    avatar = models.ImageField(upload_to='character/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/api/v1/characters/{self.slug}'


    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' +  self.avatar.url
        return ''
    
    
    