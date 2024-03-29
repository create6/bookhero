from django import http
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from a3_Model_Serializer.serializers import BookInfoSerializer, BookInfoModelSerializer, HeroInfoModelSerializer
from booktest.models import BookInfo,HeroInfo
from rest_framework.generics import GenericAPIView, ListAPIView,CreateAPIView,\
	RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.mixins import *
from django.shortcuts import get_object_or_404


#---------------一级视图----------------
#1,一级视图，APIView之request
class Demo1APIView(APIView):
	def get(self,request):
		print(request.query_params)
		print(request.query_params.get("name"))
		return http.HttpResponse("子曰：学而时习之，不亦乐乎")

	def post(self,request):
		print(request.data)
		return http.HttpResponse("老子曰：老子愿意！")

#2,一级视图，APIView之response
class Demo2APIView(APIView):
	def get(self,request):

		return Response({"context":"登高而呼，声非加疾也，而闻者彰"},status=status.HTTP_200_OK)

	def post(self,request):

		return Response({"context":"出污泥而不染"},status=status.HTTP_201_CREATED)

#3,一级视图，查看列表视图
class BookInfoAPIView(APIView):
	# 查看所有书籍(序列化）
	def get(self, request):
		# 1查询所有书籍
		books = BookInfo.objects.all()
		#2,获取序列化器
		serializer = BookInfoSerializer(instance=books, many=True)
		# 3返回响应
		return Response(serializer.data, status=status.HTTP_200_OK)

	# 创建单个书籍 create  （反json,反序列化，保存数据，入库）
	def post(self, request):
		# 1获取参数
		dict_data=request.data
		# 2获取序列化器
		serializer=BookInfoModelSerializer(data=dict_data)   #不是用instance=dict_data
		# 3,校验，入库
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#4,返回响应
		return Response(serializer.data,status=status.HTTP_201_CREATED)

#4,一级视图，查看详情视图
class BookInfoDetailView(APIView):
	def get(self,request,pk):
		#1,通过pk获取对象
		book=BookInfo.objects.get(pk=pk)
		#2,获取序列化器
		serializer=BookInfoModelSerializer(instance=book)
		#3返回响应
		return Response(serializer.data,status=status.HTTP_200_OK)
	#修改
	def put(self,request,pk):
		#1,获取参数
		dict_data=request.data
		book = BookInfo.objects.get(pk=pk)
		# 2,获取序列化器
		serializer = BookInfoModelSerializer(instance=book,data=dict_data)
		#3,校验，入库
		serializer.is_valid(raise_exception=True)
		serializer.save()

		#4,返回响应
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	#3 delete
	def delete(self,request,pk):
		#1 获取对象
		book=BookInfo.objects.get(pk=pk)
		#2,删除书籍
		book.delete()
		#3,response
		return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------二级视图----------------
#5,二级视图，GenericAPIView实现列表视图
class BookInfoGenericAPIView(GenericAPIView):
	'''
	GenericAPIView特点:
	1, GenericAPIView,继承自APIView，
	2, 为标准列表和详细视图,添加了常用的行为,和属性
	    属性:
	        serializer_class    :指定通过序列化器
	        queryset            :指定通用的数据集
	        lookup_field        :默认是pk,用来获取单个对象

	    方法(行为):
	        get_serializer:     :获取序列化器对象
	        get_queryset:       :获取queryset数据集
	        get_object          :根据lookup_field,获取单个对象


	'''
	#1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer
	# serializer_class = HeroInfoModelSerializer  #英雄
	#2,指定通用数据集
	queryset=BookInfo.objects.all()
	# queryset=HeroInfo.objects.all()  #英雄
	# 查看所有书籍(序列化）
	def get(self, request):
		# 1查询所有书籍
		# books = self.queryset.all()
		books=self.get_queryset()
		#2,获取序列化器
		# serializer = self.serializer_class(instance=books, many=True)
		serializer=self.get_serializer(instance=books, many=True)
		# 3返回响应
		return Response(serializer.data, status=status.HTTP_200_OK)

	# 创建单个书籍 create  （反json,反序列化，保存数据，入库）
	def post(self, request):
		# 1获取参数
		dict_data=request.data
		# 2获取序列化器
		# serializer=BookInfoModelSerializer(data=dict_data)   #不是用instance=dict_data
		# serializer = self.serializer_class(data=dict_data)
		serializer = self.get_serializer(data=dict_data)
		# 3,校验，入库
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#4,返回响应
		return Response(serializer.data,status=status.HTTP_201_CREATED)

#6二级详情视图
class GenericBookDetailAPIView(GenericAPIView):
	# 1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer
	# serializer_class = HeroInfoModelSerializer  #英雄
	# 2,指定通用数据集
	queryset = BookInfo.objects.all()
	# queryset=HeroInfo.objects.all()  #英雄
	# 查看单个书籍(序列化）
	def get(self,request,pk):
		# 1 获取单个对象
		book = self.get_object()
		# book = self.get_queryset()
		# 2,获取序列化器
		# serializer = self.serializer_class(instance=books, many=True)
		serializer = self.get_serializer(instance=book)
		# 3返回响应
		return Response(serializer.data, status=status.HTTP_200_OK)
	#修改单个对象
	def put(self,request,pk):
		# 1,获取参数
		dict_data = request.data
		# book = BookInfo.objects.get(pk=pk)
		book = self.get_object()  #获取对象
		# 2,获取序列化器
		serializer = self.get_serializer(instance=book, data=dict_data)
		# 3,校验，入库
		serializer.is_valid(raise_exception=True)
		serializer.save()
		# 4,返回响应
		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
	# 3 delete
	def delete(self, request, pk):
		# 1 获取对象
		book = self.get_object()
		# 2,删除书籍
		book.delete()
		# 3,response
		return Response(status=status.HTTP_204_NO_CONTENT)

