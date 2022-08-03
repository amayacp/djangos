from . import views

from django.urls import path

urlpatterns = [
   #path('',views.load_home_page,name='load_home_page'),
   #path('index',views.index,name='index'),
   path('',views.kerala,name='kerala'),
   path('alappuzha',views.alappuzha,name='alappuzha'),
   path('gavi',views.gavi,name='gavi'),
   path('beypore',views.beypore,name='beypore'),
   path('bekal',views.bekal,name='bekal')

]
