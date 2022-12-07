from django.shortcuts import render
from django.http import HttpResponse #HttpResponse = STR을 http로 날려주는 역활
# from .models import Ff
def sub(ss):
# 	# s = Ff.object.get(f1-10001) #데이터베이스 에서 모델로 만든후 웹페이지에 불러온다
	return HttpResponse("<h1>Hello World!!!</>"
	"<h2>Hello World!!!</>"
    # "<img src ='https://user-images.githubusercontent.com/110071838/203696366-e7f0ff25-b478-4ede-9cb2-1299c173edee.jpg'>"
    )
# 	"<h3>Hello World!!!</>"
# 	"<h4>Hello World!!!</>"
# 	"<h5>Hello World!!!</>"
# 	"<h6>Hello World!!!</>"

def Home(s1):
    # return HttpResponse("<img src ='https://user-images.githubusercontent.com/110071838/203696366-e7f0ff25-b478-4ede-9cb2-1299c173edee.jpg'>")
    return HttpResponse()
# Create your views here.
    
    #return render(s1, 'templates,home.html',{'a':'123' 'b':'456'}) #html 경로 설정
    #render 페이지를 돌려주는 함수