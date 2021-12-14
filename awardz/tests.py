from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Projects, Rating
import datetime as dt

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Review(user='Rinnah', bio='student', profile_photo='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Review))
   
class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Projects(title='RESORT APP', project_image='cloudlink.cloud', description='3D interpretation of a 4D object', link='tess.com', pub_date='2020', prof_ref='MontezProfile')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

class RatingTestClass(TestCase):
    def setUp(self):
        self.rating = Rating(user='chelsea', project='NEWS REVIEW', review='excellent', rate_design=10, rate_usability=9, rate_content=8)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))