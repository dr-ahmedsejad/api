# Generated by Django 5.1.4 on 2025-01-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_articles', '0002_alter_article_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='etat',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Validé', 'Validé')], default='En attente', max_length=20),
        ),
    ]
