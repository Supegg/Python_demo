import base64
import io

with open('./media/bitcoin.png','rb') as f:
    base64_data = base64.b64encode(f.read())
    print(type(base64_data))

with open('./media/bitcoin.html','w') as f2:
    f2.write(f'<img src = \"data:image/jpg;base64,{base64_data.decode("ascii")}\" />')
