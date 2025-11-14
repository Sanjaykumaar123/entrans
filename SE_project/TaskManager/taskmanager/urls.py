from django.contrib import admin
from django.urls import path, include
from todo.views import home, signup_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('api/', include('todo.urls')),

    # Custom Login + Signup
    path('accounts/login/', 
         include('django.contrib.auth.urls')),
    path('accounts/signup/', signup_view, name='signup'),

    # Custom Logout (override Django default)
    path('accounts/logout/', logout_view, name='logout'),
]
