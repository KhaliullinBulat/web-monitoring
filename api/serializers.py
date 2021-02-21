from rest_framework import serializers
from monitoring.models import Link
from monitoring.views import make_resp
from django_q.tasks import async_task


# class LinkSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Link
#         fields = ['id', 'link', 'finish_link', 'response']


class LinkListSerializer(serializers.ListSerializer):
    pass
    # link = serializers.CharField(max_length=1000)
    # def create(self, validated_data):
    #     return validated_data


class LinkNameSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=1000)

    class Meta:
        list_serializer_class = LinkListSerializer


class LinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=1000)
    last_check_time = serializers.DateTimeField()
    response = serializers.IntegerField()
    status = serializers.CharField(max_length=10)
    error = serializers.CharField(max_length=100000000)
    finish_link = serializers.CharField(max_length=1000)

    # class Meta:
    #     list_serializer_class = LinkListSerializer
