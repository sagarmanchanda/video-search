//owl rousel

'use strict';

  $("#slider-owl-demo").owlCarousel({
 
      autoPlay: 3000, //Set AutoPlay to 3 seconds
      items : 3,
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3],
        afterInit : function(elem){
      var that = this;
      that.owlControls.prependTo(elem)
    }
 
  });

//quickview
$(".boxer").boxer();

//owl casousel
$(document).ready(function() {
 
  $("#owl-demo").owlCarousel({
 
      navigation : false,
      slideSpeed : 400,
      paginationSpeed : 400,
      singleItem:true
      
  });
 
});



//load more btn
$("#load").on('click',function() {
  $("div").removeClass('hidden');
  $(this).hide();

});

/*flickr widget start*/
$('#flikr-wdgt').jflickrfeed({
    limit: 9,
    qstrings: {
        id: '141069235@N07'
    },
    itemTemplate:
    '<li>' +
    '<a rel="colorbox" href="{{image}}" title="{{title}}">' +
    '<img src="{{image_s}}" alt="{{title}}" />' +
    '</a>' +
    '</li>'
}, function(data) {
    $('#flikr-wdgt a').colorbox();
});

/*flickr widget end*/


/*video*/

$(document).on('bind','ready',function(){

    $('#video1').videoExtend({

    });
    $('#video2').videoExtend({

    });
    $('#video3').videoExtend({

    });
    $('#video4').videoExtend({

    });
    $('#video5').videoExtend({

    });



});

/*plyr*/

$(document).ready(function(){
  plyr.setup();
});