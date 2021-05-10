# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2021 - present darius.tech
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import MainPage,Cause, User, Common, Event, Leader, Testimomial, Statistic
from .forms import SignUpForm, FeedBackForm


def index(request):
    try:
        ome_id = max((obj.id for obj in MainPage.objects.filter(active=True)))
        main = MainPage.objects.get(id =ome_id )
    except Exception as mae:
        main,_ = MainPage.objects.get_or_create(id =1)
        pass
    couses = Cause.objects.order_by('-id')[:3]
    events= Event.objects.order_by('-id')[:3]
    volunteers= Leader.objects.order_by('-id')[:4]
    testimomials= Testimomial.objects.order_by('-id')
    statistics =Statistic.objects.order_by('-id')
    
    common, _ = Common.objects.get_or_create(id=1)
  

    return render(
        request,
        "index.html",
        {'common': common, 'main': main,'couses':couses,'events': events,'volunteers': volunteers,'testimomials': testimomials,'statistics':statistics})

def causes(request):
    common, _ = Common.objects.get_or_create(id=1)
    couses= Cause.objects.order_by('-id')[:10]

    # if len(couses)<1:
    #     mssg ='Causes to be posted soon!'

    # mssg=""   

    return render(request, "causes.html", {'common': common,'couses':couses,}) #'mssg':mssg})

def members(request):
    common, _ = Common.objects.get_or_create(id=1)
    members = User.objects.order_by('-id')[:10]

    return render(request, "members.html", {'common': common,'members':members})


def about(request):
    try:
        ome_id = max((obj.id for obj in MainPage.objects.filter(active=True)))
        main = MainPage.objects.get(id =ome_id )
    except Exception as mae:
        main,_ = MainPage.objects.get_or_create(id =1)
        pass    
    common, _= Common.objects.get_or_create(id=1)
    couses = Cause.objects.order_by('-id')[:3]
    events= Event.objects.order_by('-id')[:3]
    volunteers= Leader.objects.order_by('-id')[:4]
    testimomials= Testimomial.objects.order_by('-id')
    statistics =Statistic.objects.order_by('-id')
    common, _ = Common.objects.get_or_create(id=1)
    return render(request, "about.html",{'common': common,'main': main,'couses':couses,'events': events,'volunteers': volunteers,'testimomials': testimomials,'statistics':statistics})

def events(request):
    common, _= Common.objects.get_or_create(id=1)
    events= Event.objects.order_by('-id')[:10]
    return render(request, "events.html",{'common': common,'events': events,})

def blogs(request):
    common, _= Common.objects.get_or_create(id=1)
    return render(request, "blog.html",{'common': common,})


# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template = request.path.split('/')[-1]
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( 'error-404.html' )
#         return HttpResponse(html_template.render(context, request))

#     except:
    
#         html_template = loader.get_template( 'error-500.html' )
#         return HttpResponse(html_template.render(context, request))    


def join_us(request):
    common, _= Common.objects.get_or_create(id=1)
    if request.method == 'POST':
        data = {}
        data['username'] = request.POST.get('username')
        data['first_name'] = request.POST.get('first_name')
        data['last_name'] = request.POST.get("last_name")
        data['phone_number'] = request.POST.get("phone_number")
        data['email'] = request.POST.get("email")
        data['member_type'] = request.POST.get("member_type")
        data['password1'] = 'qqqqq11111'
        data['password2'] = 'qqqqq11111'

        form = SignUpForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/members')
    else:
        form = SignUpForm()     

    return render(request, 'join_us.html', {'form': form, 'common': common, })




# def join_us(request):
#     common, _= Common.objects.get_or_create(id=1)
#     if request.method == 'POST':

#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('/members')
#         else:
#             print(form.errors)    
#     else:
#         form = SignUpForm()
#     return render(request, 'join_us.html', {'form': form, 'common': common, })        


def contact(request):
    common, _  = Common.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    else:
        form = FeedBackForm()
    return render(request, 'contact.html', {'common': common, 'form': form})        
