from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^demo1/$', views.Demo1APIView.as_view())


]