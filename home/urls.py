from django.urls import path, include
from .views import *

urlpatterns = [
   path('', home, name='home'),
   path('login/', login_view, name='login_view'),
   path('signin/', register_view, name='register_view'),
   path('add-blog/',add_blog_view, name='add_blog'),
   path('blog-details/<slug>', blog_details, name='blog_details'),
   path('see-blog/', see_blogs, name='see_blogs'),
   path('blog-delete/<id>', blog_delete, name='blog_delete'),
   path('blog-update/<slug>', blog_update, name='blog_update'),
   path('logout_view/', logout_view, name='logout_view'),
   path('verify/<token>', verify, name='verify')
    
]