from rest_framework import serializers
from services.models import Service, Post, SubService, Title, CalcParameter, CalcQuestion


class PostTextSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Post
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'text': obj.text_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'text': obj.text_rus}


class ServiceSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Service
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'icon': self.get_thumbnail_url(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'icon': self.get_thumbnail_url(obj)}


class SubServiceSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = SubService
        fields = ('kaz', 'rus')

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'serviceId': self.context.get('service_id')}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'serviceId': self.context.get('service_id')}


class TitleSerializer(serializers.ModelSerializer):

    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Title
        fields = ('kaz', 'rus')

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.name_kaz,
                'serviceId': self.context.get('service_id'), 'subServiceId': self.context.get('sub_service_id')}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.name_rus,
                'serviceId': self.context.get('service_id'), 'subServiceId': self.context.get('sub_service_id')}


class TitleDetailSerializer(serializers.ModelSerializer):
    posts = PostTextSerializer(many=True)

    class Meta:
        model = Title
        fields = ('posts',)


class CalcParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalcParameter
        fields = ('name', 'value')


class CalcQuestionSerializer(serializers.ModelSerializer):

    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = CalcQuestion
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'question': obj.question_kaz, 'answer': obj.answer_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'question': obj.question_rus, 'answer': obj.answer_rus}
