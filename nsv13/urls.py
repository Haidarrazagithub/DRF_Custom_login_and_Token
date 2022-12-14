"""nsv13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api import views
from api.views import PatientList, UserCreate, LoginView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
# from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# schema_view = get_swagger_view(title='Patient API')
# router=DefaultRouter()

# router.register('PatientList',views.PatientList,basename='PatientList')

urlpatterns = [
    # path(r'docs/', include_docs_urls(title='Patient API')),
    path('admin/', admin.site.urls),
    path('patientlist/', PatientList.as_view(), name='patientlist'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('auth',include('rest_framework.urls'))
    # path(r'swagger/', schema_view),
    # path('',include(router.urls))
]
