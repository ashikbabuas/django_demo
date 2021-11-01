from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from users import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterApi.as_view(), name='register'),
    path('users/', views.UserList.as_view(), name='users')
]
