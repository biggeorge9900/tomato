from tomato.auth.handlers.authenticated import AuthenticatedHandler

routes = [(r'/api/signup', ''),
          (r'/api/changepwd', ''),
          (r'/api/login', ''),
          (r'/api/logout', ''),
          (r'/api/recoverpwd', ''),
          (r'/api/authenticated', AuthenticatedHandler)]
