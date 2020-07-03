from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app import views
from app.views import Home, CreateOrder, Profit, Error
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profit-and-loss/', Profit.as_view(template_name='app/profit-and-loss.html'), name='profit-loss'),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', Home.as_view(template_name='app/home.html'), name='app-home'),
    path('create-order/', CreateOrder.as_view(template_name='app/new_order.html'), name='app-create'),
    path('error/', views.Error),
]
