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