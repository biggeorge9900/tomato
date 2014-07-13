'''
Created on Jul 13, 2014

@author: tli
'''


class HttpResponse(object):
  status_code = 200


class HttpResponseCreated(object):
  status_code = 201


class HttpResponseAccepted(object):
  status_code = 202


class HttpResponseNonContent(object):
  status_code = 204


class HttpResponseBadRequest(object):
  status_code = 400


class HttpResponseUnauthorized(object):
  status_code = 401


class HttpResponseForbidden(object):
  status_code = 403


class HttpResponseNotFound(object):
  status_code = 404


class HttpResponseNotAllowed(object):
  status_code = 405


class HttpResponseServerError(object):
  status_code = 500


class HttpResponseNotImplemented(object):
  status_code = 501
