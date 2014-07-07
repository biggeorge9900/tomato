import webapp2
from .configs import configs
from .ajax_proxy import AjaxProxy

application = webapp2.WSGIApplication(routes=[(r'/api/.*', AjaxProxy)],
                                      debug=configs.get('debug', False),
                                      config=configs)