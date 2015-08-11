'use strict';

jQuery.postJSON = function(url, args, callback) {
    args._xsrf = getCookie("_xsrf");
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
        success: function(response) {
        callback(eval("(" + response + ")"));
    }});
};
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
function loadAvatar() {
	var hero = $('#avatar_hero option:selected').val();
	if(hero == undefined){
		//error!
		alert('unkown hero avatar choosed!');
		return;
	}
	var hgImgUrl = '/static/images/avatar/'+ hero +'_hphover.png';
	var sbImgUrl = '/static/images/avatar/'+ hero +'_sb.png';
	var loader = $('#avatar_img');
	var hgImg = $("<img />").attr('src', hgImgUrl).attr('class', 'avatar').attr('alt',hero);
	var sbImg = $("<img />").attr('src', sbImgUrl).attr('class', 'avatar').attr('alt',hero);

	loader.html('');
	hgImg.load(hgImgUrl, function() {
	    sbImg.load(sbImgUrl, function() {
	    	loader.append(hgImg).append(sbImg);
	    });
	});
}
function saveAvatar() {
	var data = {};
	data.avatar = $('#avatar_hero option:selected').val();
	data._xsrf = getCookie('_xsrf');
	var saveAvatarUrl = '/setting/avatar';
	$.post( saveAvatarUrl, data, function(d){
		if(d.hasOwnProperty('msg')){
			alert(d.msg);
			location.reload();
		}
	},'json');
}

$(function(){
	//loadAvatar();
});
$( '#avatar_hero' ).change(function() {
  	loadAvatar();
});
$( '#save_setting' ).click(function(){
	saveAvatar();
});