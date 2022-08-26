from django.urls import path
from blog.views import home, post_detay

urlpatterns = [
    path('', home, name='blog_list'),
    path('<post_link>/', post_detay, name='blog_detay'),
    
    # path('about/', views.about, name="about"),
]