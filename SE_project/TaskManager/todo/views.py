from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Task
from .serializers import TaskSerializer


# =============================
#      HOME PAGE (PROTECTED)
# =============================
@login_required
def home(request):
    return render(request, "home.html")


# =============================
#       SIGNUP VIEW
# =============================
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)     # Auto login after signup
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


# =============================
#       CUSTOM LOGOUT
# =============================
def logout_view(request):
    logout(request)
    return redirect("login")     # Redirect to login page after logout


# =============================
#      TASK API VIEWSET
# =============================
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
