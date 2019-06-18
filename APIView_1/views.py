from django import http
from rest_framework.views import APIView
from rest_framework.response import Response


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

		return Response("登高而呼，声非加疾也，而闻者彰")

	def post(self,request):
		print(request.data)
		return http.HttpResponse("老子曰：老子愿意！")