from rest_framework import serializers

from main.models import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('code', )
