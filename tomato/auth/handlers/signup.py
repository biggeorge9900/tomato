'''
Created on Jun 22, 2014

@author: tli
'''
from tomato.http.base_handler import BaseHandler
from tomato.http.json_responses import JsonResponseBadRequest, JsonResponse
from tomato.const.auth import SIGNUP_CONFIRM_PASSWORD_FAIL, \
                              SIGNUP_DUP_EMAIL,\
                              SIGNUP_SUCCESS_TPL


class SignupHandler(BaseHandler):

  user_required = False

  def _post_(self):
    full_name = self.request.get('full_name')
    email = self.request.get('email')
    password = self.request.get('password')
    confirm_password = self.request.get('confirm_password')

    if password != confirm_password:
      return JsonResponseBadRequest(SIGNUP_CONFIRM_PASSWORD_FAIL)

    unique_properties = ['email_address']
    user_data = self.user_model.create_user(email,
      unique_properties,
      email_address=email,
      name=full_name,
      password_raw=password,
      verified=False)

    if not user_data[0]:  # user_data is a tuple
      return JsonResponseBadRequest(SIGNUP_DUP_EMAIL)

    '''
    user = user_data[1]
    user_id = user.get_id()
    token = self.user_model.create_signup_token(user_id)
    verification_url = self.uri_for('verification', type='v', user_id=user_id,
      signup_token=token, _full=True)
    msg = 'Send an email to user in order to verify their address. \
          They will be able to do so by visiting <a href="{url}">{url}</a>'

    self.display_message(msg.format(url=verification_url))
    '''

    return JsonResponse(self.render_template(SIGNUP_SUCCESS_TPL))
