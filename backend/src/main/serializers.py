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

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'messages': self.get_kaz_messages(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'messages': self.get_rus_messages(obj)}

    @staticmethod
    def get_kaz_messages(obj):
        messages = obj.messages.all()
        return [{'_id': message.id, 'text': message.message_kaz} for message in messages]

    @staticmethod
    def get_rus_messages(obj):
        messages = obj.messages.all()
        return [{'_id': message.id, 'text': message.message_rus} for message in messages]
