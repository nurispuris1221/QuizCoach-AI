"""Run with Python 3.10+: python app.py. No third-party dependencies."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import json
from engine import QUESTIONS, grade

ROOT = Path(__file__).resolve().parent / 'static'

class Handler(BaseHTTPRequestHandler):
    def send(self, status, data, content_type='application/json; charset=utf-8'):
        body = data if isinstance(data, bytes) else json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/api/questions':
            return self.send(200, [{k:v for k,v in q.items() if k not in ('answer','explanation')} for q in QUESTIONS])
        files = {'/': ('index.html','text/html'), '/style.css': ('style.css','text/css'), '/app.js': ('app.js','application/javascript')}
        if path in files:
            name, mime = files[path]
            return self.send(200, (ROOT / name).read_bytes(), mime+'; charset=utf-8')
        self.send(404, {'error':'Not found'})

    def do_POST(self):
        if self.path != '/api/analyze':
            return self.send(404, {'error':'Not found'})
        try:
            n = int(self.headers.get('Content-Length', '0'))
            if not 0 < n <= 4096:
                raise ValueError('Invalid request size')
            payload = json.loads(self.rfile.read(n))
            if not isinstance(payload, dict):
                raise ValueError('Expected object')
            self.send(200, grade(payload.get('choices')))
        except (ValueError, TypeError, UnicodeError) as e:
            self.send(400, {'error': str(e)})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(f'QuizCoach AI: http://127.0.0.1:{args.port}', flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
