from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Habilidad/Lenguaje'
        verbose_name_plural = 'Habilidades/Lenguajes'