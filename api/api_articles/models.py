from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    ETAT_CHOIX = [
        ('En attente', 'En attente'),
        ('Validé', 'Validé'),
    ]
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    etat = models.CharField(max_length=20, choices=ETAT_CHOIX, default='En attente')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

