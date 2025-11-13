from django.contrib import admin
from django.urls import path, include
from todo.views import home, signup_view   # ⬅ add signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # API routes
    path('api/', include('todo.urls')),

    # Auth (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Signup route
    path('accounts/signup/', signup_view, name='signup'),
]
