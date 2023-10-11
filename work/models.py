from django.db import models
from skill.models import Skill


class Work(models.Model):
    photo = models.ImageField(upload_to='works/', null=True, blank=True, verbose_name='Foto')
    title = models.CharField(max_length=200, unique=True, verbose_name='Título')
    skill = models.ManyToManyField(Skill, verbose_name='Lenguajes')
    date_project = models.DateField(verbose_name='Fecha del Proyecto')
    observation = models.CharField(max_length=200, null=True, blank=True, verbose_name='Observación')
    link_github = models.CharField(max_length=200, null=True, blank=True, verbose_name='Link GitHub')
    link_website = models.CharField(max_length=200, null=True, blank=True, verbose_name='Link Página Web')
    is_work = models.BooleanField(verbose_name='Es Trabajo')
    is_design = models.BooleanField(verbose_name='Es Diseño')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Trabajo/Diseño'
        verbose_name_plural = 'Trabajos/Diseños'
