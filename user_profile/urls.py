from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('registration/', views.RegisterAPIView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]
