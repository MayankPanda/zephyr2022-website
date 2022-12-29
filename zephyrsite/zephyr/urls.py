from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testlayout', views.home_view,),#Nothing
    path('register', views.message_test,),#reg form
    path('testh', views.home_test,),#Nothing
    path('incentives', views.inc_test,),#incentives
    path('responsibilities', views.resp_test,),#responsibility
    path('home', views.layout_test,),#home
    path('testphonehome', views.phone_home_test,),
    path('testhamburger',views.hamburger),#Phone incentives page
    path('success',views.reg_success),#success page
    path('about',views.about),#about page
]