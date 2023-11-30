from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('index2/', views.Index2.as_view(), name='index2'),
    
    path('register/', views.CreateSchedule.as_view(), name='register'),
    
    path('done/', views.Done.as_view(), name='done'),

    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),

    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),

    path('contact/', views.Contact.as_view(), name='contact'),
    
    
]
