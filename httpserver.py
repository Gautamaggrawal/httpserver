from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import re
import json

records={}

class RestHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        try:
            if None != re.search('/api/put/\d', self.path):
                global rootnode
                ctype,pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                clen,pdict = cgi.parse_header(self.headers.getheader('Content-length'))
                #print 'Content-type: ' + ctype + "\n"
                #print 'Content-length: ' + clen + "\n"

                if ctype == 'text/json' or ctype == 'application/json':
                    s = ""
                    s = self.rfile.read(int(clen))
                    #print 'READ: ' +     s
                    self.send_response(200)
                    self.end_headers()
                    data={}
                    id=int(self.path.split('/')[-1])
                    data[id]={'id':id,'name':s}
                    records.update(data)
                    self.wfile.write(json.dumps({'message': 'PUT Successfull', 'code': 200}))
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        except:
            pass
        
    def do_GET(self):
        try:
            if None != re.search('/api/get/\d', self.path):
                recordID =int(self.path.split('/')[-1])
                if records.has_key(recordID):
                    self.send_response(200)
                    self.send_header('Content-type','application/json')
                    self.end_headers()
                    print(records[recordID])
                    self.wfile.write(json.dumps(records[recordID]))
                else:
                    self.send_response(400, 'Bad Request: record does not exist')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': {'message': 'Bad Request: record does not exist', 'code': 400, 'type': 'Exception'}}))
                    
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': 'Unsupported GET request', 'code': 403, 'type': 'Exception'}}))
                
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_GET(self):
        try:
            if None != re.search('/api/list/', self.path):
                if len(records)!=0:
                    self.send_response(200)
                    self.send_header('Content-type','application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(records))
                else:
                    self.send_response(400, 'Bad Request: record does not exist')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': {'message': 'Bad Request: record does not exist', 'code': 400, 'type': 'Exception'}}))
                    
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': 'Unsupported GET request', 'code': 403, 'type': 'Exception'}}))
                
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_DELETE(self):
        try:
            if None != re.search('/api/delete/\d', self.path):
                recordID =int(self.path.split('/')[-1])
                if records.has_key(recordID):
                    self.send_response(200)
                    self.send_header('Content-type','application/json')
                    self.end_headers()
                    del records[recordID]
                    self.wfile.write(json.dumps({'message': 'Successfull', 'code': 200}))
                else:
                    self.send_response(204, 'Bad Request: record does not exist')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': {'message': 'Bad Request: record does not exist', 'code': 204, 'type': 'Exception'}}))
                    
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': 'Unsupported DELETE request', 'code': 403, 'type': 'Exception'}}))
                
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

            



def main():
    try:
        port = 8080
        server = HTTPServer(('', port), RestHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
