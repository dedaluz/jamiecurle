$(function(){
    /* collapses the uls inside of a fieldset.collapse */
    $('.collapsable a').click(function(){
        var fieldset = $(this).parent().parent();
        var lis = fieldset.find('li:not([title])');
        // collapse all of the ul's
        if(fieldset.hasClass('collapsed')){
            // remove the collapsed class
            fieldset.removeClass('collapsed');
            // slide them up
            lis.each(function(){
                if(! $(this).parent().hasClass('errorlist')){
                    $(this).slideUp(200);
                }
            });
        }else{
            // add the collapse class
            fieldset.addClass('collapsed');
            // slide down all of the uls - unless it's parent it error list
            lis.each(function(){
                if(! $(this).parent().hasClass('errorlist')){
                    $(this).slideDown(200);
                }
            });
        }
        // return false so we don't scoot aboot
        return false;
    });
});
