from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie


# -----------------------------------------
# HOME PAGE (IMPORTANT: CSRF FIXED)
# -----------------------------------------
@login_required
@ensure_csrf_cookie
def home(request):
    return render(request, 'home.html')


# -----------------------------------------
# SIGNUP PAGE
# -----------------------------------------
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


# -----------------------------------------
# TASK API
# -----------------------------------------
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
