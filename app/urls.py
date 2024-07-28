from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path('',views.create_user_api_view),
    path('confirm-user',views.BasicView.as_view()),
    path('obtain',TokenObtainPairView.as_view()),
    path('refresh',TokenRefreshView.as_view()),
    path('delete/<str:username>/',views.DeleteApiView.as_view()),
]