#7二级视图，GenericAPIView + Mixin 实现列表视图..ListModelMixin,CreateModelMixin,RetrieveModelMixin
class BookMixinGenericAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):
	'''
	bobo
	GenericAPIView特点:
	1, GenericAPIView,继承自APIView，
	2, 为标准列表和详细视图,添加了常用的行为,和属性
	    属性:
	        serializer_class    :指定通过序列化器
	        queryset            :指定通用的数据集
	        lookup_field        :默认是pk,用来获取单个对象

	    方法(行为):
	        get_serializer:     :获取序列化器对象
	        get_queryset:       :获取queryset数据集
	        get_object          :根据lookup_field,获取单个对象


	'''
	#1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer #书籍类
	# serializer_class = HeroInfoModelSerializer  #英雄类
	#2,指定通用数据集
	queryset=BookInfo.objects.all()     #书籍类
	# queryset=HeroInfo.objects.all()   #英雄
	# 查看所有书籍(序列化）
	def get(self, request):
		return self.list(request)
	# 创建单个书籍 create  （反json,反序列化，保存数据，入库）
	def post(self, request):
		return self.create(request)

#8二级 迷信-详情视图
class MixinGenericBookDetailView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	# 1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer
	# serializer_class = HeroInfoModelSerializer  #英雄
	# 2,指定通用数据集
	queryset = BookInfo.objects.all()
	# queryset=HeroInfo.objects.all()  #英雄
	# 查看单个书籍(序列化）
	def get(self,request,pk):
		return self.retrieve(request)
	#修改单个对象
	def put(self,request,pk):
		return self.update(request)
	# 3 delete
	def delete(self, request, pk):
		return self.destroy(request)

#---------------三级视图----------------
#9三级视图，GenericAPIView + Mixin 实现列表视图..ListModelMixin,CreateModelMixin,RetrieveModelMixin
class BookThirdAPIView(ListAPIView,CreateAPIView):
	'''
	bobo
	GenericAPIView特点:
	1, GenericAPIView,继承自APIView，
	2, 为标准列表和详细视图,添加了常用的行为,和属性
	    属性:
	        serializer_class    :指定通过序列化器
	        queryset            :指定通用的数据集
	        lookup_field        :默认是pk,用来获取单个对象

	    方法(行为):
	        get_serializer:     :获取序列化器对象
	        get_queryset:       :获取queryset数据集
	        get_object          :根据lookup_field,获取单个对象


	'''
	#1,指定通用的序列化器
	# serializer_class = BookInfoModelSerializer #书籍类
	serializer_class = HeroInfoModelSerializer  #英雄类
	#2,指定通用数据集
	# queryset=BookInfo.objects.all()     #书籍类
	queryset=HeroInfo.objects.all()   #英雄

#10 三级 详情视图
class ThirdDetailView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
	# 1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer
	# serializer_class = HeroInfoModelSerializer  #英雄
	# 2,指定通用数据集
	queryset = BookInfo.objects.all()
	# queryset=HeroInfo.objects.all()  #英雄

#---------------视图集----------------
# 11 查看列表及详情视图，viewset
class BookViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = BookInfo.objects.all()
		serializer = BookInfoModelSerializer(queryset, many=True)
		return Response(serializer.data)
	#查看单个
	def retrieve(self, request, pk=None):
		queryset = BookInfo.objects.all()
		book = get_object_or_404(queryset, pk=pk)
		serializer = BookInfoModelSerializer(instance=book)
		return Response(serializer.data)

# 12 查看列表及详情视图，ReadOnlyModelViewSet
class BookROViewSet(viewsets.ReadOnlyModelViewSet):
	#1,指定通用的序列化器
	serializer_class = BookInfoModelSerializer #书籍类
	# serializer_class = HeroInfoModelSerializer  #英雄类
	#2,指定通用数据集
	queryset=BookInfo.objects.all()     #书籍类
	# queryset=HeroInfo.objects.all()   #英雄

#13 视图集，终极版
class HeroModelViewSet(viewsets.ModelViewSet):
	# 1,指定通用的序列化器
	# serializer_class = BookInfoModelSerializer  # 书籍类
	serializer_class = HeroInfoModelSerializer  #英雄类
	# 2,指定通用数据集
	# queryset = BookInfo.objects.all()  # 书籍类
	queryset=HeroInfo.objects.all()   #英雄

	#额外功能，定制
	def special_hero(self,request):
		heros=HeroInfo.objects.filter(hgender =0 )
		#获取序列化器
		serializer=self.get_serializer(instance=heros,many=True)
		return Response(serializer.data)
	#额外功能，partial
	def update_hero(self,request,pk):
		#1,获取参数
		dict_data=request.data
		hero=self.get_object()
		#2,获取序列化器，入库,,partial=True 允许局部更新
		serializer=self.get_serializer(instance=hero,data=dict_data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#3,返回
		return Response(serializer.data)
















