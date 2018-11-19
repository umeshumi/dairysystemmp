from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = 'dairy'

urlpatterns = [
	path('', views.homePage, name='home'),
	path('milklist/', views.milkList, name='milklist'),
	path('addmilk/', views.addMilk, name='addmilk'),
	path('search/', views.searchFilter, name='search'),
	path('logout/', views.logoutView, name='logout'),
	path('login/',LoginView.as_view(template_name='login.html'), name='login'),
]