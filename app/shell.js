define(['plugins/router'], function (router) {
    return {
        router: router,
        activate: function () {
            return router.map([
                { route: ['', 'home'],                  moduleId: 'hello/index',            title: 'Hello World',       nav: 1 },
                { route: 'view-composition',            moduleId: 'viewComposition/index',  title: 'View Composition',  nav: true }
           ]).buildNavigationModel()
              .mapUnknownRoutes('hello/index', 'not-found')
              .activate();
        }
    };
});