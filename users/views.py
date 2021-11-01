from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from django.http import JsonResponse
from API.views import ValError, ErrorDict, SuccessDict
from users.serializers import UserSerializer


class RegisterApi(ListAPIView):

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST["name"]
            username = request.POST["username"]
            password = request.POST["password"]

            user = User.objects.filter(username=username)
            if user.exists(): return JsonResponse(ValError("username already exist"))
            User.objects.create(username=username, first_name=name, password=make_password(password))
            return JsonResponse(SuccessDict("registraion is completed"))
        except Exception as e: JsonResponse(ErrorDict(e))


class UserList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            id_ = self.request.GET.get("id","")
            qs = User.objects.all()
            if id_ != "": qs.filter(id=id_)
            return qs
        except Exception as e: return User.objects.none()



