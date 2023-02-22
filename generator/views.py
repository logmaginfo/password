from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):

    thepassword = ""
    uppercase_checked = ""
    numbers_checked = ""
    spec_checked = ""
    visibility = "hidden"
    length_op = "12"

    if request.GET.get('sub'):

        character = list('abcdefghijklmnopqrstuvwxyz')
        visibility = "visible"

        length_op = int(request.GET.get('length'))
        if length_op > 14:
            length_op = 14
        if length_op < 4:
            length_op = 4

        if request.GET.get('uppercase'):
            character += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            uppercase_checked = "checked='checked'"

        if request.GET.get('numbers'):
            character += list('1234567890')
            numbers_checked = "checked='checked'"

        if request.GET.get('special'):
            character += list('!@#$%^&*()_+')
            spec_checked = "checked='checked'"


        for i in range(length_op):
            thepassword += random.choice(character)

    #return render(request,'generator/home.html',{'password':thepassword, 'uppercase_checked':uppercase_checked, 'numbers_checked':numbers_checked, 'special_checked'=special_checked})
    return render(request,'generator/home.html',{
                                                'password':thepassword,
                                                'uppercase_checked':uppercase_checked,
                                                'numbers_checked':numbers_checked,
                                                'spec_checked':spec_checked,
                                                'visibility':visibility,
                                                'length':length_op,
                                                'post':[i for i in range(4,15)]
                                                })

def about_we(request):
    return render(request,'generator/about_we.html')


def password(request):
    thepassword = ""

    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'),12)

    if request.GET.get('uppercase'):
        character += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        character += list('1234567890')

    if request.GET.get('special'):
        character += list('!@#$%^&*()_+')


    for i in range(length):
        thepassword += random.choice(character)

    return render(request,'generator/password.html',{'password':thepassword})
