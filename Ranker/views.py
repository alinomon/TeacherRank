from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Rating, Professor, Module
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

@csrf_exempt
def HandleRegisterRequest (request): #request, poll_username, poll_email, poll_password
    poll_username = request.GET["username"]
    poll_email = request.GET["email"]
    poll_password = request.GET["password"]

    switch = 0
    if User.objects.filter(email=poll_email).exists():
        return HttpResponse(switch)
    else:
        new_user = User.objects.create_user(poll_username, poll_email, poll_password)
        new_user.save()
        switch = 1
    

    return HttpResponse(switch)

#POST Function that searches User model and authenticates
@csrf_exempt
def HandleLoginRequest(request):
    switch = 2

    poll_username = request.GET["username"]
    poll_password = request.GET["password"]
    
    user = authenticate(request, username=poll_username, password=poll_password)
    if user is not None:
        login(request, user)
        return HttpResponse(switch)
    else:
        switch = 3
        return HttpResponse(switch)

def HandleListRequest(request):
    output = []
    module_list = Module.objects.all()

    
    for x in module_list:
        output.append(x.listview())

        for i in x.professors.all().values():
            id = i['professor_id']
            name = i['name']
            output.append(id)
            output.append(", ")
            output.append(name)
            output.append(" | ")

        output.append("\n\n")

    return HttpResponse(output)

def HandleViewRequest(request):
    professors = Professor.objects.all()
    output = []

    for i in professors:
        rating = 0
        count = 0
        for j in i.rating.all():
            if j.rating != 0:
                rating += j.rating
                count += 1
        if count == 0:
            count += 1
        final_rating_number = round(rating/count)
        if final_rating_number == 0:
            final_rating = "-"
        elif final_rating_number == 1:
            final_rating = "*"
        elif final_rating_number == 2:
            final_rating = "**"
        elif final_rating_number == 3:
            final_rating = "***"
        elif final_rating_number == 4:
            final_rating = "****"
        else:
            final_rating = "*****"

        output.append("The rating of Professor %s (%s) is %s\n" % (i.name, i.professor_id, final_rating))
    

    return HttpResponse(output)

@csrf_exempt
def HandleRateRequest(request):
    poll_profid = request.GET["professor_id"]
    poll_modcode = request.GET["module_code"]
    poll_year = request.GET["year"]
    poll_sem = request.GET["semester"]
    poll_rating = request.GET["rating"]

    the_professor = Professor.objects.get(professor_id = poll_profid)

    the_class = Module.objects.get(module_code=poll_modcode, semester=poll_sem, year=poll_year)

    #Checks if the teacher is in the class, if not dont rate
    taught_by = the_class.professors.all()
    for x in taught_by:
        if x.professor_id == poll_profid:
            new_rating = Rating(class_id = poll_modcode, professor_id = poll_profid, rating=poll_rating, year=poll_year, semester=poll_sem)
            new_rating.save()
            the_professor.rating.add(new_rating)
            return HttpResponse("**Rating Added!**\n")

    return HttpResponse("That professor does not teach this class")

def HandleAverageRequest(request):
    poll_profid = request.GET["professor_id"]
    poll_modcode = request.GET["module_code"]

    professor = Professor.objects.get(professor_id=poll_profid)
    mod = Module.objects.filter(module_code=poll_modcode)
    module = mod.first()
    output = []

    ratings = professor.rating.all()
    final_rating_temp = 0
    count = 0

    for i in ratings:
        if i.professor_id == poll_profid and i.class_id == poll_modcode:
            count += 1
            final_rating_temp += i.rating


    if count == 0:
        count += 1

    final_rating_number = round(final_rating_temp/count)
    if final_rating_number == 0:
        final_rating = "-"
    elif final_rating_number == 1:
        final_rating = "*"
    elif final_rating_number == 2:
        final_rating = "**"
    elif final_rating_number == 3:
        final_rating = "***"
    elif final_rating_number == 4:
        final_rating = "****"
    else:
        final_rating = "*****"
        

    output.append("The rating of Professor %s (%s) in module %s (%s) is %s\n" % (professor.name, professor.professor_id, module.name, poll_modcode, final_rating))
    

    return HttpResponse(output)
"""
def login():


def logout(request):
    return 'Temp Return'

def view():
    return 'Temp return'    

def average(poll_profid, poll_modulecode):
    return 'Temp return'

def rate(poll_profid, poll_modulecode, poll_year, poll_sem, poll_rating):
    return 'Temp return'

"""