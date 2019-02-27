from rest_framework import serializers
from apps.sector.models import Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
            'standardized',
        )
