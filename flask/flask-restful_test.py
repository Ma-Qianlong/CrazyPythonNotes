#!/usr/bin/env python

# -*- *************** -*-
# @File  : flask-restful_test.py
# @Description : 使用flask的RESTful扩展库 flask-restful, 参考官方文档（http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html#a-minimal-api
# @Author: mql
# @Time  : 2020/5/13 16:06
# -*- *************** -*-


from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '哈哈哈'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo{} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument("task")


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(selfs, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(selfs, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task':args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


# flask-restful框架使用总结
# 这个框架用Resource类将封装好了http的各种请求，只需定义一下对应的函数即可，返回值也是可以直接丢对象过去，非常方便，写好接口类用API配置一下路径就搞定了
