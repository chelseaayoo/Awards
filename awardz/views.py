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

@login_required
def post_project_view(request):
    if request.method =='POST':
        form = Post_projectform(request.POST,request.FILES)
        
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.posted_by = request.user
            new_project.save()
            return redirect('home')
        else:
            messages.info(request,'all fields are required')
            return redirect('post-project')
    
    else:
        form = Post_projectform()
    return render(request,'new_post.html',{"form":form})

@login_required
def post_review_view(request,id):
    
    form = ReveiwForm()
    reviews = Reviews.get_review_by_project_id(id)
    project = Project_Post.get_project_by_id(id)
    rates = Rates.get_rates_by_project_id(id)
    desrate = []
    usarate=[]
    conrate=[]
    if rates:
        for rate in rates:
            desrate.append(rate.design)
            usarate.append(rate.usability)
            conrate.append(rate.content)
        total = len(desrate)*9
        design =round(sum(desrate)/total *100,2)
        usability = round(sum(usarate)/total *100,2)
        content = round(sum(conrate),2)
        return render(request,'single_project.html',{"form":form,"reviews":reviews,"project":project,"project_id":id,"design":design,"usability":usability,"content":content})
    else:
        usability=0
        design = 0
        content = 0
        return render(request,'single_project.html',{"form":form,"reviews":reviews,"project":project,"project_id":id,"design":design,"usability":usability,"content":content})

@login_required   
def review_post(request,id):
    if request.method=='POST':
        form = ReveiwForm(request.POST)
        
        if form.is_valid():
            new_review=form.save(commit=False)
            new_review.posted_by = request.user
            project = Project_Post.objects.get(id=id)
            new_review.project_id = project
            new_review.save()
            return redirect('post-review',id)

@login_required
def post_rate_view(request,id):
    if request.method=='POST':
        rates = Rates.get_rates_by_project_id(id)
        for rate in rates:
            if rate.rate_by ==request.user:
                messages.info(request,'You have alraedy rated the project')
                return redirect('post-review', id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')
        
        if design and usability and content:
            project = Project_Post.objects.get(id=id)
            rate = Rates(design = design,usability = usability,content=content,project_id = project,rate_by=request.user)
            
            rate.save()
            return redirect('post-review',id)
    else:
        messages.info(request,'all fields are required')
        return redirect('post-review',id)

@login_required
def update_profile_view(request):
    if request.method =='POST':
        form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        userform = UserUpdateform(request.POST,instance=request.user)
        
        if form.is_valid() and userform.is_valid():
            form.save()
            userform.save()
            return redirect('profile')
    else:
        form = UpdateProfile(instance=request.user.profile)
        userform = UserUpdateform(instance=request.user)
    return render(request,"update_profile.html",{"form":form,"userform":userform})

        