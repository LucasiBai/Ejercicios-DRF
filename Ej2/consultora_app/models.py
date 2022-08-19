from django.db import models

# Create your models here.
LANG_CHOICES = (
    ("js", "Javascript"),
    ("python", "Python"),
    ("c", "C"),
    ("java", "Java"),
    ("php", "PHP"),
)


class Programmer(models.Model):
    nick = models.CharField(max_length=16)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    program_lang = models.CharField(max_length=32, choices=LANG_CHOICES)
