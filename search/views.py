from .models import dataFramework
from django.shortcuts import render

#SERIALIZER
from django.core import serializers
import json
from search.models import dataFramework
from django.contrib.postgres.search import SearchVector
import os
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger 

#SEARCH ALGOTITHM GOES SHERE

def search(request):
    query=request.GET.get("search")
    page=request.GET.get("page",1)

    #SAVING THE QUERY IN HISTORY FILE
    #f=open('Users/'+request.session['uName']+'/history.txt','a')
    #f.write("\n"+str(query))
    
    #ENDS HERE

    drugs = dataFramework.objects.filter(data_title__contains=query)

    pageResults=[]

    #GET THE INDIVIDUAL PAGE IDS

    for drug in drugs:
        pageResults.append(str(drug.data_id))
    

    request.session['pageResults']=pageResults;
    
    #PAGINATION HERE

    paginator=Paginator(drugs,10)

    try:
        drugs=paginator.page(page)
    except PageNotAnInteger:
        drugs=paginator.page(1)
    except EmptyPage:
        drugs=paginator.page(paginator.num_pages)

    return render(request,'search/search.html',{'drug':drugs,'query':query})

def returnWarningPage(request):
    return render(request,'search/Warning.htm')