import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import TblSnippets, TblTags
from .serializers import SnippetSerializer, TagsSerializer


def ValError(message):
    return {"MESSAGE": "Validation error occured", "ERROR": message, "STATUS": False}


def ErrorDict(message):
    return {"MESSAGE": "Exception error occured", "ERROR": message, "STATUS": False}


def SuccessDict(message):
    return {"MESSAGE": message, "STATUS": True}


class Snippet(ListAPIView):

    authentication_classes = (TokenAuthentication,)
    serializer_class = SnippetSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        try:
            id_ = self.request.GET.get('id', "")
            qs = TblSnippets.objects.all()
            if id_ != "": qs = qs.filter(id=id_)
            return qs
        except Exception as e: return APIException(e)

    def post(self, request):
        try:
            title = request.POST["title"]
            snippet = request.POST["snippet"]
            tags_id = json.loads(request.POST["tags_id"])
            if title != "": return JsonResponse(ValError("invalid value for title"))
            instance = TblSnippets.objects.create(title=title, snippet=snippet)
            instance.tags.add(*TblTags.objects.filter(id__in=tags_id))
            return JsonResponse(SuccessDict("snippet added Successfully"))

        except Exception as e: return JsonResponse(ErrorDict(e))

    def post(self, request):
        try:
            id_ = request.POST["id"]
            title = request.POST["title"]
            snippet = request.POST["snippet"]
            tags_id = request.POST["tags_id"]
            if title != "": return JsonResponse(ValError("invalid value for title"))
            instance = TblSnippets.objects.filter(id=id_)
            if not instance.exists(): return JsonResponse(ValError("invalid id is passed"))
            instance.update(title=title, snippet=snippet)
            instance.tags.add(*TblTags.objects.filter(id__in=tags_id))
            return JsonResponse(SuccessDict("snippet added Successfully"))

        except Exception as e: return JsonResponse(ErrorDict(e))

    def delete(self, request):
        try:
            id_ = request.GET["id"]
            instance = TblSnippets.objects.filter(id=id_).first()
            if instance is not None:
                instance.delete()
                JsonResponse(SuccessDict("snippet deleted Successfully"))
            else: return JsonResponse(ValError("objects does not exists"))
        except Exception as e: return JsonResponse(ErrorDict(e))


class Tags(ListAPIView):

    authentication_classes = (TokenAuthentication,)
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        try:
            id_ = self.request.GET.get('id', "")
            qs = TblTags.objects.all()
            if id_ != "": qs = qs.filter(id=id_)
            return qs
        except Exception as e: return APIException(e)

    def post(self, request):
        try:
            title = request.POST["title"]
            if title != "": return JsonResponse(ValError("invalid value for title"))
            if TblTags.objects.filter(title=title).exists(): return JsonResponse(ValError("title already exist"))
            TblTags.objects.create(title=title)
            return JsonResponse(SuccessDict("tag created successfully"))
        except Exception as e: return JsonResponse(ErrorDict(e))

    def delete(self, request):
        try:
            id_ = request.GET["id"]
            instance = TblTags.objects.filter(id=id_).first()
            if instance is not None:
                instance.delete()
                JsonResponse(SuccessDict("tag deleted Successfully"))
            else: return JsonResponse(ValError("objects does not exists"))
        except Exception as e: return JsonResponse(ErrorDict(e))



