$(document).ready(function() {
    $('.overlay').fadeIn(300,
        function(){
            $('#modal_confirmation_email')
                .css('display', 'block')
                .animate({opacity: 1, top: '50%'}, 400);
		});
	});
	/* Зaкрытие мoдaльнoгo oкнa */
	$('.modal-close, .overlay').click( function(){
		$('#modal_confirmation_email')
			.animate({opacity: 0, top: '35%'}, 400,
				function(){
					$(this).css('display', 'none');
					$('.overlay').fadeOut(400);
				}
			);
});