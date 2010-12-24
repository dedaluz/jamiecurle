
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
  var img = $('<a>', {'href':'#'}).click(function(event){
    /*
     Insert magic christmas inspired code here.
    */
    console.log(currentPosition);
    event.preventDefault();
  }).text('blkoop')
  
  var currentPosition = 0;

  return this.each(function(){
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