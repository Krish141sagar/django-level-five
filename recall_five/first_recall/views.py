from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_recall.models import Teacher
from django.contrib.auth import authenticate,login,logout
from first_recall.forms import Teacher_Form,Portfoiloform,Userform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    return HttpResponse("Hello u are at polls Index")
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_recall:register'))

@login_required
def special(request):
    return HttpResponse("u are logged in, Nice!")

def info(request):
    teacher_data=Teacher.objects.order_by('Name')
    context_data={"Name":teacher_data}
    return render(request,'first_recall\info.html',context=context_data)

def teach_form(request):
    teacher_form=Teacher_Form()
    if request.method=='POST':
        teacher_form= Teacher_Form(request.POST)
        teacher_form.save()
        print("hai")

        if teacher_form.is_valid():
            print("validation success")
            return HttpResponseRedirect("/info/")




    return render(request,"first_recall/teacherform.html",{'teacher_form':teacher_form})

def register(request):
    return render(request,"first_recall/register.html")

def register(request):
    registered=False
    if request.method=="POST":

        user_form=Userform(request.POST)
        profile_form=Portfoiloform(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            # this is for hashing the password
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'Image_link' in request.FILES:
                print("hi")
                profile.Image_link=request.FILES['Image_link']
            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=Userform()
        profile_form=Portfoiloform()

    return render(request,"first_recall/register.html",
                                                     {'user_form':user_form,
                                                     'portfoilo_form':profile_form,
                                                     'registered':registered })

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('info'))

            else:
                return HttpResponse('user not active')
        else:
            print("someone tried to login and failed")
            print("username: {} and passeord {}".format(username,password))
            return HttpResponse("Imvalid login details supplied")
    else:
        return render(request,"first_recall/login.html",{})
