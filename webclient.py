##########!/usr/bin/env python
# conversion to JSON done by dumps() function


from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
import flask


users = [
  {
    "name": "Nicholas",
    "age": 42,
    "occupation": "Network Engineer"
  },
  {
    "name": "Elvin",
    "age": 32,
    "occupation": "Doctor"
  },
  {
    "name": "Jass",
    "age": 22,
    "occupation": "Web Developer"
  }
]

data = {
  "jsonrpc": "2.0",
  "method": "methodCMD",
  "params": [],
  "id": 1234
}

class User(Resource):
  def get(self, name):
    for user in users:
      if (name == user["name"]):
        return user, 200
    return "User not found", 404

  def post(self, name):
    parser = reqparse.RequestParser()
    parser.add_argument("age")
    parser.add_argument("occupation")
    args = parser.parse_args()

    for user in users:
      if (name == user["name"]):
        return "User with name {} already exists".format(name), 400

    user = {
      "name": name,
      "age": args["age"],
      "occupation": args["occupation"]
    }
    users.append(user)
    return user, 201

  def put(self, name):
    parser = reqparse.RequestParser()
    parser.add_argument("age")
    parser.add_argument("occupation")
    args = parser.parse_args()

    for user in users:
      if (name == user["name"]):
        user["age"] = args["age"]
        user["occupation"] = args["occupation"]
        return user, 200

    user = {
      "name": name,
      "age": args["age"],
      "occupation": args["occupation"]
    }
    users.append(user)
    return user, 201

  def delete(self, name):
    global users
    users = [user for user in users if user["name"] != name]
    return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)



# import jsonsocket
# from jsonsocket import Client
# import json
#
#
#
# data = {
#   "jsonrpc": "2.0",
#   "method": "methodCMD",
#   "params": [],
#   "id": 1234
# }
#
#
# host = "127.0.0.1"
# port= 18003
#
# client = Client()
# client.connect(host, port)
# data2 = json.dumps(data)
#
# # client.send(data2)
# # response = client.recv()
# # or in one line:
# response = Client().connect(host, port).send(data2).recv()
#
# print(response)


# ws = "ws://127.0.0.1:9005/"

# url = ws2
# print("url: ", url)






































#
# import websocket
# import json
# from time import sleep
#
# json_pack = {
#   "jsonrpc": "2.0",
#   "method": "methodCMD",
#   "params": [],
#   "id": 1234
# }
#
# ws = "ws://127.0.0.1:9005/"
# ws2 = "ws://127.0.0.1:18003/"
# url = ws2
# print("url: ", url)
#
# #
# # allstr99 = "POST / HTTP/1.1\r\nHost: Delia.localdomain\r\nContent-Type: application/json;charset=UTF-8\r\nUpgrade: websocket\r\nUpgrade: websocket\r\n\r\n{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"getChainInfo\",\t\t \n\t\"params\":[],\t\t\t\t \n\t\"id\":1234\n}\r\n\r\n"
#
# # p99 = bytes(allstr99,'utf-8')
# #
# # print("p99 bytes: ", p99)
#
# while True:
#   websocket.enableTrace(True)
#   ws = websocket.create_connection(url)
#   ws.send("Hello, World")
#
#
#   print("Sending json query ...")
#   ws.send(json_pack)
#   print("sending: ", json_pack)
#
#   print("Waiting for json query...")
#
#   resultb = ws.recv()
#
#   print("Result from json query: ", resultb)
#   sleep(0)
#
# # ws.close()
# #
#
# #data.encode("raw_unicode_escape")
#
#
#   # out.write("POST /path HTTP/1.1\r\n".getBytes());
#   #           out.write(("Host: localhost:" + PORT + "\r\n").getBytes());
#   #           out.write("Content-Type: application/x-www-form-urlencoded\r\n".getBytes());
#   #           out.write("Content-Length: 7\r\n".getBytes());
#
#
#
#
# #
# # wheads = ws.getheaders.__str__()
# # print("websock headers: ", wheads)
# # print("ws.handshake_response: ", ws.handshake_response)
# # print("ws.fileno: ", ws.fileno())
