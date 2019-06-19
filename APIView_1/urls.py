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

	#视图集1 viewset
	url(r'^viewset/$',views.BookViewSet.as_view({"get":"list"})),
	url(r'^viewset/(?P<pk>\d+)/$',views.BookViewSet.as_view({"get":"retrieve"})),
	# 视图集2 ReadOnly
	url(r'^roviewset/$', views.BookROViewSet.as_view({"get": "list"})),
	url(r'^roviewset/(?P<pk>\d+)/$', views.BookROViewSet.as_view({"get": "retrieve"})),
	# 视图集3 ModelView
	url(r'^mdviewset/$', views.HeroModelViewSet.as_view({"get": "list","post":"create"})),
	url(r'^mdviewset/(?P<pk>\d+)/$', views.HeroModelViewSet.as_view({"get": "retrieve","put":"update","delete":"destroy"})),
	#额外 ,get--> special_hero
	url(r'^spviewset/$', views.HeroModelViewSet.as_view({"get": "special_hero"})),
	#额外功能，partial
	url(r'^spviewset/(?P<pk>\d+)/$', views.HeroModelViewSet.as_view({"put": "update_hero"})),



]