from rest_framework import serializers
from file.service import thumbnail_files
from file.models import File


class FileFieldSerializer(serializers.FileField):
    def __init__(self, context, *args, **kwargs):
        super(FileFieldSerializer, self).__init__(*args, **kwargs)
        self.request = context['request']
        self.width = self.request.GET.get('width')
        self.height = self.request.GET.get('height')

    def to_representation(self, instance):
        url = thumbnail_files(instance, self.width, self.height)
        return self.request.build_absolute_uri(url)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id',
            'image',
            'format',
            'name',
            'ordering'
        ]

    def __init__(self, *args, **kwargs):
        super(FileSerializer, self).__init__(*args, **kwargs)
        self.request = self.context['request']
        if getattr(self.request, 'method', None) == 'GET':
            self.fields['image'] = FileFieldSerializer(context=self.context)


class FileUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id',
            'name',
            'image'
        ]
