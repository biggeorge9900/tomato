'''
Created on Jun 21, 2014

@author: tli
'''

import os
import webapp2
from webapp2_extras import auth
from webapp2_extras import sessions
from webapp2_extras import json
from google.appengine.ext.webapp import template
import urllib2
from tomato.http.json_responses import JsonResponseUnauthorized, JsonResponse


def check_user(handler):
  """
    Decorator that checks if there's a user associated with the current session.
    Will also fail if there's no session present.
  """
  def check_login(self, *args, **kwargs):
    if self.__class__.user_required:
      auth = self.auth
      if not auth.get_user_by_session():
        self._process_response(JsonResponseUnauthorized(errorcode=1))
      else:
        return handler(self, *args, **kwargs)
    else:
      return handler(self, *args, **kwargs)

  return check_login


class BaseHandler(webapp2.RequestHandler):
  user_required = True

  @webapp2.cached_property
  def auth(self):
    """Shortcut to access the auth instance as a property."""
    return auth.get_auth()

  @webapp2.cached_property
  def user_info(self):
    """Shortcut to access a subset of the user attributes that are stored
    in the session.

    The list of attributes to store in the session is specified in
      config['webapp2_extras.auth']['user_attributes'].
    :returns
      A dictionary with most user information
    """
    return self.auth.get_user_by_session()

  @webapp2.cached_property
  def user(self):
    """Shortcut to access the current logged in user.

    Unlike user_info, it fetches information from the persistence layer and
    returns an instance of the underlying model.

    :returns
      The instance of the user model associated to the logged in user.
    """
    u = self.user_info
    return self.user_model.get_by_id(u['user_id']) if u else None

  @webapp2.cached_property
  def user_model(self):
    """Returns the implementation of the user model.

    It is consistent with config['webapp2_extras.auth']['user_model'], if set.
    """
    return self.auth.store.user_model

  @webapp2.cached_property
  def session(self):
    """Shortcut to access the current session."""
    return self.session_store.get_session(backend="datastore")

  def render_template(self, view_filename, params=None):
    if not params:
      params = {}
    user = self.user_info
    params['user'] = user
    path = os.path.join(os.path.dirname(__file__), 'gdn/views', view_filename)
    return template.render(path, params)

  # this is needed for webapp2 sessions to work
  def dispatch(self):
    self.response.headers["Access-Control-Allow-Origin"] = "*"

    # Get a session store for this request.
    self.session_store = sessions.get_store(request=self.request)

    try:
      # Dispatch the request.
      webapp2.RequestHandler.dispatch(self)
    finally:
      # Save all sessions.
      self.session_store.save_sessions(self.response)

  def _process_response(self, response):
    self.response.set_status(response.code)
    jsonp_callback = self.request.get('jsonp_callback')
    if jsonp_callback:
      self.response.headers['Content-Type'] = 'application/javascript'
      self.response.out.write("%s(%s)" %
                              (urllib2.unquote(jsonp_callback),
                               json.encode(response.obj)))
    else:
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.encode(response.obj))

  @check_user
  def get(self, *args, **kwargs):
    response = self._get_(*args, **kwargs)
    self._process_response(response)

  @check_user
  def put(self, *args, **kwargs):
    response = self._put_(*args, **kwargs)
    self._process_response(response)

  @check_user
  def post(self, *args, **kwargs):
    response = self._post_(*args, **kwargs)
    self._process_response(response)

  @check_user
  def delete(self, *args, **kwargs):
    response = self._delete_(*args, **kwargs)
    self._process_response(response)

  # enable CORS
  def options(self, *args, **kwargs):
    self.response.headers['Access-Control-Allow-Methods'] \
         = 'GET, POST, PUT, DELETE, OPTIONS'
    self.response.headers['Access-Control-Allow-Headers'] \
         = self.request.headers['Access-Control-Request-Headers']
    self.response.headers['Access-Control-Max-Age'] = '3600'
    self._process_response(JsonResponse())

  def _get_(self, *args, **kwargs):
    """
    Subclass will implement; default not allowed
    """
    self.abort(405)

  def _put_(self, *args, **kwargs):
    """
    Subclass will implement; default not allowed
    """
    self.abort(405)

  def _post_(self, *args, **kwargs):
    """
    Subclass will implement; default not allowed
    """
    self.abort(405)

  def _delete_(self, *args, **kwargs):
    """
    Subclass will implement; default not allowed
    """
    self.abort(405)
