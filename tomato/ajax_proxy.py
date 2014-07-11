'''
Created on Jul 6, 2014

@author: tli
'''

import os
import webapp2
import requests
from webapp2_extras import json


class AjaxProxy(webapp2.RequestHandler):

  exclude_headers = ['X-Gdn-Ajax-Forward-Url', 'Host']

  def get(self):
    req = self.request
    forward_host = req.headers.get('x-gdn-ajax-forward-url', None)
    if not forward_host:
      self.response.set_status(400)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.encode({'message': ('Invalud ajax proxy request: '
                                                       'x-gdn-ajax-forward-url not set.')}))
      return

    path_qs = req.path_qs
    uri =  forward_host.rstrip('/') + os.path.join('/', path_qs)

    headers = {}
    for key in [key for key in req.headers.keys() \
                if not key in AjaxProxy.exclude_headers]:
      headers.update({key: req.headers[key]})

    try:
      response = requests.get(uri, data=req.body, headers=headers)

      self.response.set_status(response.status_code)
      self.response.headers['Content-Type'] = response.headers['Content-Type']
      self.response.out.write(response.content)
    except Exception, e:
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.encode({'message': ('Exception: %s' % e)}))

  def put(self):
    pass

  def post(self):
    pass

  def delete(self):
    pass
