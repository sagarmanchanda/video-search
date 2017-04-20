'use strict';

//owl carousel


$("#select1").select2({
    minimumResultsForSearch: Infinity
});
$("#select2").select2({
    minimumResultsForSearch: Infinity
});

$("#logo-sec").owlCarousel({

    autoPlay: 3000, //Set AutoPlay to 3 seconds

    items: 6,
    itemsDesktop: [1199, 3],
    itemsDesktopSmall: [979, 3],
    afterInit: function (elem) {
        var that = this;
        that.owlControls.prependTo(elem)
    }

});


//revolution slider

$(document).ready(function () {

    $('.tp-banner').show().revolution(
        {
            dottedOverlay: "none",
            delay: 16000,
            startwidth: 1170,
            startheight: 390,
            hideThumbs: 200,

            thumbWidth: 100,
            thumbHeight: 50,
            thumbAmount: 5,

            navigationType: "bullet",
            navigationArrows: "solo",
            navigationStyle: "preview2",

            touchenabled: "on",
            onHoverStop: "on",

            swipe_velocity: 0.7,
            swipe_min_touches: 1,
            swipe_max_touches: 1,
            drag_block_vertical: false,

            parallax: "mouse",
            parallaxBgFreeze: "on",
            parallaxLevels: [7, 4, 3, 2, 5, 4, 3, 2, 1, 0],

            keyboardNavigation: "off",

            navigationHAlign: "center",
            navigationVAlign: "bottom",
            navigationHOffset: 0,
            navigationVOffset: 20,

            soloArrowLeftHalign: "left",
            soloArrowLeftValign: "center",
            soloArrowLeftHOffset: 20,
            soloArrowLeftVOffset: 0,

            soloArrowRightHalign: "right",
            soloArrowRightValign: "center",
            soloArrowRightHOffset: 20,
            soloArrowRightVOffset: 0,

            shadow: 0,
            fullWidth: "on",
            fullScreen: "off",

            spinner: "spinner4",

            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,

            shuffle: "off",

            autoHeight: "off",
            forceFullWidth: "off",


            hideThumbsOnMobile: "off",
            hideNavDelayOnMobile: 1500,
            hideBulletsOnMobile: "off",
            hideArrowsOnMobile: "off",
            hideThumbsUnderResolution: 0,

            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            startWithSlide: 0,
            videoJsPath: "rs-plugin/videojs/",
            fullScreenOffsetContainer: ""
        });

}); //ready


//gmap3

$("#test").gmap3({
    map: {
        options: {
            center: [36.4386833, -108.065073],
            zoom: 6
        }
    },
    marker:{
        values: [
            {
                address: "4800 Calhoun Rd, Houston",
                data: "4800 Calhoun Rd, Houston",
                options: {icon: "images/marker6.png"}
            },
            {
                address: "Matamoros 430, Centro, 64000 Monterrey",
                data: "Matamoros 430, Centro, 64000 Monterrey",
                options: {icon: "images/marker6.png"}
            },

            {
                address: "Ocampo 1128, Centro, 27000 Torreón, Coah., Mexico",
                data:"Ocampo 1128, Centro, 27000 Torreón, Coah., Mexico",
                options: {icon: "images/marker6.png"}
            },
            {
                address: "4901 E University Blvd, Odessa, TX 79762, United States",
                data:  "4901 E University Blvd, Odessa, TX 79762, United States",
                options: {icon: "images/marker6.png"}
            },
            {
                address: "208 E 10th St, #600, Austin, TX 78701, USA",
                data: "208 E 10th St, #600, Austin, TX 78701, USA",
                options: {icon: "images/marker6.png"}
            },

            {
                address: "Hermanos Escobar s/n, Omega, Cd Juárez, Chih., Mexico",
                data: "Hermanos Escobar s/n, Omega, Cd Juárez, Chih., Mexico",
                options: {icon: "images/marker6.png"}
            }
        ],
        options:{
            draggable: false
        },
        events:{
            mouseover: function(marker, event, context){
                var img="<img src='images/gridlist/job9.png'  width='200px' height='100px' class='img-responsive'>";
                var map = $(this).gmap3("get"),
                    infowindow = $(this).gmap3({get:{name:"infowindow"}});
                if (infowindow){
                    infowindow.open(map, marker);
                    infowindow.setContent("<div class='map-view'><p>"+context.data + "</p>"+ img+ "</div>");
                } else {
                    $(this).gmap3({
                        infowindow:{
                            anchor:marker,
                            options:{content: context.data}
                        }
                    });
                }
            },
            mouseout: function(){
                var infowindow = $(this).gmap3({get:{name:"infowindow"}});
                if (infowindow){
                    infowindow.close();
                }
            }
        }
    }
});


