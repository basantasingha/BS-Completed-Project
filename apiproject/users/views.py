from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        response = {'status': 500, 'message': 'something went wrong'}

        try:
            data = request.data
            
            if 'username' not in data:
                response['message'] = 'key username not found'
                raise ValueError('key username not found')
            
            if 'password' not in data:
                response['message'] = 'key password not found'
                raise ValueError('key password not found')
            
            check_user = User.objects.filter(username=data['username']).first()

            if check_user is None:
                response['message'] = 'Invalid username, user not found'
                raise ValueError('Invalid username, user not found')
            
            user_obj = authenticate(username=data['username'], password=data['password'])
            
            if user_obj is not None:
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid password'
                raise ValueError('Invalid password')
            
        except ValueError as e:
            print(e)
            return Response(response)
        
        return Response(response)

# Note: Removed unnecessary line: LoginView = LoginView.as_view()


class RegisterView(APIView):
    def post(self, request):
        response = {'status': 500, 'message': 'something went wrong'}

        try:
            data = request.data
            
            if 'username' not in data:
                response['message'] = 'key username not found'
                raise ValueError('key username not found')
            
            if 'password' not in data:
                response['message'] = 'key password not found'
                raise ValueError('key password not found')
            
            check_user = User.objects.filter(username=data['username']).first()

            if check_user:
                response['message'] = 'Username already taken'
                raise ValueError('Username already taken')
            
            user_obj = User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User Created'
            response['status'] = 200
            
        except ValueError as e:
            print(e)
            return Response(response)
        
        return Response(response)

# Note: Removed unnecessary line: RegiaterView = RegisterView.as_view()
