#!/usr/bin/env python

# -*- *************** -*-
# @File  : DataToRomaRESTful.py
# @Description :
# @Author: mql
# @Time  : 2020/5/13 16:37
# -*- *************** -*-


from flask import Flask
from flask_restful import Api, reqparse, abort, Resource, request
from flask_cors import *
from RandomDataToRoma import manyTagDataToMySQL2 as d2db
import time
import re

p=re.compile(r'[-,$()#+&*]')

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域
api = Api(app)

def abort_if_param_doesnt_exist(args):
    if False:
        abort(404, message="the requirted param is empty")


# parser = reqparse.RequestParser()
# parser.add_argument("tagnames")

# parser = reqparse.RequestParser
# parser.add_argument()
# parser.add_argument("tagnames")
# parser.add_argument('sT')
# parser.add_argument('eT')
# parser.add_argument('min')
# parser.add_argument('max')


class DoDataToMySQL(Resource):
    def post(self):
        # args = parser.parse_args()
        args = request.json
        print("请求了向MySQL历史数据库模拟数据：" + str(args))
        tagnames = str(args["tagnames"]).replace("#", "_")
        # tagnames = re.sub(re.compile(r'[#]'), "_", args["tagnames"])
        print(tagnames)
        # print(re.sub(re.compile(r'[#]'), '_', "test#test"))
        # print("test#test".replace("#", "_"))
        try:
            d2db(tagnames=tagnames, sTime=args["sT"], eTime=args["eT"],
                 minVal=float(args["min"]) if 'min' in args else 0,
                 maxVal=float(args["max"]) if 'max' in args else 255,
                 isFixedVal=args["isFixedVal"] if 'isFixedVal' in args else 'no',
                 host=args["host"] if 'host' in args else '192.168.5.249',
                 port=int(args["port"]) if 'port' in args else 3136,
                 user=args["user"] if 'user' in args else "root",
                 password=args["password"] if 'password' in args else "root",
                 database=args["database"] if 'database' in args else 'db-deepctrls-cecep-roma')
            print("当前进程使用CPU时间(ms): %f" % (time.process_time_ns() / 1000000))
        except Exception as e:
            print(type(e.args))
            print(e.args)
            return {'success': False, 'msg': e.args[0]}, 201
        else:
            return {'success': True, 'msg': '模拟MySQL历史数据完成！'}, 201




##
## Actually setup the Api resource routing here
##
api.add_resource(DoDataToMySQL, '/data2mysql')

if __name__ == '__main__':
    app.run(debug=True)
