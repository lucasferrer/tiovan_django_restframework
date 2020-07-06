"""tiovan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tiovan_app.views import home
import tiovan_app.api_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'api/v1/endereco', tiovan_app.api_views.EnderecoViewSet)
router.register(r'api/v1/motorista', tiovan_app.api_views.MotoristaViewSet)
router.register(r'api/v1/instituicoes', tiovan_app.api_views.InstituicoesViewSet)
router.register(r'api/v1/responsavel', tiovan_app.api_views.ResponsavelViewSet)
router.register(r'api/v1/dependente', tiovan_app.api_views.DependenteViewSet)
router.register(r'api/v1/user', tiovan_app.api_views.UserViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Tiovan API",
      default_version='v1',
      description="Backend of tiovan APP",
      url='https://tiovan-backend.ml/api/v1',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ferrer.xtreme@gmail.com"),
      license=openapi.License(name="Tiovan License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    path('node/', home, name='home'),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
