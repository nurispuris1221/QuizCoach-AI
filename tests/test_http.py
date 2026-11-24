import unittest, threading, json
from http.server import ThreadingHTTPServer
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from app import Handler

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown(); cls.server.server_close(); cls.thread.join()
    def request(self, path, data=None):
        req = Request(self.url+path, data=None if data is None else json.dumps(data).encode(), headers={'Content-Type':'application/json'})
        with urlopen(req) as response: return response.read()
    def test_static_assets(self):
        for path in ('/', '/style.css', '/app.js'): self.assertTrue(self.request(path))
    def test_questions(self):
        questions=json.loads(self.request('/api/questions')); self.assertEqual(len(questions),5); self.assertNotIn('answer',questions[0])
    def test_full_session(self):
        choices=[0,0,2,3,0]
        for i in range(1,6):
            r=json.loads(self.request('/api/analyze',{'choices':choices[:i]})); self.assertEqual(r['answered'],i)
            if i==1: self.assertEqual(r['mdp']['action'],'Review Topic')
        self.assertEqual(r['correct_count'],3); self.assertEqual(r['mdp']['action'],'Next Question')
        self.assertEqual(json.loads(self.request('/api/analyze',{'choices':[]}))['knowledge'],.5)
    def test_invalid_request(self):
        with self.assertRaises(HTTPError) as err: self.request('/api/analyze',{'choices':[99]})
        self.assertEqual(err.exception.code,400)
