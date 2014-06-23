$._ = (function() {
        function createCache(requestFunction) {
            var cache = {};
            return function(key, callback) {
                if ( !cache[key] ) {
                    cache[key] = $.Deferred(function(defer) {
                        requestFunction(defer, key);
                    }).promise();
                }
                return cache[key].done(callback);
            };
        }

        return {
            ajax: function(url, method, data) {
              return $.ajax({url: url,
                             async: true,
                             cache: false,
                             data: data,
                             contentType: "application/json; charset=utf-8",
                             dataType: 'json',
                             type: method ? method : 'GET'})
            },
            jsonp: function(url, method, data) {
              return $.ajax({url: url,
                             async: true,
                             cache: false,
                             data: data,
                             jsonp: 'jsonp_callback',
                             contentType: "application/json; charset=utf-8",
                             dataType: 'jsonp',
                             type: method ? method : 'GET'})
            }
        }
})();
