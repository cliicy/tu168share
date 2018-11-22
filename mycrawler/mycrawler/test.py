# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# import re
import sys
# sys.path.append('../mycrawler')
#
# match=re.search( r"(\d+\.?\d*)","aa123,4,567,89,3.456".replace(",",""))
# print(match.group())

import time
#
# num_dict = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五',
#             '6': '六', '7': '七', '8': '八', '9': '九'}
# money_dict = {'-2': '分', '-1': '角', '0': '元', '1': '十',
#               '2': '百', '3': '千', '4': '万', '8': '亿'}
#
#
# def trans(money):
#     money_str = []
#     dd = money[0]
#     print(dd)
#     rdd = dd[::-1]
#     print(rdd)
#     for index, value in enumerate(rdd):
#         remain = index % 4
#         if value != '0':
#             if remain != 0:
#                 money_str.insert(0, num_dict[value] + money_dict[str(remain)])
#             elif remain == 0 and (index + 1) != len(money[0]):\
#                 money_str.insert(0, money_dict[str(index)])
#             else:
#                 money_str.insert(0, num_dict[value] + money_dict[str(index)])
#     if len(money) > 1:
#         for index, value in enumerate(money[1]):
#             if index > 1:
#                 break
#             if value != 0:
#                 money_str.append(num_dict[value] + money_dict['-' + str(index + 1)])
#
#     print(''.join(money_str))
#
#
# def main():
#     input_str = '¥ 67,308,530'
#     # input_str = raw_input('Entry your money:')
#     money = input_str.split(',')
#     trans(money)
#
#
# if __name__ == '__main__':
#     main()

# import requests
#
# s = requests
#
# data={"username":"zhangsan","password":"123",}
# r = s.post('http://127.0.0.1:5000/login', data)
#
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

def mock_post():
    # import requests
    # s = requests
    # data={"username":"zhangsan","password":"123",}
    # r = s.post('http://127.0.0.1:5000/login', data)
    #
    # print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    # print(r.text)
    l1 = [1,2,3,4]
    l2 = ['a','b','c','d']
    l1.extend(l2)
    print(l1)
    print(l2)


if __name__ == '__main__':
    mock_post()
