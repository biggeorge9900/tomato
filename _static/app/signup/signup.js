define(['durandal/app',
        'durandal/system',
        'knockout',
        'app/signup/signup_model.js'], function (app, system, ko, signup_model) {
  redirect = undefined;
    return {
      model: signup_model,
      submit: function() {
        $("html").mask({
          spinner: { lines: 10, length: 8, width: 3, radius: 10}
        });
        signup_model.save($('#signin-form'))
      },
      canSubmit: function() {
        return true;
      },
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