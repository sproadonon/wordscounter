""" Views funtions """

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'name': 'Spéro'})


def count(request):
    fulltext = request.GET['fulltext']

    wordslist = fulltext.split()

    wordsdictionnary = {}

    for word in wordslist:

        if word in wordsdictionnary:
            wordsdictionnary[word] += 1
        else:
            wordsdictionnary[word] = 1

    return render(request, 'count.html', {'numberOfWords': len(wordslist),
                                          'fulltext': fulltext,
                                          'worddict': wordsdictionnary.items()
                                          })
