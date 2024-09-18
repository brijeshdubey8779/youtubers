$(document).ready(function () {
	$('.slider').slick({
		centerPadding: '60px',
		autoplay: true,
		arrows: false,
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				},
			},
			{
				breakpoint: 800,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				},
			},
		],
	});
});
$(document).ready(function () {
	$('.top').slick({
		dots: false,
		infinite: true,
		speed: 200,
		slidesToShow: 1,
		autoplay: true,
		arrows: true,
		cssEase: 'linear',
	});
});

$('.youtuber-left ').click(function () {
	$('.slider').slick('slickPrev');
});

$('.youtuber-right').click(function () {
	$('.slider').slick('slickNext');
});

$('.team-left ').click(function () {
	$('.slider').slick('slickPrev');
});

$('.team-right').click(function () {
	$('.slider').slick('slickNext');
});



// dfduui

$(document).ready(function () {
	$('.tubers').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
	});
});


$(document).ready(function () {
	$('.tubers').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		arrows: true, // Add arrows for navigation if needed
		dots: true,   // Add dots for navigation if needed
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}
		]
	});
});	