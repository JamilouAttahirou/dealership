from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('inventory/', views.inventory, name="inventory"),
    path('car/<int:car_id>/', views.car, name="car"),

    
    path('financing/', views.financing_room, name="financing"),
    path('all_financing_applications/', views.all_financing_applications, name="all_financing_applications"),
    path('financing_application/<str:pk>/', views.financing_application, name="financing_application"),

    path('contact/', views.contact, name="contact"),
    path('all_messages/', views.all_messages, name="all_messages"),
    path('message/<int:pk>/', views.message, name="message"),

    path('service/', views.service, name="service"),
    path('aboutus/', views.aboutUs, name="aboutus"),
    path('directions/', views.direction, name="direction"),
    path('info/', views.info, name="info"),
    path('store_hours/', views.store_hours, name="store_hours"),
    
    path('create-car-room/', views.createCarRoom, name="create-car-room"),
    path('update-car-room/<int:car_id>/', views.updateCarRoom, name="update-car-room"),
    path('delete-car-room/<int:car_id>/', views.deleteCarRoom, name="delete-car-room"),
]