$(document).ready(function(){
    email_field = $('#in_signup_email');
    password_field = $('#in_signup_password');
    con_password_field = $('#in_signup_con_password');
    email_field.val('');
    email_field.next().css('display', 'none');
    password_field.val('');
    password_field.next().css('display', 'none');
    con_password_field.val('');
    con_password_field.next().css('display', 'none');
});