import webapp2
from box.client import start_authenticate_v2

client_id = '0mx67p8j5a1v1dpehw794qfg0xcd3yub'

class authentication(webapp2.RequestHandler):

    def get(self):
        import sys
        print sys.path
        uri = start_authenticate_v2(client_id)
        self.redirect(uri)

class finish_authentication(webapp2.RequestHandler):

    def post(self):
        # req = self.request
        pass
