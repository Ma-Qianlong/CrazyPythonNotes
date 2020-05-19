#!/usr/bin/env python

# -*- *************** -*-
# @File  : Flask_test.py
# @Description : hello world
# @Author: mql
# @Time  : 2020/5/13 15:11
# -*- *************** -*-


from flask import Flask

# Flask初始化参数尽量使用你的包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)


@app.route('/HelloWorld')
def hello_world():
    return "HelloWorld!"


if __name__ == "__main__":
    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(debug=True)
