from django.shortcuts import render
import requests
import logging

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'message': "It works"}
    return render(request, 'myclasses/base.html', context)




def fetch_classrooms(username, password):
    
    URL = 'https://app.learncube.com/api/virtual-classroom/classrooms/'
    
      
    res = requests.get(URL, auth=(username, password))
    
    return res.json()

def get_classrooms(request):
    username = "omobolajianuoluwapoyahoocom" 
    password = "2517729HHRpqMsAy3" 
    res = fetch_classrooms(username, password)
    
    results = res['results']
    res_data = []
    for dt in results:
        data = {
            "uuid": dt['uuid'],
            "names": dt['teacher_first_name'] + " " + dt['teacher_last_name'],
            
        }
        res_data.append(data)
    # print(res_data)
    context = {
        "classrooms": res_data,
        "count": res['count']
    }
    
    return render(request, 'myclasses/data_room.html', context)        



    