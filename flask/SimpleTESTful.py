#!/usr/bin/env python

# -*- *************** -*-
# @File  : SimpleTESTful.py
# @Description : 简单的RESTful实现
# @Author: mql
# @Time  : 2020/5/13 15:18
# -*- *************** -*-


from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据
tasks = []


@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        print(request.args)
        # data_byte = request.get_data()
        # data_str = data_byte.decode()
        # data_dict = json.loads(data_str)
        # print(data_str)

        a = filter(lambda x: x % 2 == 0, range(10))
        # print(a) # python2 打印列表
        print(list(a)) # python3 打印列表

        task_id = request.args.get("id")
        taskF = filter(lambda t: t['id'] == int(task_id), tasks)
        task = list(taskF)
        print(task)
        return jsonify(task) if task else jsonify({'result': 'not found'})

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('请求方式为------->', request.method)
    args = request.args.get("name") # 获取  get  参数
    form = request.form.get('data') # 获取  post 参数
    # main(form)   # 调用我们的逻辑函数
    # get_html(form)
    print("=========成功 生成 index.html================")
    return jsonify(args=args, form=form)


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
