requirejs.config({
    paths: {
        'text': '../lib/require/text',
        'durandal':'../lib/durandal/js',
        'plugins' : '../lib/durandal/js/plugins',
        'transitions' : '../lib/durandal/js/transitions',
        'knockout': '../lib/knockout/knockout-2.3.0',
        'bootstrap': '../lib/bootstrap/js/bootstrap',
        'jquery': '../lib/jquery/jquery-1.9.1',
        'loadmask': '../lib/spinner/jquery.loadmask.spin',
        'common': '../common'
    },
    shim: {
      'bootstrap': {
        deps: ['jquery'],
        exports: 'jQuery'
      },
      'common/overrides': {
        deps: ['jquery', 'bootstrap']
      },
      'spin': {
        deps: ['jquery']
      },
      'loadmask': {
        deps: ['jquery']
      }
    }
});

define(['durandal/system',
        'durandal/app',
        'durandal/viewLocator',
        'common/overrides',
        'loadmask'],
       function (system, app, viewLocator) {
    //>>excludeStart("build", true);
    system.debug(true);
    //>>excludeEnd("build");

    app.title = 'Potato';

    //specify which plugins to install and their configuration
    app.configurePlugins({
        router:true,
        dialog: true,
        widget: {
            kinds: ['expander']
        }
    });

    app.start().then(function () {
        //Replace 'viewmodels' in the moduleId with 'views' to locate the view.
        //Look for partial views in a 'views' folder in the root.
        viewLocator.useConvention();

        //Show the app by setting the root view model for our application.
        app.setRoot('shell');
    });
});