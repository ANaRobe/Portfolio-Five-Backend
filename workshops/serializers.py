from rest_framework import serializers
from .models import Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Fields to display.
        """
        model = Workshop
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'price',
            'link',
            'date',
            'time',
            'location',
            'created_on',
            'last_edit',
            'is_owner',
            'profile_id',
            'profile_image',
        ]
