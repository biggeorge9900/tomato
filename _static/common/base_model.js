define([], function() {
  return {
    url: undefined,
    form: undefined,
    data: undefined,
    save: function(form) {
      form = form ? form : this.form
      $.ajax({
        url: this.url,
        type: 'post',
        dataType: 'json',
        data: form ? form.serialize() : data,
        success: self.on_save_success
      });
    }
  }
});