from django.urls import path 
from . import views

urlpatterns=[

path("",views.index,name="index"),
path("contact/",views.contact,name="contact"),
path("diet_plan/",views.diet_plan,name="diet_plan"),
path("about_us/",views.about_us,name="about_us"),
path("user_registration/",views.user_registration,name="user_registration"),
path("user_login/",views.user_login,name="user_login"),
path("user_home/",views.user_home,name="user_home"),
path("logout/",views.logout,name="logout"),
path("dietitian_registration/",views.dietitian_registration,name="dietitian_registration"),
path("dietitian_login/",views.dietitian_login,name="dietitian_login"),
path("search_dietitian/",views.search_dietitian,name="search_dietitian"),
path("edit_user/",views.edit_user,name="edit_user"),
path("edit_dietitian/",views.edit_dietitian,name="edit_dietitian"),
path("user_feedback/",views.user_feedback,name="user_feedback"),
path("dietitian_home/",views.dietitian_home,name="dietitian_home"),
path("dietitian_post/",views.dietitian_post,name="dietitian_post"),


]