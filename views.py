'''
1,序列化器，序列化单个书籍对象
'''''

from serializers import BookInfoSerializer
from booktest.models import BookInfo
#1 获取书对象
book=BookInfo.objects.get(id=2)   #id=1的书籍已被删除

#2 创建器，instance，表示要序列化的对象
serializer=BookInfoSerializer(instance=book)
#3 转换数据
print(serializer.data)


'''
2,序列化器，序列化全部书籍对象
'''
from serializers import BookInfoSerializer
from booktest.models import BookInfo

#1 获取书对象
books=BookInfo.objects.all()
#2 创建器，instance，表示要序列化的对象
serializer=BookInfoSerializer(instance=books,many=True)
#3 转换数据
print(serializer.data)

'''
[
OrderedDict([('id', 2), ('btitle', '天龙八部'), ('bpub_date', '1986-07-24'), ('bread', 36), ('bcomment', 1000'is_delete', False)]),
OrderedDict([('id', 3), ('btitle', '笑傲江湖'), ('bpub_date', '1995-12-24'), ('bread',  ('bcomment', 80), ('is_delete', False)]),
OrderedDict([('id', 4), ('btitle', '雪山飞狐'), ('bpub_date', '198711'), ('bread', 58), ('bcomment', 24), ('is_delete', False)]),
OrderedDict([('id', 5), ('btitle', '三国演义'),pub_date', '1395-12-24'), ('bread', 20000), ('bcomment', 8000), ('is_delete', False)]),
OrderedDict([('id', 7), ('btitle', '水浒传'), ('bpub_date', '1390-12-24'), ('bread', 20000), ('bcomment', 80), ('is_delete', False)])
]

'''

'''
3,序列化器，序列化单个英雄对象
'''
from serializers import HeroInfoSerializer
from booktest.models import HeroInfo

#1 获取书对象
hero=HeroInfo.objects.get(id=6)
#2 创建器，instance，表示要序列化的对象
serializer=HeroInfoSerializer(instance=hero)
#3 转换数据
print(serializer.data)

'''
4,序列化器，序列化全部英雄对象
'''
from serializers import HeroInfoSerializer
from booktest.models import HeroInfo

#1 获取书对象
heros=HeroInfo.objects.all()
#2 创建器，instance，表示要序列化的对象
serializer=HeroInfoSerializer(instance=heros,many=True)
#3 转换数据
print(serializer.data)



'''
5,反序列化，书籍对象，反json
参数
'''
from serializers import BookInfoSerializer
#1,准备数据
book_dict={
    "btitle":"金瓶v2",
    "bpub_date":"1990-1-1",
    "bread":200,
    "bcomment":150
}

#2,创建序列化器，校验
serializer=BookInfoSerializer(data=book_dict)

#3,校验
serializer.is_valid(raise_exception=True)




'''
6,反序列化，书籍对象，反json
    create创建 保存
'''
from serializers import BookInfoSerializer
#1,准备数据
book_dict={
    "btitle":"金瓶v2",
    "bpub_date":"1990-1-1",
    "bread":200,
    "bcomment":150
}

#2,创建序列化器，校验
serializer=BookInfoSerializer(data=book_dict)

#3,校验
serializer.is_valid(raise_exception=True)

#4入库
serializer.save()


'''
7,反序列化，书籍对象，反json
    update 更新，修改 保存
'''
from serializers import BookInfoSerializer
from booktest.models import BookInfo
#1,准备数据
book_dict={
    "btitle":"金瓶v2",
    "bpub_date":"1990-1-1",
    "bread":200,
    "bcomment":50
}
#1.1  book实例对象，即要修改的对象
book=BookInfo.objects.get(id=4)

#2,创建序列化器，校验
serializer=BookInfoSerializer(instance=book,data=book_dict)

#3,校验
serializer.is_valid(raise_exception=True)

#4入库
serializer.save()



'''
8,自动化序列化器,测试create,update
'''
from serializers import BookInfoModelSerializer
from booktest.models import BookInfo

#1,准备数据
book_dict={
    "btitle":"完美世界",
    "bpub_date":"2016-1-1",
    "bread":200,
    "bcomment":150
}
#使用BookInfo时需要导入模型
book=BookInfo.objects.get(id=4)  #加此句为更新,下面也要加入instance=book,

#2,创建序列化器，校验
serializer=BookInfoModelSerializer(instance=book,data=book_dict)

#3,校验，未调用BookInfoSerializer中校验
serializer.is_valid(raise_exception=True)

#4入库
serializer.save()

