import json
import requests
from uuid import uuid4

from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.users.models import User
from apps.sector.models import Sector
from apps.skill.models import Skill
from apps.users.serializers import UserSerializer, UserWriteSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserSerializer
        return UserWriteSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        if 'password' in self.request.data:
            user.set_password(self.request.data.get('password'))
            user.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        skills_query = self.request.GET.get('skills', None)
        sector_query = self.request.GET.get('sector', None)
        sort_by = "-"
        sort_by += self.request.GET.get('sort', 'first_name')
        is_employee = json.loads(self.request.GET.get('is_employee', 'true'))
        print(skills_query)
        qs = User.objects.filter(is_employee=is_employee)
        if skills_query:
            qs = qs.filter(skills__name__in=skills_query.split(','))
        if sector_query:
            qs = qs.filter(sector__name=sector_query)
        return qs.order_by(sort_by).distinct()

    @list_route(methods=['GET'])
    def profile(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['POST'])
    def login(self, request, format=None):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            serializer = self.serializer_class(user)
            response_data = {'token': user.token}
            response_data.update(serializer.data)
            return Response(status=status.HTTP_200_OK, data=response_data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['POST'])
    def register(self, request):
        last_name = request.data.get('last_name', None)
        first_name = request.data.get('first_name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if User.objects.filter(email__iexact=email).exists():
            return Response({'status': 210})

        # user creation
        user = User.objects.create(
            email=email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            is_admin=False,
        )
        response_data = {'token': user.token}
        response_data.update(UserSerializer(user).data)
        return Response(
            response_data,
            status=status.HTTP_201_CREATED)

    @list_route(methods=['POST'])
    def password_reset(self, request, format=None):
        if User.objects.filter(email=request.data['email']).exists():
            user = User.objects.get(email=request.data['email'])
            params = {'user': user, 'DOMAIN': settings.DOMAIN}
            send_mail(
                subject='Password reset',
                message=render_to_string('mail/password_reset.txt', params),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.data['email']],
            )
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['POST'])
    def save_user_settings(self, request, format=None):
        if User.objects.filter(token=request.data['token']).exists():
            user = User.objects.get(token=request.data['token'])
            data = request.data.copy()
            if data['new_password']:
                user.set_password(data['new_password'])
                user.token = uuid4()
            if user.email != data['email']:
                if User.objects.filter(email=data['email']).exists():
                    return Response({'error': "Email exist"},
                        status=status.HTTP_400_BAD_REQUEST)
                user.email = data['email']
            user.save()
            return Response({'token': user.token}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['POST'])
    def save_profile_settings(self, request, format=None):
        if User.objects.filter(token=request.data['token']).exists():
            user = User.objects.get(token=request.data['token'])
            data = request.data.copy()
            del data['skills']
            del data['sector']
            skills = self._normalized_skills(request.data.get('skills', []))
            try:
                sector_name = request.data.get('sector', '')
                sector = Sector.objects.get(name=sector_name.strip())
            except Sector.DoesNotExist:
                sector = Sector(name=sector_name, standardized=False)
                sector.save()
            serializer = UserProfileSerializer(instance=user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(
                skills=skills, sector=sector)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def _normalized_skills(skill_names):
        skills = []
        for skill_name in skill_names:
            try:
                skill_obj = Skill.objects.get(name=skill_name.strip())
            except Skill.DoesNotExist:
                skill_obj = Skill(name=skill_name, standardized=False)
                skill_obj.save()
            skills.append(skill_obj)
        return skills
