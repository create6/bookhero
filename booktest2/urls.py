from django.conf.urls import url
from . import views

urlpatterns=[]

#drf中的路由
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'books',views.BookInfoModelViewSet,base_name="books")
urlpatterns +=router.urls