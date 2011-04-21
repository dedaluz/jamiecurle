$(function(){
    $('.collapsable-inline a').click(function(){
        // if 
        uls = $(this).parent().parent().find('ul.inline:not("ul.errors")').each(function(){
            if($(this).hasClass('collapsed')){
                $(this).removeClass('collapsed').slideUp(200);
            }else{
                $(this).addClass('collapsed').slideDown(200);
            }
        })
        return false;
    });
})