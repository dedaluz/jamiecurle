$(function(){
    /* collapse any li's that do not have an error list in them*/
    //console.log($('li[title="errors"]'));
    
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
            })
        }else{
            // add the collapse class
            fieldset.addClass('collapsed');
            // slide down all of the uls - unless it's parent it error list
            lis.each(function(){
                if(! $(this).parent().hasClass('errorlist')){
                    $(this).slideDown(200);
                }
            })
        }
        // return false so we don't scoot aboot
        return false;
    });
    
    /* 
        mark ul.error as visible

    $('.collapse > ul.errors').each(function(){
        
        
        $(this).show();
        // all li's without error as a title are to hide
        $(this).find('li').each(function(){
            $(this).hide();
        });
    })
    /*
        now any lis in an ul.error nee
        
        that contain an ul.errorlist need to be shown
        but any that don't need to slide up
    */
    
});



    /*
    $(this).find('span').text('Hide');
    
    console.log($(this).parent().next())
    
    $(this).parent().next().slideDown(200);

}, function(){
    $(this).find('span').text('Show');
    
    console.log($(this).parent().next())

    $(this).parent().next().slideUp(200);

});
*/
