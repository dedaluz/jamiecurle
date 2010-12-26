
jQuery.fn.getCursorPosition = function() {
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
  // create out "UI" elmeent
  var textarea;
  var img = $('<a>', {'href':'#'}).click(function(event){
    /*
     Insert magic christmas inspired code here.
    */
    console.log(textarea.val()[currentPosition])

    var before = textarea.val().substring(0, currentPosition)
    var after = textarea.val().substring(currentPosition, textarea.val().length)
    
    textarea.val(before + "shabba" + after)
    
    
    event.preventDefault();
  }).text('blkoop')
  
  var currentPosition = 0;

  return this.each(function(){
    // set textarea
    textarea = $(this)
    // apend the minimal button
    $(this).before(img);
    
    
    
    // bind clicks and keystrokes to setting the new position.
    $(this).bind('keypress', function(){
      currentPosition = $(this).getCursorPosition()
    });
    $(this).bind('click', function(){
      currentPosition = $(this).getCursorPosition()
    });
    
  });
}

$('.editor textarea').editor();