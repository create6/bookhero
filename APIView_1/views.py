from django import http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from a3_Model_Serializer.serializers import BookInfoSerializer, BookInfoModelSerializer
from booktest.models import BookInfo



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

#3,一级视图，查看视图列表
class BookInfoAPIView(APIView):
	# 查看所有书籍
	def get(self, request):
		# 1查询所有书籍
		books = BookInfo.objects.all()
		#2,获取序列化器
		serializer = BookInfoSerializer(instance=books, many=True)
		# 3返回响应
		return Response(serializer.data, status=status.HTTP_200_OK)

	# 创建单个书籍
	def post(self, request):
		# 1获取参数
		dict_data=request.data
		# 2获取序列化器
		serializer=BookInfoModelSerializer(instance=dict_data)
		# 3,校验，入库
		serializer.is_valid(raise_exception=True)
		serializer.save()
		#4,返回响应
		return Response(serializer.data,status=status.HTTP_201_CREATED)
