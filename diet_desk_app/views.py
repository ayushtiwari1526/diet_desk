from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import User,Dietitian,Feedback,Dietitian_post,Contact
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

def index(request):

    feedbacks = Feedback.objects.all().order_by('-id')[:5]
    return render(request,"diet_desk_app/html/index.html", {"feedbacks": feedbacks})


def user_registration(request):
    if request.method=="GET":
        return render(request,"diet_desk_app/user/user_registration.html")
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        city=request.POST["city"]
        phone=request.POST["phone"]
        profile_pic=request.FILES["profile_pic"]
        user_obj=User(name=name,email=email,password=password,city=city,phone=phone,profile_pic=profile_pic)
        user_obj.save()
        messages.success(request,"User Registered SuccessFull , Kindly Login ")
        return redirect("user_login")

def user_login(request):
    if request.method=="GET":
        return render(request,"diet_desk_app/user/user_login.html")
    
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user_obj=User.objects.filter(email=email , password=password)
        if len(user_obj)>0 :
            request.session["email"]=email
            return redirect("user_home")
        else:
            messages.error(request,"Credentian didnot match")
            return render(request,"diet_desk_app/user/user_login.html")


def logout(request):
    ##request.session.delete()
    request.session.flush()
    return redirect("index")
        
@never_cache
def user_home(request):
    if "email" in request.session:
        email=request.session.get("email")
        user_obj=User.objects.filter(email=email)[0]
        post_obj=Dietitian_post.objects.all().order_by('-id')[:5]

        return render(request,"diet_desk_app/user/user_home.html",{"post":post_obj,"user":user_obj})
    
    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/user/user_login.html")
    
def dietitian_registration(request):
    if request.method=="GET":
        return render(request,"diet_desk_app/dietitian/dietitian_registration.html")
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        name=request.POST["name"]
        phone=request.POST["phone"]
        qualification=request.POST["qualification"]
        gender=request.POST["gender"]
        experience=request.POST["experience"]
        skills=request.POST["skills"]
        city=request.POST["city"]
        registration_no=request.POST["registration_no"]
        profile_pic=request.FILES["profile_pic"]

        dietitian_obj=Dietitian(email=email,password=password,name=name,phone=phone,qualification=qualification,gender=gender,experience=experience,skills=skills,city=city,registration_no=registration_no,profile_pic=profile_pic)
        dietitian_obj.save()
        messages.success(request,"Registered .... Plz logIn ")
        return redirect("dietitian_login")

def dietitian_login(request):
    if request.method=="GET":
        return render(request,"diet_desk_app/dietitian/dietitian_login.html")
    
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        dietitian_obj=Dietitian.objects.filter(email=email , password=password)
        if len(dietitian_obj)>0 :
            request.session["email"]=email
            return redirect("dietitian_home")
        else:
            messages.error(request,"Credentian didnot match")
            return render(request,"diet_desk_app/dietitian/dietitian_login.html")


def contact(request):
    if request.method=="GET":
        return render(request,"diet_desk_app/html/contact.html")
    
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        role=request.POST["role"]
        message=request.POST["message"]
        contact_obj=Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,role=role,message=message)
        contact_obj.save()
        messages.success(request,"Thanks To contact us ")
        return redirect("contact")
        

def diet_plan(request):
    return render(request,"diet_desk_app/html/diet_plan.html")

def about_us(request):
    return render(request,"diet_desk_app/html/about_us.html")

@never_cache
def search_dietitian(request):
    if  "email" in request.session :
        email=request.session.get("email")
        user_obj=User.objects.filter(email=email)[0]
        if request.method=="GET":
            return render(request,"diet_desk_app/user/search_dietitian.html",{"user":user_obj})
        if request.method=="POST":
            city=request.POST["city"]
            city=city.capitalize()
            dietitian_obj=Dietitian.objects.filter(city=city)
            if len(dietitian_obj)>0:
                return render(request,"diet_desk_app/user/search_dietitian.html",{"d":dietitian_obj,"user":user_obj})
            else:
                messages.error(request,"No Dietitian Available in this City")
                return redirect("search_dietitian")
            
    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/user/user_login.html")

@never_cache  
def edit_user(request):
    if "email" in request.session:
        email=request.session.get("email")
        user_obj=User.objects.filter(email=email)[0]
        if request.method=="GET":
             
            return render(request,"diet_desk_app/user/edit_user.html",{"user":user_obj})
        if request.method=="POST":
            name=request.POST["name"]
            phone=request.POST["phone"]
            city=request.POST["city"]
            if "profile_pic" in request.FILES:
                user_obj.profile_pic = request.FILES["profile_pic"]
            
            user_obj.name=name
            user_obj.phone=phone
            user_obj.city=city
            user_obj.save()
            return redirect("edit_user")
          
    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/user/user_login.html")

@never_cache  
def user_feedback(request):
    if "email" in request.session:
        email=request.session.get("email")
        user_obj=User.objects.filter(email=email)[0]
        if request.method=="GET":
            return render(request,"diet_desk_app/user/user_feedback.html",{"user":user_obj})
        
        if request.method=="POST":
            name=user_obj.name
            subject=request.POST["subject"]
            rating=request.POST["rating"]
            feedback=request.POST["feedback"]

            feedback_obj=Feedback(name=name,email=email,rating=rating,feedback=feedback,subject=subject)
            feedback_obj.save()
            messages.success(request,"Feedback submited")
            return redirect("user_feedback")

    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/user/user_login.html") 
    
@never_cache
def dietitian_home(request):
    if "email" in request.session:
        email=request.session.get("email")
        dietitian=Dietitian.objects.filter(email=email)[0]
        return render(request,"diet_desk_app/dietitian/dietitian_home.html",{"dietitian":dietitian})
    
    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/dietitian/dietitian_login.html") 

@never_cache   
def dietitian_post(request):
    if "email" in request.session:
        email=request.session.get("email")
        dietitian_obj=Dietitian.objects.filter(email=email)[0]
        if request.method=="GET":
            return render(request,"diet_desk_app/dietitian/dietitian_post.html",{"dietitian":dietitian_obj})
        if request.method=="POST":
            post=request.POST["post"]
            name=dietitian_obj.name
            post_obj=Dietitian_post(name=name,email=email,post=post)
            post_obj.save()
            messages.success(request,"Posted Successfully")
            return redirect("dietitian_post")

    else:
        messages.error(request,"Login Required")
        return render(request,"diet_desk_app/dietitian/dietitian_login.html") 
    
@never_cache
def edit_dietitian(request):
    if "email" in request.session:
        email=request.session.get("email")
        dietitian_obj=Dietitian.objects.filter(email=email)[0]
        if request.method=="GET":
            dietitian={
                "dietitian":dietitian_obj
            }
            return render(request,"diet_desk_app/dietitian/edit_dietitian.html",dietitian)
        
        if request.method=="POST":
            
            dietitian_obj.name = request.POST["name"]
            dietitian_obj.phone = request.POST["phone"]
            dietitian_obj.qualification = request.POST["qualification"]
            dietitian_obj.experience = request.POST["experience"]
            dietitian_obj.skills = request.POST["skills"]
            dietitian_obj.city = request.POST["city"]
            dietitian_obj.registration_no = request.POST["registration_no"]
            if "profile_pic" in request.FILES:
                dietitian_obj.profile_pic = request.FILES["profile_pic"]

            dietitian_obj.save()
            return redirect("edit_dietitian")


         







 


    
        





    

