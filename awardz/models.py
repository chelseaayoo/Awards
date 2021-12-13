from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile/",default = "default.jpg")
    bio = HTMLField()
    updated_on = models.DateTimeField(auto_now_add=True)

class Project_Post(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    img_project = models.ImageField(upload_to="project/")
    project_url = models.URLField()
    description = TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True)
    
    
    def get_all_projects():
        projects = Project_Post.objects.all()
        return projects
    
    @classmethod
    def get_project_by_id(cls,id):
        project = Project_Post.objects.filter(id=id)
        
        return project
        