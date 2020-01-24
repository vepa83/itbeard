from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.mainview, name="home"),
    path('about/', views.aboutview, name="about"),
    path('contact/', views.contactview, name="contact"),
    path('searchresult/', views.searchview, name="searchresult"),
    path('comments/', views.commentview, name="comments"),
    path('<slug>/', views.categoryview, name="category"),
    path('comments/leave_comment/', views.leave_commentview, name="leave_comment"),
]