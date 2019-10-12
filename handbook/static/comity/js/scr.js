$(document).ready(function(){


	$('header a').click(function(){
		var href = $(this).attr('href');
		var id = href.split('#').join('');			
		$('body, html').animate({
			'scrollTop' : $('#' + id).offset().top
		});
		return false;
	});
	
});


