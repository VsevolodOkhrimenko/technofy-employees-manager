from rest_framework import serializers

from django.conf import settings

from apps.users.models import User
from apps.skill.serializers import SkillSerializer
from apps.sector.serializers import SectorSerializer


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(
        format='%H:%M %d.%m.%Y', read_only=True)

    avatar = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)
    days_in_company = serializers.SerializerMethodField(read_only=True)

    sector = SectorSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    def get_avatar(self, obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + \
            'images/default_avatar.png'

    def get_full_name(self, obj):
        return obj.full_name

    def get_short_name(self, obj):
        return obj.short_name

    def get_days_in_company(self, obj):
        return obj.days_in_company

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'avatar',
            'first_name',
            'last_name',
            'full_name',
            'short_name',
            'nationality',
            'age',
            'address',
            'phone_number',
            'sector',
            'skills',
            'salary',
            'started',
            'is_employee',
            'ended',
            'days_in_company',
            'is_archived',
            'registered_at']

class UserProfileSerializer(serializers.ModelSerializer):

    sector = SectorSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'avatar',
            'nationality',
            'age',
            'address',
            'phone_number',
            'started',
            'sector',
            'skills',
            'salary',
            'is_employee',
            'is_archived',
            'ended']


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
