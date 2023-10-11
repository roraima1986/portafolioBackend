from django.db import models
from skill.models import Skill


class About(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    photo = models.ImageField(upload_to='about/', null=True, blank=True, verbose_name='Foto')
    description = models.TextField(verbose_name='Descripción')
    skill = models.ManyToManyField(Skill, verbose_name='Habilidades')
    is_published = models.BooleanField(default=True, verbose_name='Publicado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Resumen'
        verbose_name_plural = 'Resumen'
