from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.


def create_book(request):

    book = BookInfo.objects.create(
        name='雪中悍刀行',
        pub_date='2018-1-1',
        readcount=1000,
    )
    return HttpResponse('create')


def shop(request, city_id, shop_id):
    """
    查询字符串
    http://ip:port/path/path/?key=value&key1=value

    url 以 ? 为分隔
    ?之前是 请求路径
    ?之后是 查询字符串  类似于字典
    """
    # 获取查询字符串
    # <QueryDict: {'order': ['lalala']}>
    # QueryDict具有字典的特性 且可以一键多值
    query_parms = request.GET
    print(query_parms)

    # 当一键多值时，获取键值需要使用getlist(),否则只能得到最后一个键值
    order = query_parms.getlist('order')

    # order = query_parms.get('order')
    # order = query_parms['order']
    print(order)
    return HttpResponse('禄波的小商店')




