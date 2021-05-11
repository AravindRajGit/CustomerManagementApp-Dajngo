from django.urls import path,include
from .import views 

urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.LoginPage,name="Login"),
    path('home/',views.Home,name="home"),
    path('products/',views.Products,name="products"),
    path('userpage/',views.userpage,name="userpage"),
    path('userprofile/',views.customersettings,name="userprofile"),
    path('customer/<str:pk>',views.Customers,name="customers"),
    path('create_order/',views.CreateOrder,name="create_order"),
    path('update_order/<str:pk>/',views.UpdateOrder,name="update_order"),
    path('delete_order/<str:pk>/',views.DeleteOrder,name="delete_order"),
    path('logout/',views.LogOutUser,name="logout"),
]

