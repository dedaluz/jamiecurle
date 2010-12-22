$(function(){
  $('body#post article.editable div.body').editable( window.location, { 
        indicator : "<img src='/images/indicator.gif'>",
        loadurl   :  window.location + '/edit/',
        type      : "textarea",
        submit    : "OK",
        event     : "dblclick",
        cancel    : "Cancel",
        method    : "PUT",
        tooltip   : "Click to edit..."
    });
});
