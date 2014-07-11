'''
Created on Jun 22, 2014

@author: tli
'''

class JsonResponse(object):
  code = 200
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
    self.code = self.__class__.code
    self.content_type = self.__class__.content_type


class JsonResponseBadRequest(JsonResponse):
  code = 400
  success = False
  message = 'bad-request'


class JsonResponseUnauthorized(JsonResponse):
  code = 401
  success = False
  message = 'unauthorized'


class JsonResponseNotFound(JsonResponse):
  code = 404
  success = False
  message = 'not-found'