// animovane odkazy

$(function() {
    $('ul.nav li a')
        .attr('data-href', function () { return $(this).attr('href');})
        .attr('href', '#')
        .click(function(event){
            event.preventDefault();
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.data('href')).offset().top
            }, 1000);
            window.location.hash = $anchor.data('href');
            return false;
        });
});


$(document).ready(function() {
	$(".present-button").fancybox({
		maxWidth	: '70%',
		maxHeight	: '70%',
        minWidth    : 300,
        minHeight   : 100,
		fitToView	: true,
		autoSize	: true,
		closeClick	: false,
		openEffect	: 'none',
		closeEffect	: 'fade',
        type        : 'ajax'
	});
});


// Create cookie
function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires="+date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name+"="+value+expires+"; path=/";
}

// Read cookie
function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1,c.length);
        }
        if (c.indexOf(nameEQ) === 0) {
            return c.substring(nameEQ.length,c.length);
        }
    }
    return null;
}

// Erase cookie
function eraseCookie(name) {
    createCookie(name,"",-1);
}