from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
import smtplib 
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class UserCreateForm(UserCreationForm):
    class Meta:
       fields =('username','email','password1','password2')
       model = get_user_model()
       
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label="Enter User Name"
        self.fields['email'].label="Enter Email-Id"
        self.fields['password1'].label="Enter Password"
        self.fields['password2'].label="Confirm Password"
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        username=self.cleaned_data['email']
        print(username)
        if password2!=password1:
            raise ValidationError("Your passowrd did not match!! please enter same password")
        
  
        num=random.randint(1024,9999)
        print(num)
        me="deshmukhss3@rknec.edu"
        msg=MIMEMultipart('alternative')
        msg['Subject']="Please Verify your Account!!"
        msg['From']=me
        msg['To']=username

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

        server.sendmail(me,username,msg.as_string())
        f=open("Users/otp.txt","w")
        f.write(str(num)+"\n")
        f.write(str(username))
        f.close()
        return password2,username 
        
