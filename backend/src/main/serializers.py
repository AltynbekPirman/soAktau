from rest_framework import serializers

from main.accessories import ImageLinker
from main.models import CompanyInfo, Address, TaxiQuestion


class CompanyInfoSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = CompanyInfo
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'text': ImageLinker(obj.info_kaz).link_images(), 'icon': self.get_thumbnail_url(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'text': ImageLinker(obj.info_rus).link_images(), 'icon': self.get_thumbnail_url(obj)}


class AddressSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Address
        fields = ('kaz', 'rus')

    def group_by_lang_kaz(self, obj):
        return {
            'emails': self.get_mails(obj), 'busStops': self.get_buses(obj),
            'addresses': self.get_kaz_info(obj), 'markers': self.get_coordinates(obj),
            'tels': self.get_phones(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'emails': self.get_mails(obj), 'busStops': self.get_buses(obj),
            'addresses': self.get_rus_info(obj), 'markers': self.get_coordinates(obj),
            'tels': self.get_phones(obj)
        }

    @staticmethod
    def get_coordinates(obj):
        coordinates = obj.coordinates.all()
        return [{'lat': coordinate.latitude, 'lon': coordinate.longitude} for coordinate in coordinates]

    @staticmethod
    def get_phones(obj):
        phones = obj.phones.all()
        return [phone.telephone for phone in phones]

    @staticmethod
    def get_mails(obj):
        emails = obj.emails.all()
        return [email.email for email in emails]

    @staticmethod
    def get_buses(obj):
        buses = obj.buses.all()
        return [bus.bus_num for bus in buses]

    @staticmethod
    def get_rus_info(obj):
        addresses = obj.addresses.all()
        return [address.text_rus for address in addresses]

    @staticmethod
    def get_kaz_info(obj):
        addresses = obj.addresses.all()
        return [address.text_kaz for address in addresses]


class ChatSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Address
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'icon': self.get_thumbnail_url(obj),
                'messages': self.get_kaz_messages(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'icon': self.get_thumbnail_url(obj),
                'messages': self.get_rus_messages(obj)}

    @staticmethod
    def get_kaz_messages(obj):
        messages = obj.messages.all()
        return [{'_id': message.id, 'text': message.message_kaz} for message in messages]

    @staticmethod
    def get_rus_messages(obj):
        messages = obj.messages.all()
        return [{'_id': message.id, 'text': message.message_rus} for message in messages]


class TaxiInfoSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Address
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def get_image_urls(self, obj):
        images = obj.images.all()
        return [self.context['request'].build_absolute_uri(image.icon.url) for image in images]

    @staticmethod
    def get_phones(obj):
        phones = obj.phones.all()
        return [phone.telephone for phone in phones]

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'text': obj.text_kaz, 'icon': self.get_thumbnail_url(obj),
                'title': obj.title_kaz, 'tels': self.get_phones(obj), 'imageUrls': self.get_image_urls(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'text': obj.text_rus, 'icon': self.get_thumbnail_url(obj),
                'title': obj.title_rus, 'tels': self.get_phones(obj), 'imageUrls': self.get_image_urls(obj)}


class TaxiQuestionSerializer(serializers.ModelSerializer):

    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = TaxiQuestion
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'question': obj.question_kaz, 'answer': obj.answer_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'question': obj.question_rus, 'answer': obj.answer_rus}
