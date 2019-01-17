from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import cgi
import json
 
TODOS = [
    {'id': 1, 'title': 'learn python'},
    {'id': 2, 'title': 'get paid'},
]
 
class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'data': TODOS}))
        return
 
    def do_POST(self):
        print(TODOS)
        new_id = len(TODOS)+1
        form = cgi.FieldStorage(fp=self.rfile,
                           headers=self.headers, environ={
                                'REQUEST_METHOD':'POST', 
                                'CONTENT_TYPE':self.headers['Content-Type']
                           })
        new_title = form['title'].value
        new_todo = {'id': new_id, 'title': new_title}
        TODOS.append(new_todo)
 
        self.send_response(201)
        self.end_headers()
        self.wfile.write(json.dumps(new_todo))
        return
 
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), RestHTTPRequestHandler)
        print(("Web Server running on port %s" % port))
        
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
