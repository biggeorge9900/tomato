
import webapp2
from .routes import routes
from .configs import configs

'''
def include_3rdpart_libs():
    # path to 3rdparty directory
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../3rdparty'))

include_3rdpart_libs()
'''

application = webapp2.WSGIApplication(routes=routes,
                                      debug=configs.get('debug', False),
                                      config=configs)
