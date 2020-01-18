from django.contrib import admin
# from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewSet,CreateUserView
from django.conf.urls import include,url
from restapp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from a1.views import *
from django.urls import path,include
router=routers.DefaultRouter()
# router=routers.SimpleRouter()
router.register(r'employee',EmployeeViewSets)
# router.register(r'employee',EmployeeViewSets)
# router.register(r'employee1',poll)

urlpatterns = [
    path('',include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # path('poll/',poll),
    path('poll/',POOLAPIView.as_view()),
    path('poll1/',POOLListView.as_view()),
    path('poll1/<int:id>/',POOLListView.as_view()),
    path('poll/<int:id>/',pool_details,name='get'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)