from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from collections import namedtuple
from django.shortcuts import Http404
from search.models import dataFramework

@login_required(login_url="signup:login")
def recommendPages(request):
    userQuery=request.GET.get('data')
    userUploader=request.GET.get('uploader')

    #RECOMMENDATION ALGORITHM STARTS HERE

    #GET THE CURRENT DATA TAGS

    currentTags=dataFramework.objects.get(data_id=userQuery)

    currentTitle=currentTags.data_title
    currentCategory=currentTags.data_category

    print("CURRENT DATA TAGS: ",currentTags.data_tags)

    #SPlit THE TAGS
    s=currentTags.data_tags.split(',')

    #GET THE PAGE RESULTS

    #returnedResults=request.session['pageResults']

    #EXCLUDE THE CLICKED QUERY
    #returnedResults.remove(str(userQuery))
    #BLANK DICT INITIALIZATION
    myRecommendations={}
    rlist=[]

    #FIND IN EVERY RESULT
    li=dataFramework.objects.all()
    for l in li:
        objdTag=l.data_tags.split(',')
        count=0
        for i in (objdTag):
            if(i in s):
                count+=1
        
        
        
        if(count>=1):
            rlist.append(l)
            myRecommendations[str(l.data_id)]=count
    print(rlist)
    try:
        f=open("Users/"+request.session['userName']+"/recommend.txt","w")
    except Exception:
        raise ValueError("we couldnot complete the action")
    for i in rlist:
        try:
            f.write(str(i.data_id)+"\n")
        except Exception:
           raise Http404
    f.close
    print(myRecommendations)
    print(s) 

    '''for result in returnedResults:
        pageHits=0
        dataTags=dataFramework.objects.get(data_id=result)
        for tag in currentTags.data_tags.split(","):
            for dataTag in dataTags.data_tags.split(","):
                if(tag==dataTag):
                    pageHits+=1
        #CHECK IF HITS ARE > 0
        if pageHits>0:
            myRecommendations[dataFramework.objects.get(data_id=result).data_title]=pageHits
    
    print("PRINTING DICT")
    '''
    # FINAL RECOMMENDATION ARRAY
    for key in myRecommendations:
        print(key,myRecommendations[key])

    #MAKE SESSION KEY MYRECOMMENDATION HERE
    #request.session['Recommended']=myRecommendations
    #request.session['rlist']=rlist

    return render(request,'Profile.html',{'rlist':rlist})       
