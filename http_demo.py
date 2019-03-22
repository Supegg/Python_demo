
from http.server import HTTPServer,BaseHTTPRequestHandler  
import io,shutil,time,socketserver  
import threading


class MyThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):  
    pass  
  
class MyHttpHandler(BaseHTTPRequestHandler):  
    def do_GET(self):  
        print(time.asctime(), self.path, threading.current_thread().getName())  
        if self.path=='/':
            time.sleep(0.5)
        print(self.path)  
        r_str="Hello World";  
        enc="UTF-8"  
        encoded = ''.join(r_str).encode(enc)  
        f = io.BytesIO()  
        f.write(encoded)  
        f.seek(0)
        self.send_response(200)  
        self.send_header("Content-type", "text/html; charset=%s" % enc)  
        self.send_header("Content-Length", str(len(encoded)))  
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)  
  
    def do_POST(self):
        pass


if __name__ == '__main__':
    httpd=MyThreadingHTTPServer(('',8080), MyHttpHandler)  
    print("Server started on 127.0.0.1,port 8080.....")  
    httpd.serve_forever()  

