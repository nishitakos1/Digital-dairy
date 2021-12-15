from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .helpers import *
from .models import Profile

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'Username is not found'
                raise Exception('Username is not found')
            if data.get('password') is None:
                response['message'] = 'password is not found'
                raise Exception('password is not found')

            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid Username'
                raise Exception('Invalid Username')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            


            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'WELCOME'
            else:
                response['message'] = 'Invalid password'
                raise Exception('Invalid password')

        except Exception as e:
            print(e)

        return Response(response)

LoginView = LoginView.as_view()

class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'Username is not found'
                raise Exception('Username is not found')
            if data.get('password') is None:
                response['message'] = 'password is not found'
                raise Exception('password is not found')

            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')

            user_obj = User.objects.create(email= data.get('username'), username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()

            token = generate_random_sting(21)
            Profile.objects.create(user = user_obj, token = token)
            #send_mail_to_user(token, data.get('username'))

            response['message'] = 'User created'
            response['status'] = 200


        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()
