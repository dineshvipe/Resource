from django.db import models
from signup.models import Users
import uuid
# Create your models here.

class dataFramework(models.Model):
    data_id=models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    data_title=models.CharField(max_length=200)
    data_tags=models.CharField(max_length=200)
    data_price=models.CharField(max_length=200)
    data_type=models.CharField(max_length=200)
    data_uploader=models.CharField(max_length=200)
    data_category=models.CharField(max_length=200)
    data_path=models.FileField(upload_to='uploads/')

    def __str__(self):
        return(str(self.data_title))