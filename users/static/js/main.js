$(document).ready(function() {

    var toggle = $(".toggle_box input[type='checkbox']");
    toggle.click(function(){
        $(this).parents(".toggle_box").find("p").toggle();
    });


    var check = $(".custom_check input[type='checkbox']");
    check.click(function(){
        $(this).parent(".custom_check").find("span.Roboto").toggle();
    });


});