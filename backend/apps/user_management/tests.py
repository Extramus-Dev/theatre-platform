from django.forms.fields import EmailField
from django.http.response import JsonResponse
from django.test import TestCase, Client

from .models import User

USER_MODEL = {
    "email":"antonio@extramus.eu",
    "first_name":"Antonio", 
    "last_name": "Gallo", 
    "date_birth": "1990-01-25", 
    "password": "senhaforte",
}

class ViewerSignUp(TestCase):

    def setUp(self):
        self.client = Client()
        super().setUp()

    def accept_request(self):
        """
        Test if returns expected response(201)
        """
        data={"user":USER_MODEL}
        response = self.client.post(
            path='/users/signup/viewer',
            content_type='application/json',
            data=data,
        )
        #self.assertEqual(response.content,bytes((data)))
        self.assertEqual(response.status_code, 201)

class UserTest(TestCase):

    def setUp(self):
        super().setUp()


    def _create_user(self, email, first_name, last_name, date_birth, password):
        return User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            password=password,
        )  


    def test_create_user(self):
        user = self._create_user(
            email=USER_MODEL['email'], 
            first_name=USER_MODEL['first_name'], 
            last_name=USER_MODEL['last_name'],
            date_birth=USER_MODEL["date_birth"],
            password=USER_MODEL["password"],
        )
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.email,      USER_MODEL['email'])
        self.assertEqual(user.first_name, USER_MODEL['first_name'])
        self.assertEqual(user.last_name,  USER_MODEL['last_name'])
        self.assertEqual(user.date_birth, USER_MODEL["date_birth"])
        self.assertEqual(user.password,   USER_MODEL["password"])
