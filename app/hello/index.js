define(['durandal/app', 'durandal/system', 'knockout'], function (app, system, ko) {
    var name = ko.observable('' + app_config['api_base']);
    var canSayHello = ko.computed(function () {
      return name() ? true : false;
    });

    return {
        displayName: 'What is your name?',
        name: name,
        sayHello: function() {
          app.showMessage('Hello ' + name() + '!', 'Greetings');
        },
        canSayHello: canSayHello,
        activate: function() {
          console.log('Lifecycle : activate : hello');
        },
        canActivate: function() {
          return {redirect: '/login?redirect=#home'};
        },
        binding: function () {
          console.log('Lifecycle : binding : hello');
            return { cacheViews:false }; //cancels view caching for this module, allowing the triggering of the detached callback
        },
        bindingComplete: function () {
          console.log('Lifecycle : bindingComplete : hello');
        },
        attached: function (view, parent) {
          console.log('Lifecycle : attached : hello');
        },
        compositionComplete: function (view) {
          console.log('Lifecycle : compositionComplete : hello');
        },
        detached: function (view) {
          console.log('Lifecycle : detached : hello');
        }
    };
});