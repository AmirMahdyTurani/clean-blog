from django.urls import path
from . import views

# app_name = "web"

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.all_posts, name="posts"),
    path('posts/<slug:slug>', views.post_detail, name="post-detail"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('about-us/', views.about_us, name="about-us"),
]
