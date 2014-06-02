app_config = {
        'api_base': undefined
        'api_base_mapping': {
        	'localhost': ['localhost', null],
        	'tomato-prd01.appspot.com': ['potato-prd01.appspot.com', null],
        	'tomato-dev01.appspot.com': ['potato-dev01.appspot.com', null]
        }
};

function update_api_base() {
	hostname = location.hostname.toLowerCase();
	protocol = location.protocol.toLowerCase();
	port = location.port;
	mapping = app_config['api_base_mapping'][hostname];
	hostname = mapping[0]
	port = mappting[1] ? mapping[1]: port;

	app_config["api_base"] = protocal + "//" + hostname + ((":" + port) ? port else "");
};

