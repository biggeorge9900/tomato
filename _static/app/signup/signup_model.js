define(['knockout', 'common/base_model'], function(ko, base_model){
  return $.extend(base_model, {
    url: '/api/signup',
    full_name: ko.observable(),
    email: ko.observable('tao_9900@hotmail.com'),
    password: ko.observable(),
    password_confirm: ko.observable(),
  });
});