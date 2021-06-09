from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import UserProfile, User
import smtplib
from email.message import EmailMessage

# Create your views here.


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],


            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }
        print(request.data['email'])
        data = request.data['email']
        print(data)
        try:
            msg = EmailMessage()
            msg['Subject'] = f'Welcome to Trophy Case {data}'
            msg['From'] = 'hunterbooktrophycase@gmail.com'
            msg['To'] = f'{data}'
            msg.set_content('WELCOME TO TROPHY CASE. Thanks for signing up. You may be asking yourself, '
                            '"Why would I want to pay 1$ per year for using this website!?" Well, truthfully'
                            'you are not paying for the website. The website is free. However, paying people $$$$'
                            'rewards is not possible, without the communities annual subscription. I do not keep any of it.'
                            '100% of all the subscription money is paid out annually to the winners of the games. '
                            'If you participate with 1$ a year, you could win 1$ x the number of people subscriped, divided by'
                            'the current number of games which are 6. However, only 3 of them are won annually, the others in time'
                            'could take years to beat the last records. So, really you are just buying your fellow hunter'
                            'a cheap cup of coffee, to say "congratulations" for his trophy.')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('hunterbooktrophycase@gmail.com', 'Wordpass1!')
                smtp.send_message(msg)
        except: print("didn't work")


        return Response(response, status=status_code)


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                    'user_id': user_profile.user_id
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)



class Email(APIView):
    permission_classes = [];
    def send_winner_email(self, request):
        data = request.data['email']  #need to change this to figure out what the data will look like coming in
        msg = EmailMessage()
        msg['Subject'] = f'You are on the leader board! Nice Trophy! {data}'
        msg['From'] = 'hunterbooktrophycase@gmail.com'
        msg['To'] = f'{data}'
        msg.set_content('Did you see yourself on the Trophy Case leader board? Nice work! If you hold position there,'
                        'till the end of the year. You will win the pot for that category!')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('hunterbooktrophycase@gmail.com', 'Wordpass1!')
            smtp.send_message(msg)

