from django.db import models

# Create your models here.
class Facinfo(models.Model):      #클래스 앞글자는 대문자로 명칭하여야 한다
    fCode = models.IntegerField()
    fName = models.CharField(max_length=50)
    fModel = models.CharField(max_length=50)
    fDesc = models.CharField(max_length=250)
    # tPublish = models.DateTimeField() #시간 추가 항목

    
    def __str__(self):
        return self.fName  #사이트에 Facinfo 의 표시할 내용
