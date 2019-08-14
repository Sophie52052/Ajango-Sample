from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import User, UserInfo
from django.http import JsonResponse
# Create your views here.


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

#import
from datetime import datetime
def index(request):
    name = "Pika~"
    current_time = str(datetime.now())
    return render(request, 'myapp/index.html', locals())

def tag_page(request):
    animals = ['cat', 'dog', 'pikachu']
    return render(request, 'myapp/tag.html', locals())




def createUser(request):
    u = User.objects.create(name="Lisa")
    u.save()
    ui = UserInfo.objects.create(user_id=u, age=23)
    ui.save()
    return JsonResponse({"state":"success"})

def getUser(request):
    #U = User.objects.all()
    nameList = []
    U = User.objects.filter(name="lisa")
    for user in U:
        nameList.append(user.name)
    return JsonResponse({"userList": nameList})

def getAge(request):
    # only find the name is lisa
    U = User.objects.filter(name='lisa')
    print(U)
    ageList = []
    for user in U:
        print(user.name)
        age = UserInfo.objects.filter(user_id=user)[0]
        print(age.age)
        ageList.append(age.age)
    return JsonResponse({'"ageList"': ageList})