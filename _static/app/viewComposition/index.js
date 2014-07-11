define(function() {
  return {
    canActivate : function() {
      return {
        redirect : '/login?redirect=#view-composition'
      };
    },
    propertyOne : 'This is a databound property from the root context.',
    propertyTwo : 'This property demonstrates that binding contexts flow through composed views.'
  };
});