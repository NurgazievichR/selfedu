from selfApp.views import *
from django.urls import path

urlpatterns = [
    path('', ActorHome.as_view() , name='homepage'),
    path('about/', about, name='about' ),
    path('addpage/', AddPage.as_view(), name='addpage' ),
    path('contact/', contact, name='contact' ),
    path('login/', login, name='login' ),
    path('post/<slug:post_slug>/', show_post, name='post' ),
    path('category/<slug:urlpost_slug>/', ActorCategory.as_view(), name='category'),
]