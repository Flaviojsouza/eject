from django.shortcuts import render

from  .models import Home, Quemsomos, Produtos, Propaganda, Depoimento, Contato

# Create your views here.
def Subtela(request):

    home = Home.objects.last()

    produtos = Produtos.objects.all()
    quemsomos = Quemsomos.objects.last()
    propaganda = Propaganda.objects.last()
    contato = Contato.objects.last()
    depoimento = Depoimento.objects.all()

    context = {
        'home' : home ,
        'produtos' : produtos ,
        'propaganda' : propaganda ,
        'contato' : contato ,
        'depoimentos' : depoimento ,
        'quemsomos' : quemsomos,

    }

    return render(request, 'index.html', context)