$(document).ready(function(){

    var url_registration = 'http://127.0.0.1:8035/reg_auth/registration/'

//---------------------------------------

    $('.slider').slick({
        infinite: true,
        dots: true,
        dotsClass: "my-dots",
        arrows: false,
        autoplay: true,
        autoplaySpeed: 5000,
        fade: true,
        speed: 1000,
        cssEasy: 'linear',
        slidesToShow: 1,
        slidesToScroll: 1
    });

//---------------------------------------

    var nav_forms = $('.nav-forms');
    var current;
    if (window.location.toString() === url_registration){
        current = $('#signup_btn').find('a');
    } else {
        current = $('#signin_btn').find('a');
    }
    var current_offset = current.offset().left;
    var current_width = current.width();
    var underline = nav_forms.find('span');

    function slider() {
        underline.css({
            left: current_offset,
            width: current_width
        });
    };

    slider();

    nav_forms.find('a').hover(
        function () {
            underline.css({
                left: $(this).offset().left,
                width: $(this).width()
            });
        },
        function () {
            slider();
        }
    );

    $(window).resize(function () {
        current_offset = current.offset().left;
        current_width = current.width();
        slider();
    });

//---------------------------------------

    var active_form;
    if (window.location.toString() === url_registration){
        active_form = false; //SIGNUP -- active
        $('.form-signin').css('display', 'none');
        $('.form-signup').css('display', 'flex');
        current.css('color', 'black');
        $('#signin_btn').find('a').css('color', 'rgb(183,181,181)');
    } else {
        active_form = true; //SIGNIN -- active
    }


    $('#signup_btn').click(function () {
        if(active_form){
            $('.form-signin').css('display', 'none');
            $('.form-signup').css('display', 'flex');
            current.css('color', 'rgb(183,181,181)');
            current = $('#signup_btn').find('a');
            current_offset = current.offset().left;
            current_width = current.width();
            slider();
            current.css('color', 'black');
            active_form = false;    //SIGNUP -- active
        }
    });

    $('#signin_btn').click(function () {
        if(!active_form){
            $('.form-signin').css('display', 'flex');
            $('.form-signup').css('display', 'none');
            current.css('color', 'rgb(183,181,181)');
            current = $('#signin_btn').find('a');
            current_offset = current.offset().left;
            current_width = current.width();
            slider();
            current.css('color', 'black');
            active_form = true;    //SIGNUP -- active
        }
    });

//---------------------------------------

    $('#in_signup_password').keyup(function () {
        $('#in_signup_password').css('border-color', 'rgb(183,181,181)');
        var value = $(this).val();
        var value_con = $('#in_signup_con_password').val();
        var validate_input = $('#signup_password_validate');
        if (value.length > 5) {
            $(this).next().css('display', 'block');
            validate_input.val('validate');
        } else {
            $(this).next().css('display', 'none');
            validate_input.val('no_validate');
        }
        if (value_con === value) {
            $('#in_signup_con_password').next().css('display', 'block');
            $('#signup_confirm_password_validate').val('validate');
        } else {
            $('#in_signup_con_password').next().css('display', 'none');
            $('#signup_confirm_password_validate').val('no_validate');
        }
    });

    $('#in_signup_con_password').keyup(function () {
        $('#in_signup_con_password').css('border-color', 'rgb(183,181,181)');
        var value_con = $(this).val();
        var value = $('#in_signup_password').val();
        var validate_input = $('#signup_confirm_password_validate');
        if (value_con === value) {
            $(this).next().css('display', 'block');
            validate_input.val('validate');
        } else {
            $(this).next().css('display', 'none');
            validate_input.val('no_validate');
        }
    });

    $('#in_signup_email').keyup(function () {
        $('#in_signup_email').css('border-color', 'rgb(183,181,181)');
        var value_email = $(this).val();
        var validate_input = $('#signup_email_validate');
        // var regexp = /^[\w.\-]{0,25}@(gmail\.com|yandex\.by|mail\.ru)$/;
        var regexp = /^[\w.\-]{0,25}@[\w\-]{1,10}\.[\w\-]{1,10}$/;
        if (regexp.test(value_email)) {
            $(this).next().css('display', 'block');
            validate_input.val('validate');
        } else {
            $(this).next().css('display', 'none');
            validate_input.val('no_validate');
        }
    });

//---------------------------------------

    var error_form = $('.nonfield li');
    $('#form_error').html(error_form.html());

//---------------------------------------

    var flag = false;
    if (window.location.toString() === url_registration){
        flag = true;  //страничка только что загружена
    }
    if (flag){
        if ($('#in_signup_email').val() != ''){
            console.log($('#in_signup_email').next().css('display'));
            $('#in_signup_email').next().css('display', 'block');
            console.log($('#in_signup_email').next().css('display'));
            $('#signup_email_validate').val('validate');
        } else {
            $('#in_signup_email').css('border-color', 'red');
        }
        if ($('#in_signup_password').val() != ''){
            $('#in_signup_password').next().css('display', 'block');
            $('#signup_password_validate').val('validate');
        } else {
            $('#in_signup_password').css('border-color', 'red');
        }
        if ($('#in_signup_con_password').val() != ''){
            $('#in_signup_con_password').next().css('display', 'block');
            $('#signup_confirm_password_validate').val('validate');
        } else {
            $('#in_signup_con_password').css('border-color', 'red');
        }
        flag = false; // код в этом if выполнится только один раз
    }


});



