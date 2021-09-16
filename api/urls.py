from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from .views import UserDetailsView


schema_view = get_schema_view(
   openapi.Info(
      title="Quiz API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('register/', RegisterView.as_view(), name='rest_register'),
   path('login/', LoginView.as_view(), name='rest_login'),
   path('logout/', LogoutView.as_view(), name='rest_logout'),
   path('users/<int:id>/', UserDetailsView.as_view(), name='user_details'),
   
   
]
