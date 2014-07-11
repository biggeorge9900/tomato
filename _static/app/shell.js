define([ 'plugins/router' ], function(router) {

  navs = [ {
    route : [ '', 'home' ],
    moduleId : 'hello/index',
    title : 'Hello World',
    nav : true,
    hideNavbar: false,
    hideFooter: false
  }, {
    route : 'login',
    moduleId : 'login/login',
    title : 'Signin',
    nav : true,
    hideNavbar: true,
    hideFooter: true
  }, {
    route : 'signup',
    moduleId : 'signup/signup',
    title : 'Signup',
    nav : true,
    hideNavbar: true,
    hideFooter: true
  }, {
    route : 'view-composition',
    moduleId : 'viewComposition/index',
    title : 'View Composition',
    nav : true,
    hideNavbar: true,
    hideFooter: true
  } ];

  navIndex = {};
  for (var i in navs) {
    nav = navs[i];
    navIndex[nav.moduleId] = nav;
  }

  function getActiveNav() {
    actItem = router.activeItem();
    if (actItem) {
      modId = router.activeItem().__moduleId__;
      try {
        nav = navIndex[modId];
        return nav;
      } catch(e) {
        return {};
      }
    } else {
      return {};
    }
  }

  return {
    router : router,
    activate : function() {
      return router.map(navs).buildNavigationModel().mapUnknownRoutes('hello/index', 'not-found')
          .activate();
    },
    hideNavbar: function() {
      return getActiveNav().hideNavbar;
    },
    hideFooter: function() {
      return getActiveNav().hideFooter;
    }
  };
});