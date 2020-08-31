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

@app.route("/test/sd/data", methods=['GET', 'POST'])
def testSDdata():
    print(request.args)
    return '''{"apiVersion":"1.0.0","code":"success","message":"","requestId":"ID-daas-0-daas-headless-anyonedev-svc-cluster-local-37795-1597647990788-0-573",
                "result":[{"PROJECTUID":"（资源中心）车站商铺用电","RESULTCOUNT":43757.7},{"PROJECTUID":"（资源中心）中国电信","RESULTCOUNT":26296.4},{"PROJECTUID":"总电量","RESULTCOUNT":21792457.01},
                {"PROJECTUID":"(中铁二局工程有限公司)中山八站","RESULTCOUNT":187.2},{"PROJECTUID":"（资源中心）中国移动","RESULTCOUNT":49028.72},
                {"PROJECTUID":"（资源中心）自助设备用电","RESULTCOUNT":4323.36},{"PROJECTUID":"非运营总部办公用电","RESULTCOUNT":34565},
                {"PROJECTUID":"资源设备用电","RESULTCOUNT":381551.82},{"PROJECTUID":"（后勤中心）用电","RESULTCOUNT":25412},
                {"PROJECTUID":"（房产事业总部）单车衔接用电","RESULTCOUNT":0},{"PROJECTUID":"外单位借用电","RESULTCOUNT":320705.84},
                {"PROJECTUID":"（资源中心）PIDS用电","RESULTCOUNT":70333.12},{"PROJECTUID":"（资源中心）广告用电","RESULTCOUNT":167881.96},
                {"PROJECTUID":"照明用电","RESULTCOUNT":673939.46},{"PROJECTUID":"（房产事业总部）临时公交站场用电","RESULTCOUNT":917.28},
                {"PROJECTUID":"（中国铁塔股份有限公司）鱼珠车辆段","RESULTCOUNT":317768.88},{"PROJECTUID":"环控用电","RESULTCOUNT":7718358.6},
                {"PROJECTUID":"运营用电","RESULTCOUNT":21055634.35},{"PROJECTUID":"办公用电","RESULTCOUNT":5867.86},
                {"PROJECTUID":"牵引用电","RESULTCOUNT":12657468.43},{"PROJECTUID":"（环境公司）用电","RESULTCOUNT":3},
                {"PROJECTUID":"（房产事业总部）机动车停车场用电","RESULTCOUNT":870.48},{"PROJECTUID":"（中国邮政集团公司广州市分公司）区庄站","RESULTCOUNT":962},
                {"PROJECTUID":"（广州市荔湾区南源街市容环境卫生站）西场站","RESULTCOUNT":0},{"PROJECTUID":"（资源中心）中国联通","RESULTCOUNT":19930.56},
                {"PROJECTUID":"（广州市公交公安分局）用电","RESULTCOUNT":9150}]}'''

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
