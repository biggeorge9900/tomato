'''
Created on Jun 22, 2014

@author: tli
'''
from tomato.http.http_responses import HttpResponse, \
                                       HttpResponseBadRequest,\
                                       HttpResponseUnauthorized, \
                                       HttpResponseNotFound


class JsonResponse(HttpResponse):
  content_type = 'application/json'
  obj = {}
  success = True
  message = ''
  errorcode = 0

  def __init__(self, *args, **kwargs):
    if len(args) <= 1 and len(kwargs) == 0:
      data = {'message': args[0] if len(args) > 0 else ''}
    elif len(args) == 0 and len(kwargs) > 0:
      data = dict(**kwargs)
    else:
      raise Exception('Invalid JsonResponse arguments')

    if 'success' not in data.keys():
      data.update({'success': self.__class__.success})
    if 'message' not in data.keys():
      data.update({'message': self.__class__.message})
    if 'errorcode' not in data.keys():
      data.update({'errorcode': self.__class__.errorcode})

    self.obj = data
    self.status_code = self.__class__.status_code
    self.content_type = self.__class__.content_type


class JsonResponseBadRequest(HttpResponseBadRequest):
  success = False
  message = 'bad-request'


class JsonResponseUnauthorized(HttpResponseUnauthorized):
  success = False
  message = 'unauthorized'


class JsonResponseNotFound(HttpResponseNotFound):
  success = False
  message = 'not-found'
