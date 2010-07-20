/*jslint browser: true */ /*global jQuery: true */

/**
 * jQuery Cookie plugin
 *
 * Copyright (c) 2010 Klaus Hartl (stilbuero.de)
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 */

// TODO JsDoc

/**
 * Create a cookie with the given key and value and other optional parameters.
 *
 * @example $.cookie('the_cookie', 'the_value');
 * @desc Set the value of a cookie.
 * @example $.cookie('the_cookie', 'the_value', { expires: 7, path: '/', domain: 'jquery.com', secure: true });
 * @desc Create a cookie with all available options.
 * @example $.cookie('the_cookie', 'the_value');
 * @desc Create a session cookie.
 * @example $.cookie('the_cookie', null);
 * @desc Delete a cookie by passing null as value. Keep in mind that you have to use the same path and domain
 *       used when the cookie was set.
 *
 * @param String key The key of the cookie.
 * @param String value The value of the cookie.
 * @param Object options An object literal containing key/value pairs to provide optional cookie attributes.
 * @option Number|Date expires Either an integer specifying the expiration date from now on in days or a Date object.
 *                             If a negative value is specified (e.g. a date in the past), the cookie will be deleted.
 *                             If set to null or omitted, the cookie will be a session cookie and will not be retained
 *                             when the the browser exits.
 * @option String path The value of the path atribute of the cookie (default: path of page that created the cookie).
 * @option String domain The value of the domain attribute of the cookie (default: domain of page that created the cookie).
 * @option Boolean secure If true, the secure attribute of the cookie will be set and the cookie transmission will
 *                        require a secure protocol (like HTTPS).
 * @type undefined
 *
 * @name $.cookie
 * @cat Plugins/Cookie
 * @author Klaus Hartl/klaus.hartl@stilbuero.de
 */

/**
 * Get the value of a cookie with the given key.
 *
 * @example $.cookie('the_cookie');
 * @desc Get the value of a cookie.
 *
 * @param String key The key of the cookie.
 * @return The value of the cookie.
 * @type String
 *
 * @name $.cookie
 * @cat Plugins/Cookie
 * @author Klaus Hartl/klaus.hartl@stilbuero.de
 */
jQuery.cookie = function (key, value, options) {

    // key and value given, set cookie...
    if (arguments.length > 1 && (value === null || typeof value !== "object")) {
        options = jQuery.extend({}, options);

        if (value === null) {
            options.expires = -1;
        }

        if (typeof options.expires === 'number') {
            var days = options.expires, t = options.expires = new Date();
            t.setDate(t.getDate() + days);
        }

        return (document.cookie = [
            encodeURIComponent(key), '=',
            options.raw ? String(value) : encodeURIComponent(String(value)),
            options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
            options.path ? '; path=' + options.path : '',
            options.domain ? '; domain=' + options.domain : '',
            options.secure ? '; secure' : ''
        ].join(''));
    }

    // key and possibly options given, get cookie...
    options = value || {};
    var result, decode = options.raw ? function (s) { return s; } : decodeURIComponent;
    return (result = new RegExp('(?:^|; )' + encodeURIComponent(key) + '=([^;]*)').exec(document.cookie)) ? decode(result[1]) : null;
};

$(function(){
    var GRID_STATE = 'grid';
    var GRID_HOPACITY = 'hopacity'
    var GRID_VOPACITY = 'vopacity'
    var GRID_DEFAULT_OPACITY = 0.8
    var options = { path: '/', expires: 10 };
    
    function hide_grid(){
        $('#grid-vertical, #grid-horizontal').hide();
        $('#grid-toggle a').text('grid off');
        $.cookie(GRID_STATE, 'hide', options);
    }
    
    function show_grid(){
    	$('#grid-toggle a').text('grid on');
    	$('#grid-vertical, #grid-horizontal').show();
    	$.cookie(GRID_STATE, 'show', options);
    }
    
    function do_width(){
        $('#grid-vertical, #grid-horizontal').width($(document).width() - 20)
    }
    
    function do_height(){
        $('#grid-vertical, #grid-horizontal').height($(document).height())
    }
    // height and width
    do_height();
    do_width();
    
    // if hidden when load
    if($.cookie(GRID_STATE) == 'hide'){
        hide_grid();
    }
    // now do the opacities
    
    if($.cookie(GRID_HOPACITY)){
        $('div#grid-horizontal').css({'opacity' : $.cookie(GRID_HOPACITY)})
        $('#grid-toggle input#opacity_horizontal').val($.cookie(GRID_HOPACITY))
    }else{
        $('div#grid-horizontal').css({'opacity' : GRID_DEFAULT_OPACITY})
    }
    if($.cookie(GRID_VOPACITY)){
        $('div#grid-vertical').css({'opacity' : $.cookie(GRID_VOPACITY)})
        $('#grid-toggle input#opacity_vertical').val($.cookie(GRID_VOPACITY))
    }else{
        $('div#grid-vertical').css({'opacity' : GRID_DEFAULT_OPACITY})
        
    }
    // grid toggle on click
    $('#grid-toggle a').click(function(){
        if($.cookie(GRID_STATE) == 'hide'){
            show_grid()
        }else{
            hide_grid()
        }
    });
    // opacity changes
    $('#grid-toggle input#opacity_horizontal').change(function(){
        var opacity = $(this).val()
        $.cookie(GRID_HOPACITY, opacity, options);
        $('div#grid-horizontal').css({'opacity' : opacity})
    })
    $('#grid-toggle input#opacity_vertical').change(function(){
        var opacity = $(this).val()
        $.cookie(GRID_VOPACITY, opacity, options);
        $('div#grid-vertical').css({'opacity' : opacity})
    })
    
    $(window).resize(function(){
        do_height();
        do_width();
    });
})