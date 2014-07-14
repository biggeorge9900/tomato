app_config = {
  'api_backend': undefined,
  'api_backend_mapping': {
  'http://localhost:8080': 'http://localhost:8081',
  'https://tomato-prd01.appspot.com': 'https://potato-prd01.appspot.com',
  'https://tomato-dev01.appspot.com': 'https://potato-dev01.appspot.com'}
};

(function() {
  hostname = location.hostname.toLowerCase();
  protocol = location.protocol.toLowerCase();
  port = location.port;
  url = protocol + "//" + hostname + (port ? (":" + port) : "");

  app_config["api_backend"] = app_config['api_backend_mapping'][url];
})();
