$('div.secondary nav').each(function(){
	//var nav = $(this);
	var queue = []
	$(this).find('.stale').each(function(){
		queue.push($(this));
		$(this).css({display: 'block'}).hide();
	})

	var toggler = $('<a>')
				.addClass('toggler')
				.css({display: 'block'})
				.toggle(show, hide)
				.text('Show more');


	function show(){
		var show_queue = queue.slice(0);
		while(show_queue.length > 0){
			var el = show_queue.pop();
			el.slideDown(300);
		}
		$(this).text('Show less');
	}

	function hide(){
		var hide_queue = queue.slice(0);
		while(hide_queue.length > 0){
			var el = hide_queue.pop();
			el.css({display: 'block'}).slideUp(200);
		}
		$(this).text('Show more');
	}
	$(this).find('a.stale:last').after(toggler);
});
