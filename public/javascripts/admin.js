/* The editor */
(function($) {
    /*
     Options
    */
    $.fn.editor = function(options) {options = $.extend({}, options);
    /*
     Variables
    */
    var img_ui, textarea, cursorPosition, response;
    /*
     Image UI
    */
    img_ui = $('<a>', {'href':'#'}).click(function(event){
      //
      // load up the fancybox
      //
      $.fancybox({
          href : '/posts/'+ $('#post_id').val() +'/blog_images/new',
          width: 400,
          height: 200,
          autoDimensions : false,
          onComplete : function(){
            // bind write markdown
            $('#fancybox-content form').bind('ajax:complete', writeImageMarkDown)
          }
        });
        //
        // end fancybox
        //
      }).text('+ Image')
    /*
     position functions
    */
    cursorPosition = 0;
    setCursorPosition = function(el, msg){
      cursorPosition = textarea[0].selectionStart;
    }
    getCursorPosition = function(){
      return cursorPosition;
    }
    /*
      Inject image into textarea
    */
    writeImageMarkDown = function(event, xhr){
      var r = window.editor_response;
      if(r.status == 'success'){
        var markdown = "\n![" + r.title + "](" + r.src + ")";
        var cursorPos = getCursorPosition();
        var before = textarea.val().substring(0, cursorPos);
        var after = textarea.val().substring(cursorPos, textarea.val().length);
        textarea.val(before + markdown + after);
        $.fancybox.close();
      }
    }
    /*
     Main Loop
    */
    $(this).each(function() {
      // set textarea
      textarea = $(this);
      // append ui
      $(this).before(img_ui);
      // set binds for click and keypress
      $(this).bind('keypress', setCursorPosition).bind('click', setCursorPosition);
    });
  }
})(jQuery);
$('.editor textarea').editor();

/* set poster */
$('#blog_images a').click(function(event){
  // get the id of the image
  var id = $(this).attr('rel').split('-')[1];
  // get the csrf-token
  var param = $('meta[name="csrf-token"]').attr('content');
  // make the url
  var url = '/posts/' + $(this).parent().parent()[0].className;
  
  console.log(url);
  
  // send the post
  $.ajax({
    type : 'PUT',
    url : url,
    data : 'post[blog_image_id]=' + id + '&'
  })
  // remove the poster class from all  the other tags
  $(this).parent().parent().find('div').each(function(){
    $(this).find('a').removeClass('poster');
  })
  // add the poster class
  $(this).addClass('poster');
  
  
  // prevemt the default
  event.preventDefault();
});