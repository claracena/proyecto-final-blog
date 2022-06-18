from django.db import models

# Create your models here.
choices = [
    [1, 'Consulta'],
    [2, 'Sugerencia'],
    [3, 'Error'],
    [4, 'Otro']
]

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False,verbose_name="")
    email = models.EmailField(null=False,verbose_name="")
    type = models.IntegerField(choices=choices,verbose_name="")
    message = models.TextField(null=False,verbose_name="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.created.strftime('%d/%m/%Y %H:%M')