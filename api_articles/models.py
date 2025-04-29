from django.db import models
from django.contrib.auth.models import AbstractUser
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

# Hériter de la classe AbstractUser pour utiliser le modèle User fourni par Django
class Utilisateur(AbstractUser):
    ROLE_CHOICES = (
        ('redacteur', 'Rédacteur'),
        ('validateur', 'Validateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"