import json
from django import http
from django.shortcuts import render
from .models import BookInfo
from serializers import BookInfoSerializer

#查看所有书籍
from django.views import View


class SearchBooksView(View):
    #查看所有书籍
    def get(self,request):
        #1查询所有书籍
        books=BookInfo.objects.all()

        #2转换数据,
        # books_list=[]
        # for book in books :
        #     book_dict={
        #         "btitle": book.btitle,
        #         "bpub_date": book.bpub_date,
        #         "bread": book.bread,
        #         "bcomment": book.bcomment,
        #         "id": book.id
        #                 }
        #     books_list.append(book_dict)
        #2.2用序列化器改造

        serializer=BookInfoSerializer(instance=books,many=True)

        #3返回响应
        return http.JsonResponse(serializer.data,safe=False)
    #创建单个书籍
    def post(self,request):
        #1获取参数
        book_data = json.loads(request.body.decode())
        bpub_date = book_data.get("bpub_date")
        bread = book_data.get("bread")
        btitle = book_data.get("btitle")
        bcomment = book_data.get("bcomment")
        #2校验参数(省略）
        #3数据转换与入库,**book_dict 拆包

        book=BookInfo.objects.create(**book_data)
        # book.save()
        #4返回响应
        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "id": book.id
        }
        return http.JsonResponse(book_dict)



class SearchSingleBookView(View):
    def get(self,request,pk):
        #1,(参数校验省略)，获取书籍对象
        try:
            book=BookInfo.objects.get(id=pk)     #.filter() 与 .get()
            print(book)
        except BookInfo.DoesNotExist:
            #无此书
            return http.JsonResponse("查无此书")

        #2数据转换
        # book_dict = {
        #     "btitle": book.btitle,
        #     "bpub_date": book.bpub_date,
        #     "bread": book.bread,
        #     "bcomment": book.bcomment,
        #     "id": book.id
        # }
        #2.2 用序列化器改造
        serializer=BookInfoSerializer(instance=book)

        #3返回响应
        return http.JsonResponse(serializer.data)

    def put(self,request,pk):
        #1获取参数
        book_data = json.loads(request.body.decode())
        bpub_date = book_data.get("bpub_date")
        bread = book_data.get("bread")
        btitle = book_data.get("btitle")
        bcomment = book_data.get("bcomment")

        #2校验参数

        #3数据转换与入库
        book = BookInfo.objects.create(**book_data)

        #4返回响应
        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment,
            "id": book.id
        }
        return http.JsonResponse(book_dict)

    def delete(self,request,pk):
        #1校验参数
        try:
            book=BookInfo.objects.filter(id=pk)
        except BookInfo.DoesNotExist:
            #无此书
            return http.JsonResponse("查无此书")
        #有此书
        book.delete()
        return http.JsonResponse({"code":204})
