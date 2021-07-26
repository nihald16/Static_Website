from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index2',views.index2,name="index2"),
    path('about',views.about,name="about"),
    path('menu',views.menu,name="menu"),
    path('blogdetail',views.blogdetail,name="blogdetail"),
    path('blogs',views.blogstandard,name="blogs"),
    path('contact',views.contacts,name="contact"),
    path('gallery',views.gallery,name="gallery"),
    path('faq',views.faq,name="faq"),
    path('resdetail',views.rest_detail,name="resdetail"),
    path('restaurent',views.restaurent,name="restaurent"),
    path('team',views.team,name='team')
    
    
    
]
