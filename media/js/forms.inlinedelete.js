$(function(){
    $('.collapsable-inline').find('input[name$="DELETE"]').each(function(){
        // add the forms-delete class
        $(this).parent().addClass('forms-delete');
        // if the inputs that are not hidden all have no values, then
        // give the delete field a forms-hidden class
            if(! $(this).parent().parent().hasClass('forms-no-delete') ){
               $(this).parent().addClass('forms-hidden');
            }
        
    }).click(function(){
        // change the background-color if box is checked
        if($(this).is(':checked')){
            $(this).parent().parent().addClass('forms-marked-for-deletion')
        }else{
           $(this).parent().parent().removeClass('forms-marked-for-deletion')
        }
    })
});