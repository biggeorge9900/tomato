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
            //
        }
})();