(function () {


    /*grid to list js*/
    $(document).ready(function () {
        $('#sa-mapview').hide();
        $('#list').on('click',function (event) {
            event.preventDefault();
            $('#grid-list > li').removeClass('col-md-4').addClass('col-md-12');
            $('#sa-mapview').hide();
            $('#grid-list').show();
            $(".portfolio-pagination").show();
        });
        $('#grid').on('click',function (event) {
            event.preventDefault();
            $('#grid-list > li').removeClass('col-md-12').addClass('col-md-4');
            $('#sa-mapview').hide();
            $('#grid-list').show();
            $(".portfolio-pagination").show();
        });
        $('#map').on('click',function (event) {
            event.preventDefault();
            $('#sa-mapview').show();
            $('#grid-list').hide();
            $(".portfolio-pagination").hide();
            var map = $("#test").gmap3('get');
            google.maps.event.trigger(map, 'resize');
            map.setZoom(map.getZoom());
            map.panToBounds(map.getBounds());
        });
    });

})();



(function () {

    var selector = '[data-rangeSlider]',
        elements = document.querySelectorAll(selector);

    // Example functionality to demonstrate a value feedback
    function valueOutput(element) {
        var value = element.value,
            output = element.parentNode.getElementsByTagName('output')[0];
        output.innerHTML = value;
    }

    for (var i = elements.length - 1; i >= 0; i--) {
        valueOutput(elements[i]);
    }

    Array.prototype.slice.call(document.querySelectorAll('input[type="range"]')).forEach(function (el) {
        el.addEventListener('input', function (e) {
            valueOutput(e.target);
        }, false);
    });


    // Basic rangeSlider initialization
    rangeSlider.create(elements, {
        min: 0,
        max: 100,
        value: 50,
        borderRadius: 3,
        buffer: 0,
        minEventInterval: 1000,

        // Callback function
        onInit: function () {
        },

        // Callback function
        onSlideStart: function (value, percent, position) {
            console.info('onSlideStart', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlide: function (value, percent, position) {
            console.log('onSlide', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlideEnd: function (value, percent, position) {
            console.warn('onSlideEnd', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        }
    });

})();

/*end*/


/*range slider*/


(function() {

    var selector = '[data-rangeSlider]',
        elements = document.querySelectorAll(selector);

    // Example functionality to demonstrate a value feedback
    function valueOutput(element) {
        var value = element.value,
            output = element.parentNode.getElementsByTagName('output')[0];
        output.innerHTML = value;
    }

    for (var i = elements.length - 1; i >= 0; i--) {
        valueOutput(elements[i]);
    }

    Array.prototype.slice.call(document.querySelectorAll('input[type="range"]')).forEach(function(el) {
        el.addEventListener('input', function(e) {
            valueOutput(e.target);
        }, false);
    });


    // Basic rangeSlider initialization
    rangeSlider.create(elements, {
        min: 0,
        max: 100,
        value: 50,
        borderRadius: 3,
        buffer: 0,
        minEventInterval: 1000,

        // Callback function
        onInit: function() {},

        // Callback function
        onSlideStart: function(value, percent, position) {
            console.info('onSlideStart', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlide: function(value, percent, position) {
            console.log('onSlide', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlideEnd: function(value, percent, position) {
            console.warn('onSlideEnd', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        }
    });

})();

/*map view items*/
$("#map-sort").hide();

if ($('#sa-mapview').css('display') == 'block'){
    $("#map-sort").show();
}

(function () {

    var selector = '[data-rangeSlider]',
        elements = document.querySelectorAll(selector);

    // Example functionality to demonstrate a value feedback
    function valueOutput(element) {
        var value = element.value,
            output = element.parentNode.getElementsByTagName('output')[0];
        output.innerHTML = value;
    }

    for (var i = elements.length - 1; i >= 0; i--) {
        valueOutput(elements[i]);
    }

    Array.prototype.slice.call(document.querySelectorAll('input[type="range"]')).forEach(function (el) {
        el.addEventListener('input', function (e) {
            valueOutput(e.target);
        }, false);
    });


    // Basic rangeSlider initialization
    rangeSlider.create(elements, {
        min: 0,
        max: 100,
        value: 50,
        borderRadius: 3,
        buffer: 0,
        minEventInterval: 1000,

        // Callback function
        onInit: function () {
        },

        // Callback function
        onSlideStart: function (value, percent, position) {
            console.info('onSlideStart', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlide: function (value, percent, position) {
            console.log('onSlide', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        },

        // Callback function
        onSlideEnd: function (value, percent, position) {
            console.warn('onSlideEnd', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
        }
    });

})();


