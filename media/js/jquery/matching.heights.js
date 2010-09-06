/*
http://nickjurista.com/prog-blog/2009/06/10/jquery-matching-column-heights-plugin/
*/

$.fn.sameheight = function(options){
    var defaults = {
        phrase : 'What are you looking for?'
    };  
    var options = $.extend(defaults, options);
    var tallest = 0;

    this.each(function() {
        if( $(this).height() > tallest){
            tallest = $(this).height();
        }
    });
    return this.each(function(){
        $(this).height(tallest);
    });
}

$.fn.localnavheight = function(options){
    var defaults = { };  
    var options = $.extend(defaults, options);
    return this.each(function(){
        $(this).height(tallest);
    });
}
