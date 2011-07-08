
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
            
            h1 : function(photo){
                var t = '<h1>#{title}</h1>';
                return $.tmpl(t, photo);
            },
            
            lightbox : function(context){
                var t = '<div>\
                    		<p>\
                    			<a href="" class="prev"><img src="{{MEDIA_URL}}images/prev.png"></a>\
                    			<a href="" class="next"><img src="{{MEDIA_URL}}images/next.png"></a>\
                    		</p>\
                    		<img src="#{src}">\
                    		<h1> #{title} </h1>\
                    	</div>';
                    
                var rendered = $.tmpl(t, context)
                
                return $('<div>').addClass('instagram-lightbox').html(rendered);
            }
        }
        
        // the methods that build everything
        
        _photo = function(photo){
            var context =  {
                'large' : photo['images']['standard_resolution'],
                'thumb' : photo['images']['thumbnail'],
                'caption' : photo['caption'],
                'id' : photo['id'],
                'long' : photo['longitude']
            }
            //*/
            var t = '<img src="#{thumb}" alt="#{caption}" data-large="#{large}">';
            return $.tmpl(t, context);
        }
       /*
        preload the large images so there available
       */
       _preload = function(photo){
           new Image().src = photo['images']['standard_resolution'];
       }
        /*
        On rollover on the lightbox image, show the navigation controls
        */
        _show_nav = function(){
            $(this).find('p').fadeIn(200);
        }
        _hide_nav = function (){
            $(this).find('p').fadeOut(200);
        }
        $('.instagram-lightbox div').bind({'mouseenter' : _show_nav, 'mouseleave' : _hide_nav});
        /* 
         Bind the next & prevous buttons & key presses
        */
        _previous = function(){
            console.log('previous');
        }
        _next = function(){
            console.log('next');
        }
        
        $('.instagram-lightbox a.prev').bind({'click' : _previous});
         /*
           Bind the clicks to the photos
         */
         _open = function(){
             var img = $(this).find('img');
             // src and title
             var context = {
                 src : img.attr('data-large'),
                 title : img.attr('alt')
             }
             // get the lightbox
             var lightbox = html['lightbox'](context);
             // hide the img - we'll take care of this after it's loaded
             $(lightbox).imagesLoaded(function(){
               
             });
             // hide it, append it and then fade it in
             lightbox.hide()
             $('div.content').append(lightbox)
             lightbox.show()
             
             /*
             MORNING _ WORK OUT THE URLS FOR THE MEDIA
             
             create an INIT function
             
             get rid of div.content - 
             
             get previous and next working
             
             images display on load
             
             */
         }
        $('div.instagram-photo').live('click', _open)
        
        
        /* 
        Close it
        */
        _close = function(){
            $('.instagram-lightbox').fadeOut(200);
        }
        //e.keyCode == 27
        $(document).keyup(function(e){
            if (e.keyCode == 27) {
                _close();
            }
        })
        
        /*
         The main business
        */
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
            // place the holders onto the page
            for(var i = 0; i < settings.items; i++){
                $('div.content').append($('<div/>', {'class' : 'instagram-photo loading'}).html('<div>'))
            }
            
            // load the json and build up the photos
            $.getJSON(options.jsonp, function(json) {
                data['json'] = json;
                
                $.each(data['json'], function(index, val ) {
                    if ( index == parseInt(settings.items) ){
                        return false;
                    }
                    
                    photo = $('<div/>', {'id' : json['id']}).html(_photo(val))
                    
                    data['instagrams'].push(photo);
                });
                // now insert the data
                $.each(data['instagrams'], function(){
                    // if the image is loaded
                    $(this).imagesLoaded(function(){
                        var img = $(this)
                        // hide it before insertion
                        $(this).hide();
                        // get the first div.instagram photo div that has a loader
                        // and crack in the img, then go up to the parent and animate 
                        // the opacity up passing the fade image as the callback. Finally
                        // remove the loading class
                        $('div.instagram-photo.loading div')
                            .first().append(img)
                            .parent().animate({'opacity' : 1 }, 500, function(){
                                img.fadeIn(500)
                            }).removeClass('loading');
                    })
                })
            });
        });
    };
})( jQuery );