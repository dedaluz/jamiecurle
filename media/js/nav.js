$(function(){
    /* aligns navigation up with the block grid*/
    var block = 300;
    $('body > header nav.grid').width( (block * parseInt($(window).width() / 300)) -10);
    $(window).resize(function(){
        $('body > header nav.grid').width( (block * parseInt($(window).width() / 300)) -10);
    });
});