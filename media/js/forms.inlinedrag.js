jQuery.fn.extend({
insertAtCaret: function(myValue){
  return this.each(function(i) {
    if (document.selection) {
      this.focus();
      sel = document.selection.createRange();
      sel.text = myValue;
      this.focus();
    }
    else if (this.selectionStart || this.selectionStart == '0') {
      var startPos = this.selectionStart;
      var endPos = this.selectionEnd;
      var scrollTop = this.scrollTop;
      this.value = this.value.substring(0, startPos)+myValue+this.value.substring(endPos,this.value.length);
      this.focus();
      this.selectionStart = startPos + myValue.length;
      this.selectionEnd = startPos + myValue.length;
      this.scrollTop = scrollTop;
    } else {
      this.value += myValue;
      this.focus();
    }
  })
}
});


$(function(){
   $('fieldset.drag img').draggable({
       revert : true,
       helper : "clone",
       revertDuration: 200,
       start : function(){
           $('textarea#id_content').addClass('forms-drop-target')
       },
       stop : function(){
           $('textarea#id_content').removeClass('forms-drop-target')
       }
   });
   $('form textarea#id_content').droppable({
       drop: function(event, ui){
           $(this).insertAtCaret("\n\n" + ui.helper.parent().parent().attr('data-markdown') + "\n\n")
       }
   }); 
});