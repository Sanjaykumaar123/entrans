from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo.views import home, signup_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('api/', include('todo.urls')),

    # LOGIN
    path('accounts/login/', 
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),

    # SIGNUP
    path('accounts/signup/', signup_view, name='signup'),

    # LOGOUT
    path('accounts/logout/', logout_view, name='logout'),

    # Include Django auth URLs (password reset etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]
