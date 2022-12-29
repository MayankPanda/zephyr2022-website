from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home_view,),
    path('message', views.message_test,),
    path('testh', views.home_test,),
    path('testinc', views.inc_test,),
    path('testresp', views.resp_test,),
    path('testlayout', views.layout_test,),
    path('testphonehome', views.phone_home_test,),
    path('testhamburger',views.hamburger),
    path('success',views.reg_success),
    path('about',views.about),
]