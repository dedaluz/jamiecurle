
// https://gist.github.com/797120/b7359a8ba0ab5be298875215d07819fe61f87399
// $('#content-with-images').imagesLoaded( myFunction )
// execute a callback when all images inside a parent have loaded.
// needed because .load() doesn't work on cached images

// Useful for Masonry or Isotope, triggering dynamic layout
// after images have loaded:
//    $('#content').imagesLoaded( function(){
//      $('#content').masonry();
//    });

// mit license. paul irish. 2010.
// webkit fix from Oren Solomianik. thx!

// callback function is passed the last image to load
//   as an argument, and the collection as `this`


$.fn.imagesLoaded = function(callback){
  var elems = this.find('img'),
      len   = elems.length,
      _this = this;
  
  if ( !elems.length ) {
    callback.call( this );
  }

  elems.bind('load',function(){
    if (--len <= 0){ 
      callback.call( _this ); 
    }
  }).each(function(){
    // cached images don't fire load sometimes, so we reset src.
    if (this.complete || this.complete === undefined){
      var src = this.src;
      // webkit hack from http://groups.google.com/group/jquery-dev/browse_thread/thread/eee6ab7b2da50e1f
      // data uri bypasses webkit log warning (thx doug jones)
      this.src = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";
      this.src = src;
    }  
  }); 

  return this;
};


/*
 * jQuery Simple Templates plugin 1.1.1
 *
 * http://andrew.hedges.name/tmpl/
 * http://docs.jquery.com/Plugins/Tmpl
 *
 * Copyright (c) 2008 Andrew Hedges, andrew@hedges.name
 *
 * Usage: $.tmpl('<div class="#{classname}">#{content}</div>', { 'classname' : 'my-class', 'content' : 'My content.' });
 *
 * The changes for version 1.1 were inspired by the discussion at this thread:
 *   http://groups.google.com/group/jquery-ui/browse_thread/thread/45d0f5873dad0178/0f3c684499d89ff4
 * 
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
 */

(function($) {
    $.extend({
    	// public interface: $.tmpl
    	tmpl : function(tmpl, vals) {
    		var rgxp, repr;
    		
			// default to doing no harm
			tmpl = tmpl   || '';
			vals = vals || {};
    		
    		// regular expression for matching our placeholders; e.g., #{my-cLaSs_name77}
    		rgxp = /#\{([^{}]*)}/g;
    		
    		// function to making replacements
    		repr = function (str, match) {
				return typeof vals[match] === 'string' || typeof vals[match] === 'number' ? vals[match] : str;
			};
			
			return tmpl.replace(rgxp, repr);
		}
	});
})(jQuery);

/*
jquery.instafeed.js

http://instafeed.me/jquery-plugin

Copyright (c) 2011 c&c Design Consultants LTD - http://designcc.co.uk/

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*/
(function( $ ){
    $.fn.instafeed = function(options) {
        var settings = {
            'items' : 30
        };
        // hold the variables
        var data = {
            json  : false,
            instagrams : []
        }
        // hold the various html bits and bobs
        var html = {
            
            holder : $('<div>', {'class' : 'instafeed-photos'}),
            
            loader : $('<img>', {'src' : 'http://jamiecurle.jc/images/loading.gif'}),
            
            h1 : function(photo){
                var t = '<h1>#{title}</h1>';
                return $.tmpl(t, photo);
            },
            
        }
        
        // the methods that build everything
        
        
        _photo = function(photo){
            context =  {
                'large' : photo['images']['standard_resolution'],
                'thumb' : photo['images']['thumbnail'],
                'caption' : photo['caption'],
                'id' : photo['id']
            }
            var t = '<div id="instagram_#{id}" class="instagram-photo">         \
                <img src="#{thumb}" alt="#{caption}" data-large="#{large}">     \
                <h3>#{caption}</h3>                                             \
            </div>';
            return $.tmpl(t, context);
        }
       
       _preload = function(photo){
           new Image().src = photo['images']['standard_resolution'];
       }
        
        return this.each(function(){
            // set up the options
            if ( options ) {
                $.extend( settings, options );
            }
            // if there is no feed passed then bork
            if (options.jsonp == undefined){
                throw "jquery.instafeed.js requires you pass in {'jsonp' : 'http://instafeed.me/f/myfeed.json'} when you call the plugin";
            }
            // make $(this) accessible inside the getJSON function
            var $this = $(this);
            // first things first crack in a loader
            $('div.content').append(html['loader']);
            // load the json 
            $.getJSON(options.jsonp, function(json) {
                data['json'] = json;
                $.each(data['json'], function(index, val ) {
                    if ( index == parseInt(settings.items) ){
                        return false;
                    }
                    //img = '<h2> ' + val['caption'] + '</h2><img src="' + val['images']['standard_resolution'] + '" alt="' + val['caption'] + '">';
                    
                    photo = _photo(val)
                    data['instagrams'].push(photo);
                    _preload(val)
                });
                // remove the loader
                html['loader'].remove();
                html['holder'].append(data['instagrams'].join(''));
                $('div.content').append(html['holder']);
            });
            
            
        });
    };
})( jQuery );