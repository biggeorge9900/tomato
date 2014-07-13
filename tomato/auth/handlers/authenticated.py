'''
Created on Jun 22, 2014

@author: tli
'''
from tomato.http.base_handler import BaseHandler
from tomato.http.json_responses import JsonResponse


class AuthenticatedHandler(BaseHandler):
  '''
  '''

  user_required = False

  def _get_(self):
    return JsonResponse(errorcode=0,
                        message='logged-in',
                        req_data=self.request.get('data'),
                        user_info=self.user_info)

  def _post_(self):
    return JsonResponse(errorcode=0,
                        message='logged-in',
                        req_data=self.request.get('data'),
                        user_info=self.user_info)

  def _put_(self):
    return JsonResponse(errorcode=0,
                        message='logged-in',
                        req_data=self.request.get('data'),
                        user_info=self.user_info)
