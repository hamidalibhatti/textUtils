# I have created this file - Hamid
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello Hamid")
    return render(request,'index.html')

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    # Analyze the Text
    if removepunc == 'on':
        punctuations = '''!@#$%^&*(),<>.:;"'?/|\{}[]'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(capitalize == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Capitalized Text','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed New Lines','analyzed_text':analyzed}
        djtext = analyzed

    if(spaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed}


    if(removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and spaceremover != 'on'):
        return HttpResponse("Error")

    return render(request,'analyzer.html', params)
