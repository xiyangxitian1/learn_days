from django.shortcuts import render

# Create your views here.

from .models import BookInfo, HeroInfo

# 操作数据库
# 1.
# book = BookInfo.objects.get(id=1)
# print("liyan", book)
# 2.
# book = BookInfo.objects.filter(btitle__contains='湖')
# 3.
# book = BookInfo.objects.filter(btitle__endswith='部')
# 4.
# book = BookInfo.objects.filter(btitle__isnull=False)
# 5.
# book = BookInfo.objects.filter(id__in=[2,4])
# 6.查询编号大于2的书籍 (id__gt, id__lt,  id__gte, id__lte)
# book = BookInfo.objects.filter(id__gt=2)
#  7.查询id不等于3的书籍
# book = BookInfo.objects.exclude(id__exact=3)
# # 8.查询1980年发布的书籍
# book = BookInfo.objects.filter(bpub_date__year='1980')
# # 9.查询1990年1月1日后发表的书籍
# book = BookInfo.objects.filter(bpub_date__gt='1990-01-01')
from datetime import date

from django.db.models import F, Q

# book = BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1))
#
# F对象: 实现两个字段之间的比较也支持运算
# 1.查询阅读量大于评论量的书籍
# book = BookInfo.objects.filter(bread__gt=F("bcomment"))
# 2.查询阅读量大于2倍评论量的书籍
# book = BookInfo.objects.filter(bread__gt=F("bcomment") * 2)

# Q对象
# 1.查询阅读量大于20，或编号小于3的图书
# book = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
# 2.查询编号不等于3的书籍
# book = BookInfo.objects.filter(~Q(id=3))

from django.db.models import Sum, Avg, Count, Max, Min

# 聚合函数
# 1.统计总的阅读量
# book = BookInfo.objects.aggregate(Sum("bread"))
# book = BookInfo.objects.count()
# 2.查询最大阅读量的书
# book = BookInfo.objects.aggregate(Max("bread"))['bread__max']
# print(book)
########################################################

# 基础关联查询
# 1.一查多：查询编号为1的图书中所有人物信息
# book = BookInfo.objects.get(id=1)
# heros = book.heroinfo_set.all()
# print(heros)
# 2.多查一：查询编号为1的英雄出自的书籍
# hero = HeroInfo.objects.get(pk=1)
# book = hero.hbook
# print(book)
# print(hero.hbook_id)
########################################################

# 关联过滤查询
# 1.多查一：查询书籍中人物的描述包含"降龙"的书籍
# book = BookInfo.objects.filter(heroinfo__hcomment__contains='降龙')
# 2.一查多：查询书名为"天龙八部"的所有人物信息
# heros = HeroInfo.objects.filter(hbook__btitle='天龙八部')
# print(heros)
