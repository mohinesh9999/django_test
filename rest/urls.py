"""rest URL Configuration

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
from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewSet,CreateUserView
from django.conf.urls import include,url
from restapp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
import a1
from a1.views import *
router=routers.DefaultRouter()
# router=routers.SimpleRouter()
router.register(r'task',views.TaskViewSet)
# router.register(r'completed_task',views.CompletedTaskViewSet)
# router.register(r'due_task',views.DueTaskViewSet)
# router.register(r'get_task',views.TaskList,base_name='MyModel")
# router.register()
urlpatterns = [
    url(r'^register/$',views.CreateUserView.as_view(),name='user'),
    # url(r'^api-auth/',include('rest_framework.urls'
    # ,namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('api/v1/',include('a1.api_urls')),
    path('api/v1/auth/login',loginView.as_view()),
    path('api/v1/auth/logout',logoutView.as_view()),
    # path('api/v1/auth/login',include('rest_auth.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
