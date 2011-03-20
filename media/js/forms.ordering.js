$(function(){
    $('fieldset.orderable').each(function(){
        // set up the sortables
        $(this).sortable({
            containment: 'parent',
            placeholder: "ui-state-highlight",
            revert : 200,
            start : function(event, ui){
                $(this).find('.ui-state-highlight').css('height', ui.item.height());
            },
            update : function(event, ui){
               $(this).find('ul').each(function(i){
                   // if there is an image in the li then the field is already saved
                   // so we can update the order without triggering validation
                   // or if the file input  has somethingt
                   if ($(this).find('img').length > 0 || $(this).find('input[type="file"]').val() ){
                       $(this).find('input[name$="order"]').val(i + 1);
                   }
               });
            }
        });
        // now hide the li's containing the order
        $(this).find('input[name$="order"]').each(function(){
            $(this).parent().addClass('forms-hidden');
        });
    });
});