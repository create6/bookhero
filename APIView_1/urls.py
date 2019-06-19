from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^demo1/$', views.Demo1APIView.as_view()),
	url(r'^demo2/$', views.Demo2APIView.as_view()),
	url(r'^books/$', views.BookInfoAPIView.as_view()),
	url(r'^books/(?P<pk>\d+)/$', views.BookInfoDetailView.as_view()),
	#二级列表视图路由
	url(r'^genericBooks/$', views.BookInfoGenericAPIView.as_view()),

    #二级详情视图路由
	url(r'^genericBooks/(?P<pk>\d+)/$', views.GenericBookDetailAPIView.as_view()),
	#二级 迷信-列表视图路由
	url(r'^MiGenericBooks/$', views.BookMixinGenericAPIView.as_view()),
#二级 迷信-详情视图路由
	url(r'^MiGenericBooks/(?P<pk>\d+)/$', views.MixinGenericBookDetailView.as_view()),
	#三级-列表
	url(r'^ThirdBooks/$', views.BookThirdAPIView.as_view()),
	#三级-详情
	url(r'^ThirdBooks/(?P<pk>\d+)/$', views.ThirdDetailView.as_view()),




]