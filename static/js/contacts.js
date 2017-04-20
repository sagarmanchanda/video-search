'use strict';

//gmap3
$("#test").gmap3({
    map: {
        options: {
            center: [-37.7681102, 144.8378658],
            zoom: 8
        }
    },
    marker: {
        values: [{
            address: "melbourne,australia",
            options: { icon: "images/marker.png" }
        }]
    }
});


/* ==========================================================================
 Tweet
 ========================================================================== */

$('#contact_form').bootstrapValidator({
    fields: {
        first_name: {
            validators: {
                notEmpty: {
                    message: 'The first name is required'
                }
            }
        },
        last_name: {
            validators: {
                notEmpty: {
                    message: 'The last name is required'
                }
            }
        },
        email: {
            validators: {
                notEmpty: {
                    message: 'The email is required'
                },
                emailAddress: {
                    message: 'The input is not a valid email address'
                }
            }
        },
        subject: {
            validators: {
                notEmpty: {
                    message: 'The subject is required'
                }
            }
        },
        message: {
            validators: {
                notEmpty: {
                    message: 'The message is required'
                }
            }
        }

    }
});
