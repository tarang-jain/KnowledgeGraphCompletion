from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
results='Hello qumar'
def sparql_view(request):
    return render(request, "home.html")

#import templates.nlqpy
from .templates import nlqpy_new, nlqpy2, nlqpy3, nlqpy4, nlqpy5
def sparql_nlq(request):
    
    if(request.GET.get('mybtn')):
        print(request.GET.get('query'))
        results = str(nlqpy_new.search1(request.GET.get('query')))
        print(results)
        #return render(request, 'home.html', {'output': results})
    if(request.GET.get('mybtn2')):
       #print(request.GET.get('query'))
        results = str(nlqpy2.search2(request.GET.get('query')))
        print(results)
    #return render(request, 'home.html', {'output': results})
    if(request.GET.get('mybtn3')):
        print(request.GET.get('query'))
        results = str(nlqpy3.search3(request.GET.get('query')))
        print(results)
    #return render(request, 'home.html', {'output': results})
    if(request.GET.get('mybtn4')):
        print(request.GET.get('query'))
        results = str(nlqpy4.search4(request.GET.get('query')))
        print(results)
    #return render(request, 'home.html', {'output': results})
    if(request.GET.get('mybtn5')):
        print(request.GET.get('query'))
        results = str(nlqpy5.search5(request.GET.get('query')))
        print(results)
    return render(request, 'home.html', {'output': results})
    #return HttpResponse(requst)
    #sparql_result(request)
       # return render(results, "home.html")
#def sparql_result(request):
    #return render(request, "home.html",{'data1':results})