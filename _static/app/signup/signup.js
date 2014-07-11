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