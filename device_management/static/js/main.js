$(document).ready(function() {

	// on,off 토글버튼 - 슬라이드
    var toggle = $(".toggle_box input[type='checkbox']");
    toggle.click(function(){
        $(this).parents(".toggle_box").find("p").toggle();
    });

	// on,off 토글버튼 - 버튼
    var check = $(".custom_check input[type='checkbox']");
    check.click(function(){
        $(this).parent(".custom_check").find("span.txt_12").toggle();
    });

	// My Cart페이지 size 선택박스
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
		readURL(this);
	});


	// Select plant life stage 페이지	
	function stage_on(){
		if($('.stage_box ul li').eq(0).hasClass('on')){
			$('.stage_box .bar p').css({'width':'7%'});
		}else if($('.stage_box ul li').eq(1).hasClass('on')){
			$('.stage_box .bar p').css({'width':'31%'});
		}else if($('.stage_box ul li').eq(2).hasClass('on')){
			$('.stage_box .bar p').css({'width':'55%'});
		}else if($('.stage_box ul li').eq(3).hasClass('on')){
			$('.stage_box .bar p').css({'width':'75%'});
		}else if($('.stage_box ul li').eq(4).hasClass('on')){
			$('.stage_box .bar p').css({'width':'93%'});
		}
	}
	
	$('.stage_box .stage_up').click(function(){
		var stage = $('.stage_box ul li').length;
		var idx = $('.stage_box ul li.on').index();

		for (var i=idx; i<stage-1; i++) {
			$('.stage_box ul li').removeClass('on');
			$('.stage_box ul li').eq(idx + 1).addClass('on');
		};
		stage_on();
	});

	$('.stage_box .stage_down').click(function(){
		var idx = $('.stage_box ul li.on').index();

		for (var i=idx-1; i>=0; i--) {
			$('.stage_box ul li').removeClass('on');
			$('.stage_box ul li').eq(idx - 1).addClass('on');
		}
		stage_on();
	});

	$('.stage_box .choice_box button').click(function(){
		var idx = $('.stage_box ul li.on').index();
		var txt = $('.stage_box ul li').eq(idx).text();
		$('.stage_box .choice_box p').text(txt);
	});
	

	


});