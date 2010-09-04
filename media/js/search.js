$(function(){
    $('header form input[name="q"], header form button, header form ul').hover(function(){
        $('header form ul').show()
    }, function(){
        $('header form ul').hide()
    })
})