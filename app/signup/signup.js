define(['durandal/app', 'durandal/system', 'knockout'], function (app, system, ko) {
   redirect = undefined;
   return {
        activate: function(query) {
            //
        },
        canActivate: function() {
          //return {redirect: '/view-composition'};
          return true;
        },
        binding: function () {
            system.log('Lifecycle : binding : hello');
            return { cacheViews:false }; //cancels view caching for this module, allowing the triggering of the detached callback
        },
        bindingComplete: function () {
            system.log('Lifecycle : bindingComplete : hello');
        },
        attached: function (view, parent) {
            system.log('Lifecycle : attached : hello');
        },
        compositionComplete: function (view) {
            system.log('Lifecycle : compositionComplete : hello');
        },
        detached: function (view) {
            system.log('Lifecycle : detached : hello');
        }
    };
});