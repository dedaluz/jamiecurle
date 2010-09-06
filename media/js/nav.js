$(function(){
    /* aligns navigation up with the block grid*/
    
    var block = 300;
    $('body > header nav.grid').width( (block * Math.floor($(window).width() / 300)) -10);
    $(window).resize(function(){
        $('body > header nav.grid').width( (block * Math.floor($(window).width() / 300)) -10);
    });
    /* aligns with grid & local nav */
    //console.log((block * parseInt( $(window).width() / 300)) - 10)
    $('body > header nav.grid-local').width( (block * Math.floor( ( $(window).width() + 90) / 300) - 100) - 10 );
    $(window).resize(function(){
        $('body > header nav.grid-local').width( (block * Math.floor( ( $(window).width() + 90) / 300) - 100) - 10 );
    });
});