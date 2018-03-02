from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView, DeleteView,FormView

from django.shortcuts import HttpResponse

import simplejson as json

import os
from django.core.files.storage import FileSystemStorage

# CRYPTOGRAPHY GOES HERE 

from django.utils.crypto import get_random_string

num=0

#USER IMPORT MODEL GOES HERE


from  signup.models import Users
from search.models import dataFramework



class saveUploadFormData:
    
    def saveUploadFormData(request):

        print("\n\nI'M HERE:\n")

        if(request.POST):
     
            dTitle=request.POST.get('dataTitle')
            dTags=request.POST.get('dataTags')
            dType=request.POST.get('dataType')
            dPrice=request.POST.get('dataPrice')
            dCategory=request.POST.get('dataCategory')
            dFile=request.POST.get('mfile')

            print("\n\n HELLO  {} ".format(dFile))
            #SAVE DATA TO dataFramework

            #userData = dataFramework(data_title=dTitle,data_path=dFile,data_tags=dTags,data_price=dPrice,data_type=dType,data_category=dCategory,data_uploader=request.session['ID'])
        
            if request.FILES['mfile']:
                print("\n\nDINESH\n\n")
                mfile = request.FILES['mfile']
                print("\n\n\nHEll COming {}\n\n".format(mfile))
                fs = FileSystemStorage()
                filename = fs.save(mfile.name, mfile)
                uploaded_file_url = fs.url(filename)

                print("\n\n{} PATH".format(uploaded_file_url))
                userData = dataFramework.objects.create(data_title=dTitle,data_path=uploaded_file_url,data_tags=dTags,data_price=dPrice,data_type=dType,data_category=dCategory,data_uploader=request.session['ID'])
                print("\n\n{}\n\n".format(userData.data_id))
                
                try:
                    print("\n{}".format(request.session['userName']))
                    f=open("Users/"+request.session['userName']+"/uploads.txt","a")
                    print("\n\n YADAV {}\n\n".format(f))
                    f.write(str(userData.data_id)+"\n")
                    f.close()
                    userData.save()
                except:
                    return(HttpResponse("<h2>Something Happend Please Try Again</h2>"))
                #print("\n\n{}\n\n\n".format(userData))
            else:
                return HttpResponse("<center><h1>Error Uploading Files PLease Try again</h1></center>")


        #EXTRACTING DATA ID

        #dID = dataFramework.objects.filter(data_title=dTitle,data_path=dFile,data_tags=dTags,data_price=dPrice,data_type=dType,data_category=dCategory)

        #print("\nprinting fuckin : {} \n".format(dID[0].data_id))
        

        #SAVING ID TO FILE UPLOADS

        #f=open("Users/"+request.session['uName']+"/uploads.txt",'a')
        #f.write("\n"+str(dID[0].data_id))

        #print("\ndata ID : {} \n".format(dID))


            return(render(request,'Profile.html',{'status':'success'}))
        else:
        
            return(render(request,'uploadView.html',{'status':'failure'}))
