//owl carousel

'use strict';

$("#slider-owl-demo").owlCarousel({

    autoPlay: 3000, //Set AutoPlay to 3 seconds
    items: 3,
    itemsDesktop: [1199, 3],
    itemsDesktopSmall: [979, 3],
    afterInit: function(elem) {
        var that = this;
        that.owlControls.prependTo(elem)
    }

});

//quickview
$(".boxer").boxer();

//owl casousel
$(document).ready(function() {

    $("#owl-demo").owlCarousel({

        navigation: false,
        slideSpeed: 400,
        paginationSpeed: 400,
        singleItem: true

    });

});



//load more btn
$("#load").on('click', function() {
    $("div").removeClass('hidden');
    $(this).hide();

});

/*video*/

$(document).ready(function() {
    plyr.setup();
    $(".hover-btn1").on('click', function() {

        $(".hover-btn-alt").hide();


    });
    $(".box1").on('mouseleave', function() {

        $(".hover-btn-alt").show();


    });
});
