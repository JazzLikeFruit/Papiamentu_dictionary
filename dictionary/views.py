from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    return render(request, 'home_page.html', {})

def search_engine(resquest):
    return HttpResponse('<h1>helooooo</h1>')

def word_api(resquest, api_word):
    dict= {}

    try:
        word_meaning = Words.objects.get(word=api_word)
        return HttpResponse(f'<h1>{word_meaning.meaning}</h1>')
    except:
        word_meaning = Words.objects.filter(word__contains=api_word).all()
        for word in word_meaning:
            dict[word.word] = word.meaning
        return HttpResponse(f'<h1>{dict}</h1>')
