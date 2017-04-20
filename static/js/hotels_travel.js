'use strict';


$.material.init();

//owl carousel
$("#logo-sec").owlCarousel({

    autoPlay: 3000, //Set AutoPlay to 3 seconds

    items : 6,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3],
    afterInit : function(elem){
        var that = this;
        that.owlControls.prependTo(elem)
    }

});

// featured offers slider

$("#offers-slider").owlCarousel({

    autoPlay: 3000, //Set AutoPlay to 3 seconds

    items : 4,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3],
    afterInit : function(elem){
        var that = this;
        that.owlControls.prependTo(elem)
    }

});

//gmap3
$("#test").gmap3({
    map:{
        options:{
            center:[-37.7681102,144.8378658],
            zoom: 8
        }
    },
    marker:{
        values:[
            {address:"melbourne,australia",
                options:{icon: "images/marker8.png"}}
        ]
    }
});


// camera slider js code


jQuery(function(){

    jQuery('#camera_wrap_3').camera({
        height: '56%',
        pagination: false,
        thumbnails: true,
        imagePath: '../images/'
    });

});

//tabs

$('.nav-tabs li:eq(0) a').tab('show');

//upper and down icon
function toggleChevron(e) {
    $(e.target)
        .prev('.panel-heading')
        .find("i.indicator")
        .toggleClass('mdi-hardware-keyboard-arrow-down mdi-hardware-keyboard-arrow-up');
}
$('#accordion').on('hidden.bs.collapse', toggleChevron);
$('#accordion').on('shown.bs.collapse', toggleChevron);