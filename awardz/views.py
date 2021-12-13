from django.http.response import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import Post_projectform,ReveiwForm,UpdateProfile,UserUpdateform
from django.contrib import messages
from .models import Project_Post,Profile,Reviews,Rates
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serialiers import ProfileSerializer,ProjectSerializer
# from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project_Post.get_all_projects()
    return render(request,"home.html",{"projects":projects})

def logout_view(request):
    logout(request)
    return redirect('/')