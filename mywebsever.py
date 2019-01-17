from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import re
import json

class LocalData(object):
  records = {}
 
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if None != re.search('/api/get/\d', self.path):
            recordID = self.path.split('/')[-1]
            if LocalData.records.has_key(recordID):
                self.send_reponse(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                self.wfile.write(json.dumps(LocalData.records[1]))
            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        return
    
        if None != re.search('/api/list/', self.path):
            if len(LocalData.records) != 0:
                self.send_reponse(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'data': LocalData.records}))
            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': 'Bad Request: record does not exist', 'code': 400, 'type': 'Exception'}}))             
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': {'message': 'Unsupported get request.', 'code': 403, 'type': 'Exception'}}))
            return

    def do_post(self):
        
        if None != re.search('/api/post/\d/\w', self.path):
            form = cgi.FieldStorage(fp=self.rfile,headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']})
            ID = self.path.split('/')[-2]
            name=self.path.split('/')[-1]
            data={}
            data[ID]={'id':ID,'name':name}
            LocalData.update(data)
            self.wfile.write(json.dumps({'message': 'Unsupported get request.', 'code': 100}))
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        return


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), HTTPRequestHandler)
        print(("Web Server running on port %s" % port))
        
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
