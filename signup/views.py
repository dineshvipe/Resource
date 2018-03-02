from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView, DeleteView,FormView

from django.shortcuts import HttpResponse

import simplejson as json
import uuid

from . import forms
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# CRYPTOGRAPHY GOES HERE 

from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model

#USER IMPORT MODEL GOES HERE

from  signup.models import Users
from search.models import dataFramework

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    a=form_class.clean_password2
    print(a)
    
    success_url='/signup/verify/'
    template_name='signup/signup.html'
    
def see(request):
    return render(request,'signup/login.html')

# Create your views here.
def look(request):
    return render(request,'signup/firstpage.html')

def verifyPage(request):
          
    '''import smtplib 
    import random

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
  
    num=random.randint(1024,9999)
    request.session['otp']=num
    print(num,'PAGERANK')
    #EMAIL CONTAINERS

    me="deshmukhss3@rknec.edu"

    #EMAIL CODE GOES HERE
    userEmail=request.POST.get('username')
    print(request.POST.get("username"))
    print(userEmail)
    
    #SESSIONS HERE

    request.session['userEmail']=userEmail
    request.session['username']=request.POST.get('username')
    request.session['userPass']=request.POST.get('password1')

    msg=MIMEMultipart('alternative')
    msg['Subject']="Please Verify your Account!!"
    msg['From']=me
    msg['To']=userEmail

    #CREATE HTML BODY HERE

    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """
            <html>
            <head></head>
            <body>
                <div style="background-color:whitesmoke;padding:10px;box-shadow:1px 2px 3px grey;color:black;">
                <h1>Hi!</h1><br>
                <h3>Please Verify your Account by entering the OTP Code</h3><br>
                <h5>Your Code is : {}</h5>
                </div>
            </body>
            </html>
            """.format(num)

    part1=MIMEText(text,'plain')
    part2=MIMEText(html,'html')


    msg.attach(part1)
    msg.attach(part2)
      
    #NUMBER GENERATOR GOES HERE
       

    server=smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()
    server.starttls()

    server.login("deshmukhss3@rknec.edu","iamrajan")

    #msg="WE ARE GREAT!!! DESHMUKH IS POLYY "+str(num);

    print("\nHello World\n")
    server.sendmail(me,userEmail,msg.as_string())


    #ENDS HERE

    '''
    return render(request,'signup/Verify.html')

def verifyOtp(request):
    #print(request.session['otp'],'dinesh')

    if(request.GET):
        otp=request.GET.get('verifyInput')
        print(otp,type(otp))
        try:
            f=open("Users/otp.txt","r")
            s=f.readline()
            print(s)
            s=s.strip()
            username=f.readline()
            username=username.strip()
            f.close()
        except Exception:
            pass
        print(s,type(s))
        if(s==otp):
            #CREATE USER DATA SESSIONS HERE

            #SAVE USER HERE
            user=Users.objects.get(email=username)
            print("\n\n{}\n\n".format(user))
            user.active=True 
            user.save()
            
            #USER DIRECTORY GOES HERE
            
            #INDIVIDUAL DIRETORIES

            try:
                if(os.mkdir('Users/'+username)):
                    open('Users/'+username+'/uploads.txt','a')
                    open('Users/'+username+'/recommend.txt','w')
                else:
                    open('Users/'+username+'/uploads.txt','a')
                    open('Users/'+username+'/recommend.txt','w')

            except:
                return HttpResponse("<h1>We couldn't complete the action </h1>")

            #CREATE A FILE FOR USER HERE
            return(render(request,'ThankYou.html'))
            c={}
        else:
            return(render(request,'signup/Verify.html',{'error':'OTP did not match'}))
    return(render(request,'signup/Verify.html'))

def loginUser(request):

    userName=request.POST.get('username')
    userPass=request.POST.get('password')

    print(userName,'USERNAME')
    print(userPass,'PaSSWORD')

    #CHECK IS USER EXISTS OR NOT
    
    user=authenticate(request,username=userName,password=userPass)
    print(user)
    if user is not None:
        print("\n\n",authenticate(request,username=userName,password=userPass),"\n\n")
        
        #print("USER ID : {} ".format(str(user[0].userID)))

        #SAVE THE SESSION ID

        login(request,user)
        request.session['ID']=str(user.pk)
        request.session['userName']=userName
        s=[]
        #try:
        f=open("Users/"+request.session['userName']+"/recommend.txt")
        l=len(f.readlines())
        f.seek(0,0)
        for i in range(l):
                st=uuid.UUID(f.readline().strip())
                u=dataFramework.objects.get(data_id=st)
                s.append(u)
        print(s)
        #except Exception:
         #   pass
        
        return(render(request,'Profile.html',{'rlist':s,'userName':userName}))
    else:
        print('User NOT Exists!!')
        return(render(request,'Sorry.html'))

def get_drugs(request):
    if request.is_ajax():
        q = request.GET.get('term')
        print(q,'SEARCH QUERY')
        drugs = dataFramework.objects.filter(data_title__istartswith = q )[:8]
        print("\n {} \n".format(drugs),)
        results = []
        drug_json = {}
        for i in drugs:
            #drug_json['id'] = drug.rxcui
            drug_json[i] = i.data_title
            #drug_json['value'] = drug.data_title
            results.append(drug_json[i])
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

#LOAD PROFILE FUNCTION GOES HERE 
@login_required(login_url='signup:login')
def loadUserProfile(request):

    return(render(request,'uploadview.html'))
@login_required(login_url='signup:login')
def Profile(request):
        s=[]
        #try:
        f=open("Users/"+request.session['userName']+"/recommend.txt")
        l=len(f.readlines())
        f.seek(0,0)
        for i in range(l):
                st=uuid.UUID(f.readline().strip())
                u=dataFramework.objects.get(data_id=st)
                s.append(u)
        print(s)
        #except Exception:
         #   pass

        
        return(render(request,'Profile.html',{'rlist':s,'userName':request.session['userName']}))

#FUNCTION FOR THE saving Form Data




# CUSTOMIZED USER MODEL IS HERE

# INDEX VIEW GOES HERE


#SESSION FOR LOGIN

'''def login(request, user):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """
    session_auth_hash = ''
    if user is None:
        user = request.user
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()

    if SESSION_KEY in request.session:
        if _get_user_session_key(request) != user.data_id or (
                session_auth_hash and
                request.session.get(HASH_SESSION_KEY) != session_auth_hash):
            # To avoid reusing another user's session, create a new, empty
            # session if the existing session corresponds to a different
            # authenticated user.
            request.session.flush()
    else:
        request.session.cycle_key()
    request.session[SESSION_KEY] = user.data_id.value_to_string(user)
    request.session[BACKEND_SESSION_KEY] = user.backend
    request.session[HASH_SESSION_KEY] = session_auth_hash
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
    user_logged_in.send(sender=user.__class__, request=request, user=user)


'''


'''
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'user_list'
    template_name = 'modelForms/index.html'
 
    def get_queryset(self):
        return Users.objects.all()
 
# view for the product entry page
class UserEntry(CreateView):
    model = Users
    # the fields mentioned below become the entry rows in the generated form
    fields = ['userName', 'userPass', 'userEmail']
 
# view for the product update page
class UserUpdate(UpdateView):
    model = Users
    # the fields mentioned below become the entyr rows in the update form
    fields = ['userName', 'userPass', 'userEmail']
 
# view for deleting a product entry
class UserDelete(DeleteView):
    model = Users
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('modelforms:index')    


'''
