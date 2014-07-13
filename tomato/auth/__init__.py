from tomato.auth.handlers.authenticated import AuthenticatedHandler
from tomato.auth.handlers.signup import SignupHandler

routes = [(r'/api/signup', SignupHandler),
          (r'/api/changepwd', ''),
          (r'/api/login', ''),
          (r'/api/logout', ''),
          (r'/api/recoverpwd', ''),
          (r'/api/authenticated', AuthenticatedHandler)]
