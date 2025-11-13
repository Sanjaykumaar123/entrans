from django.contrib import admin
from django.urls import path, include
from todo.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
