from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    """Registers a new user in the database."""
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    user.save()
    return Response({"message": "User registered successfully"}, status=201)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                response = JsonResponse({"success": True, "message": "Success", "redirect": "/TP1/myapp/templates/myapp/loggedin.html"})
                response.set_cookie("authenticated", "true", max_age=3600, httponly=False, samesite="Lax")
                response.set_cookie("username", user.username, max_age=3600, httponly=False, samesite="Lax")
                return response
            else:
                return JsonResponse({"success": False, "message": "Mauvais"})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON"}, status=400)

@csrf_exempt
def logout_user(request):
    response = HttpResponse("Logged out successfully")
    response.delete_cookie("authenticated")
    response.delete_cookie("username")
    logout(request)
    return JsonResponse({"success": True, "redirect": "/TP1/myapp/templates/myapp/connexion.html"}) 

@login_required(login_url="/TP1/myapp/templates/myapp/connexion.html")
def loggedin_view(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    return render(request, "/TP1/myapp/templates/myapp/loggedin.html")