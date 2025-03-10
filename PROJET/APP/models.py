from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nom