from rest_framework.serializers import ModelSerializer
from .models import TblSnippets, TblTags


class TagsSerializer(ModelSerializer):

    class Meta:
        model = TblTags
        fields = "__all__"


class SnippetSerializer(ModelSerializer):

    class Meta:
        model = TblSnippets
        fields = "__all__"
