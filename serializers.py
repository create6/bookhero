'''
序列化器作用：序列化，反序列化
定义序列化器
1定义类，继承自serializer
2 和模型类字段名字，类型，字段选项一致
'''
from rest_framework import serializers
from booktest.models import BookInfo


# 1.5 自定义校验方法
def check_bpub_date(value):
    print("value=%s"%value)
    if value.year >= 2000:
        raise serializers.ValidationError("年份不能大于2000")
    return value

# 1.6 自定义校验方法  方法名要放入至字段里面
def check_bocomment(value):
    print("value=%s"%value)
    if value < 100:
        raise serializers.ValidationError("评论量太少")
    return value



#1 定义书籍器
class BookInfoSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="id",read_only=True)
    btitle =serializers.CharField(max_length=20,label="名称")
    bpub_date =serializers.DateField(label="发布日期",validators=[check_bpub_date])
    bread =serializers.IntegerField(default=0,label="阅读量")
    bcomment =serializers.IntegerField(default=0,label="评论量",validators=[check_bocomment])
    is_delete =serializers.BooleanField(default=False,label="逻辑删除")
    
    #1.2关联英雄，主键;一方序列化多方时，many=True
    # heroinfo_set=serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # heroinfo_set=serializers.StringRelatedField(read_only=True,many=True)

    #1.3,(反序列化)单字段校验：
    def validate_btitle(self,value):
        # print('value=%s'%value)
        #1.1校验value中的内容
        if "金瓶" not in value:
            raise serializers.ValidationError("书籍中不包含金瓶")
        return value
    #1.4 多字段校验：
    def validate(self, attrs):
        #1获取阅读量，评论量
        bread=attrs["bread"]
        bcomment=attrs["bcomment"]
        #2判断
        if bcomment > bread:
            raise serializers.ValidationError("评论量大于阅读量")
        return attrs
    #1.5 自定义校验方法,放在序列化器上面

    #1.6 实现create 方法  validated_data 校验成功后的数据
    def create(self, validated_data):
        #1 创建book对象，设置属性
        book=BookInfo.objects.create(**validated_data)
        #2返回
        return book







#2 定义英雄器  required=False,allow_null=True允许为空
class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES=(
        (0,"female"),
        (1,"male")
    )
    id=serializers.IntegerField(label="ID",read_only=True)
    hname=serializers.CharField(label="名字",max_length=20)
    hgender=serializers.ChoiceField(choices=GENDER_CHOICES,label="性别",required=False)
    hcomment=serializers.CharField(label="描述信息",max_length=20,required=False,allow_null=True)

    #2.2 关联书籍外键，主键e
    # hbook=serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook=serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    #2.3 关联书籍，使用模型类，__str__方法返回值,可以显示指定字段
    # hbook=serializers.StringRelatedField(read_only=True)
    #2.4 关联书籍器
    hbook=BookInfoSerializer()