from flask_jsonrpc.proxy import ServiceProxy

server = ServiceProxy('http://localhost:5001/api')
r=server.App.hello('su')
print(type(r),  r)


# server = ServiceProxy('http://192.168.10.12:16332')

# print(server.getblockcount())
# print(server.sendfrom(
#     "0xceac4961fe81a783516519d263efe4b614777d427b2eccebd1bdb897b705edec",
#     "AZqsqKiXfWm2YM5pcpFD5t4EDwKeyxs9y1","ANFbntHk1Ym7EPai1zRjkopjbYaWvTP6XL",100))

