from django.contrib import admin
from django import forms

from my_city.models import CityImage, CityNews


class ImageInline(admin.StackedInline):
    model = CityImage
    extra = 1


class MyCityForm(forms.ModelForm):

    def clean(self):
        if self.initial:
            my_city_instance = self.save(commit=False)
            if my_city_instance.images.all():
                if self.cleaned_data.get('video_url') or self.cleaned_data.get('video_screenshot'):
                    raise forms.ValidationError("Невозможно добавить видео и изображение")
            if self.cleaned_data.get('video_url') or self.cleaned_data.get('video_screenshot'):
                if len(self.files) > 1 or 'video_screenshot' not in self.files:
                    raise forms.ValidationError("Невозможно добавить видео и изображение или видео без скриншота")
                elif self.cleaned_data.get('video_url') and self.cleaned_data.get('video_screenshot'):
                    return self.cleaned_data
                else:
                    raise forms.ValidationError("Видео необходимо добавить вместе со скриншотом")
            return self.cleaned_data

        else:
            if self.cleaned_data.get('video_url') or self.cleaned_data.get('video_screenshot'):
                if len(self.files) > 1:
                    raise forms.ValidationError("Videonyn men suret pa?")
                elif self.cleaned_data.get('video_url') and self.cleaned_data.get('video_screenshot'):
                    return self.cleaned_data
                else:
                    raise forms.ValidationError("Видео необходимо добавить вместе со скриншотом")
            elif not self.files:
                raise forms.ValidationError('Необходимо добавить видео или изображение')

    class Meta:
        model = CityNews
        fields = '__all__'


class MyCityAdmin(admin.ModelAdmin):
    form = MyCityForm
    inlines = [ImageInline, ]


admin.site.register(CityNews, MyCityAdmin)
