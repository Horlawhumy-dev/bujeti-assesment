from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import logging
from .forms import LoginForm, ClassCreateForm, UpdateClassForm


user_credentials = {
    "username": "omobolajianuoluwapoyahoocom",
    "password": "2517729HHRpqMsAy3"
}


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'message': "It works"}
    return render(request, 'myclasses/base.html', context)

def fetch_classroom(uuid, username, password):
    URL = f"https://app.learncube.com/api/virtual-classroom/classrooms/{uuid}/"
    
    res = requests.get(URL, auth=(username, password))
    
    return res.json()


def fetch_classrooms(username, password):
    
    URL = 'https://app.learncube.com/api/virtual-classroom/classrooms/'
    
      
    res = requests.get(URL, auth=(username, password))
    
    return res.json()

def del_classroom(uuid, username, password):
    URL = f"https://app.learncube.com/api/virtual-classroom/classrooms/{uuid}/"
    
    res = requests.delete(URL, auth=(username, password))
    
    return res.json()

def update_class(data, username, password):
    
    URL = f"https://app.learncube.com/api/virtual-classroom/classrooms/{data['uuid']}/"
    
    payload = {**data}
    res = requests.put(URL, json=payload, auth=(username, password))
    
    return res.json()

def create_class(data, username, password):
    URL = f"https://app.learncube.com/api/virtual-classroom/classrooms/"
    payload = {
        "room_token": data['room_token'],
        "max_participants": data['max_participants'],
        "record_class": data['record_class'],
        "description": data['description'],
        "start": data['start'],
        "end": data['end']
        }
    
    res = requests.post(URL, json=payload, auth=(username, password))
    
    return res.json()

def get_classrooms():
 
    res = fetch_classrooms(user_credentials['username'], user_credentials['password'])
    
    results = res['results']
    res_data = []
    for dt in results:
        data = {
            "uuid": dt['uuid'],
            "names": dt['teacher_first_name'] + " " + dt['teacher_last_name'],
            
        }
        res_data.append(data)
    return res_data


def login_teacher(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            res = fetch_classrooms(data['username'], data['password'])
            res_data = get_classrooms()
            context = {
                "classrooms": res_data,
                "count": res['count']
            }
    
            return render(request, 'myclasses/data_room.html', context)
    
    return render(request, 'myclasses/login_teacher.html', {"form": form})





def get_classroom(request, pk):
    
    res = fetch_classroom(pk, user_credentials['username'], user_credentials['password'])
    
    context = {
        "classroom": res 
    }

    return render(request, 'myclasses/classroom.html', context)
    

def delete_classroom(request, pk):
    
    del_classroom(pk, user_credentials['username'], user_credentials['password'])
    return redirect('/login_teacher')
    
def create_classroom(request):
     
    form = ClassCreateForm()
    if request.method == "POST":
        form = ClassCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_class(data, username=user_credentials['username'], password=user_credentials['password'])
            return redirect('/login_teacher')
        
    return render(request, "myclasses/create_classroom.html", {"form": form})


    
def update_classroom(request, pk):
    res = fetch_classroom(pk, user_credentials['username'], user_credentials['password'])
    form = UpdateClassForm(data={**res})
    
    if request.method == "POST":
        form = UpdateClassForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            update_class(data, username=user_credentials['username'], password=user_credentials['password'])
            form = UpdateClassForm()
            return redirect('/login_teacher')
            
    
    return render(request, "myclasses/update_classroom.html", {"form": form, "uuid": res['uuid']})
    
    