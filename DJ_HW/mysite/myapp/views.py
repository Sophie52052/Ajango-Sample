from django.shortcuts import render

from myapp.models import KkboxSong, UserlikeRecord
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.

# from datetime import datetime

def index(request):
    

    return render(request, 'myapp/index.html', locals())


def searchlist(request):
    

    return render(request, 'myapp/search.html', locals())    


def addKkboxSong(request):
    if request.method == "POST":        
        A1 = request.POST['A1']
        A2 = request.POST['A2']
        u = KkboxSong.objects.create(song_name=A1,artist=A2,is_deleted="0",kkbox_api_id="0",image="0",url="0",length="0")
        u.save()
        return HttpResponse("success")

def updateKkboxSong(request):
    if request.method == "POST": 
        ID_update = request.POST['ID_update']
        song_update = request.POST['song_update']
        author_update = request.POST['author_update']
        KkboxSong.objects.filter(id=ID_update).update(song_name=song_update,artist=author_update)
        
        return HttpResponse("success")

def deleteKkboxSong(request):
    if request.method == "POST":        
        delete = request.POST['delete']
        deleteinstance = KkboxSong.objects.get(id=delete)
        deleteinstance.delete()
        return HttpResponse("success")

def interactionKkboxSong(request):
    if request.method == "POST":
        ID_interaction = request.POST['ID_interaction']
        U = KkboxSong.objects.filter(id=ID_interaction)
        LineList = []
        for item_id in U:
                Line = UserlikeRecord.objects.filter(item_id=item_id)[0]
                LineList.append(Line.line_id)
        return JsonResponse({'LineList': LineList})





from django.shortcuts import render
from django.db.models import Q

def searchsong(request):
        
        if request.method == "GET":  #POST
                name_search = request.GET['name_search'] #POST
                U = KkboxSong.objects.filter(Q(song_name__icontains=name_search)|Q(artist__icontains=name_search))
                #print(U[0].song_name)
                course_list = []
                for i in range(len(U)): 
                        A=(U[i].song_name)
                        B=(U[i].artist)
                        dict = {}
                        dict['songname'] = A
                        dict['artist'] = B
                        course_list.append(dict)
                # for search in U:
                #         course_list.append(search.song_name)
                        
                #return JsonResponse({"userList": course_list})
                return JsonResponse(course_list,safe=False) 





