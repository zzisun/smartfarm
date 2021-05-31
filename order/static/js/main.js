$(document).ready(function() {

	// on,off 토글버튼
    var toggle = $(".toggle_box input[type='checkbox']");
    toggle.click(function(){
        $(this).parents(".toggle_box").find("p").toggle();
    });


    var check = $(".custom_check input[type='checkbox']");
    check.click(function(){
        $(this).parent(".custom_check").find("span.Roboto").toggle();
    });

    $('.select_wrap').click(function(){
        $(this).toggleClass('on');
    });


	// 데이터피커
	$("#datepicker").datepicker({
		showOn: "button",
        buttonImage: "images/ic_date.png",
        buttonImageOnly: true,
		dateFormat: 'mm / dd / yy' 
	});


    // 프로필이미지업로드
	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();
                     //console.log(reader);
			reader.onload = function(e) {
				$('.image_box').css('background-image', 'url('+e.target.result +')');
				$('.image_box').hide();
				$('.image_box').fadeIn(650);
			}
			reader.readAsDataURL(input.files[0]);
			$('.avatar_upload .avatar_preview').css({'z-index':'4'});
		}
	}	
       
	$("#file_up").change(function() {
		var image = $(this).parent('.upload_wrap').find('.image_box');
		readURL(this);
	});
});