from rest_framework import routers
from apps.users.views import UserViewSet
from apps.sector.views import SectorViewSet
from apps.skill.views import SkillViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api.register(r'sectors', SectorViewSet)
api.register(r'skills', SkillViewSet)
