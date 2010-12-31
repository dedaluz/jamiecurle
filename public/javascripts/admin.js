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
      cursorPosition = textarea[0].selectionStart
    }
    getCursorPosition = function(){
      return cursorPosition
    }
    /*
      Inject image into textarea
    */
    writeImageMarkDown = function(event, xhr){
      var r = window.editor_response
      if(r.status == 'success'){
        var markdown = "![" + r.title + "](" + r.src + ")\n\n";
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
      textarea = $(this)
      // append ui
      $(this).before(img_ui);
      // set binds for click and keypress
      $(this).bind('keypress', setCursorPosition).bind('click', setCursorPosition);
    });
  }
})(jQuery);

/*
if (uploaded_image.status == 'success'){
  image_path = "![" + uploaded_image.title + "](" + uploaded_image.src + ")\n\n";
  // now insert the return 
  //var before = textarea.val().substring(0, currentPosition);
  //var after = textarea.val().substring(currentPosition, textarea.val().length);
  //textarea.val(before + image_path + after);
  // close fancybox
  $.fancybox.close();
}

*/

/*
// cursorPosition is 0
cursorPosition = 0;
// set cursorPosition
setCursorPosition = function(el){
  // IE Support
  if (document.selection) {
      el.focus();
      var Sel = document.selection.createRange();
      var SelLength = document.selection.createRange().text.length;
      Sel.moveStart('character', -el.value.length);
      cursorPosition = Sel.text.length - SelLength;
  }
  // Firefox support
  else if (el.selectionStart || el.selectionStart == '0'){
      cursorPosition = el.selectionStart;
  }
}


getCurrentPosition = function(){
  console.log(currentPosition)
  return currentPosition;
}

setCursorPosition = function() {
    var pos = 0;
    var el = $(this).get(0);
    // IE Support
    if (document.selection) {
        el.focus();
        var Sel = document.selection.createRange();
        var SelLength = document.selection.createRange().text.length;
        Sel.moveStart('character', -el.value.length);
        pos = Sel.text.length - SelLength;
    }
    // Firefox support
    else if (el.selectionStart || el.selectionStart == '0')
        pos = el.selectionStart;

    return pos;
}


jQuery.fn.editor = function(options){
    // set up variables
    var cursorPosition, img, image_path;
    // create our "UI" elmeent
    img = $('<a>', {'href':'#'}).click(function(event){
    // cursorPosition is 0
    cursorPosition = 0;
    // set cursorPosition
    setCursorPosition = function(el){
      // IE Support
      if (document.selection) {
          el.focus();
          var Sel = document.selection.createRange();
          var SelLength = document.selection.createRange().text.length;
          Sel.moveStart('character', -el.value.length);
          cursorPosition = Sel.text.length - SelLength;
      }
      // Firefox support
      else if (el.selectionStart || el.selectionStart == '0'){
          cursorPosition = el.selectionStart;
      }
    }
    
    // load up the fancybox
    $.fancybox({
      href : '/posts/'+ $('#post_id').val() +'/blog_images/new',
      width: 400,
      height: 200,
      autoDimensions : false,
      onComplete: function(){
        // bind a function to the remotipart return
        $('#fancybox-content form').bind('ajax:complete',(function(event, xhr){
          if (uploaded_image.status == 'success'){
            image_path = "![" + uploaded_image.title + "](" + uploaded_image.src + ")\n\n";
            // now insert the return 
            //var before = textarea.val().substring(0, currentPosition);
            //var after = textarea.val().substring(currentPosition, textarea.val().length);
            //textarea.val(before + image_path + after);
            // close fancybox
            $.fancybox.close();
          }
        }))
      }
    });
    // prevent the link from doing anything
    event.preventDefault();
  }).text('+ Image')
  // now do the plugin init stuff
  return this.each(function(){
    // apend the minimal button
    $(this).before(img);
    // add events
    $(this).bind('keypress', function(){
      
      console.log(jQuery.fn.editor)
      //setCursorPosition($(this))
    }).bind('click', function(){
      //setCursorPosition($(this))
    });
  });
}
*/
$('.editor textarea').editor();