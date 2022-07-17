from django.db import models

# Create your models here.
class Home(models.Model):
    text_propaganda = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='fotos')
    titulo = models.CharField(max_length=150)
    text_button = models.CharField(max_length=150)
    info1 = models.CharField(max_length=50)
    info2 = models.CharField(max_length=50)
    info3 = models.CharField(max_length=50)

class Quemsomos(models.Model):
    titulo = models.CharField(max_length=150)
    text_fundador = models.CharField(max_length=50)
    img_fundador = models.ImageField(upload_to='foca')
    text_cargo = models.CharField(max_length=50)
    historia = models.TextField()
    text_frase = models.CharField(max_length=150)
    text_autor = models.CharField(max_length=20)

class Produtos(models.Model):
    titulo_produto = models.CharField(max_length=20)
    img_produto = models.ImageField(upload_to='produtos')
    text_button = models.CharField(max_length=20)

class Propaganda(models.Model):
    titulo = models.CharField(max_length=200)
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    text3 = models.CharField(max_length=100)

class Depoimento(models.Model):
    img_pessoa = models.ImageField(upload_to='pessoas')
    nome = models.CharField(max_length=50)
    comentario = models.TextField()

class Contato(models.Model):
    link = models.TextField()
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)


