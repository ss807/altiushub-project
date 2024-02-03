import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    body = request.body or '{}'
    body_json = json.loads(body)
    username = body_json.get("username")
    password = body_json.get("password")
    if not username or not password:
        return JsonResponse({"status": 0, "message": "Please enter valid credentials"}, status=403)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": 0, "message": "Logged in successfully", "data": {"user": user}}, status=200)
    return JsonResponse({"status": 0, "message": "Unable to login", "data": {"user": user}}, status=400)

def logout(request):
    logout(request)

@login_required(login_url="/api/login")
def index(request):
    return JsonResponse({"status": 1, "message": "Success"})