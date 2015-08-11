'use strict';

function getCookie(name) {
	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
	return r ? r[1] : undefined;
}
function postUserInfo () {
	var saveUserInfoUrl = '/setting';
	var data = {};
	data.username = $('#username').val();
	data.email  = $('#email').val();
	data.nickname = $('#nickname').val();
	data.signature = $('#signature').val();
	data.location = $('#localtion').val();
	data.fvteam = $('#fvteam').val();
	data.weibo = $('#weibo').val();
	data.steamid = $('#steamid').val();
	data._xsrf = getCookie('_xsrf');
	$.ajax({
		url: saveUserInfoUrl,
		type: 'POST',
		data: data,
		contentType: 'application/json; charset=utf-8',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		dataType:'json',
		success: function(d){
			if(d.hasOwnProperty('msg')){
				alert(d.msg);
				//location.reload();
			}
	  	}
	})
}
$('#save_userinfo').click(function(){
	postUserInfo();
});