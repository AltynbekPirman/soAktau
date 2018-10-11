from rest_framework import serializers

from main.models import CompanyInfo, Address


class CompanyInfoSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = CompanyInfo
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'text': obj.info_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'text': obj.info_rus}


class AddressSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Address
        fields = ('kaz', 'rus')

    def group_by_lang_kaz(self, obj):
        return {
            'id': obj.id, 'email': obj.email, 'buses': obj.buses,
            'address': obj.address_kaz, 'coordinates': self.get_coordinates(obj),
            'phones': self.get_phones(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'id': obj.id, 'email': obj.email, 'buses': obj.buses,
            'address': obj.address_rus, 'coordinates': self.get_coordinates(obj),
            'phones': self.get_phones(obj)
        }

    @staticmethod
    def get_coordinates(obj):
        coordinates = obj.coordinates.all()
        return {
            'latitude': [coordinate.latitude for coordinate in coordinates],
            'longitude': [coordinate.longitude for coordinate in coordinates]
        }

    @staticmethod
    def get_phones(obj):
        phones = obj.phones.all()
        return {
            'phones': [phone.telephone for phone in phones],
        }


class ChatSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Address
        fields = ('kaz', 'rus')

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'messages': self.get_kaz_messages(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'messages': self.get_rus_messages(obj)}

    @staticmethod
    def get_kaz_messages(obj):
        messages = obj.messages.all()
        return {
            'messages': [message.message_kaz for message in messages],
        }

    @staticmethod
    def get_rus_messages(obj):
        messages = obj.messages.all()
        return {
            'messages': [message.message_rus for message in messages],
        }
