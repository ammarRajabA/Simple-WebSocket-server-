import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import thread

class WSHandler(tornado.websocket.WebSocketHandler):
    def handleData(self,threadName):
        while (self.opened):
            self.write_message("test")
            time.sleep(1)
    def open(self):
        print 'new connection'
        self.opened=1
        thread.start_new_thread(self.handleData,("handleData",))
    def on_message(self,message):
        print message
        self.write_message(message)
    
    def on_close(self):
        print 'connection closed'
        self.opened=0
    
    def check_origin(self,origin):
        return True
    

app=tornado.web.Application(
    [
        (r'/ws)',WSHandler)
    ]
)

if __name__=="__main__":
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
    
