

from django import http

#1,一级视图，APIView之request
from rest_framework.views import APIView


class Demo1APIView(APIView):
	def get(self,request):
		print(request.query_params)
		print(request.query_params.get("name"))
		return http.HttpResponse("子曰：学而时习之，不亦乐乎")

	def post(self,request):
		print(request.data)
		return http.HttpResponse("老子曰：老子愿意！")


