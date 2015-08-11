/* 
* @Author: Sguar
* @Date:   2015-08-04 22:52:09
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-05 20:38:42
*/

'use strict';
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
function postTopic (btn) {
	var node_slug = $('#editor').attr('node-slug');
	var data = {};
		data.tid = $('#tid').val();
		data.title = $('#topic_title').val();
		data.content = simplemde.value();
		data._xsrf = getCookie('_xsrf');

	$.ajax({
		url: node_slug,
		type: 'POST',
		data: data,
		contentType: 'application/json; charset=utf-8',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		dataType:'json',
		success: function(d){
			btn.button('reset');
			if(d.success) {
				alert('修改成功');
				if(d.hasOwnProperty('msg')){
					//redirect_url = '/t/'+d.msg;
					//$(location).attr('pathname',redirect_url);
				}
			}else{
				if( d.error == 'form')
					var alert_msg = '修改失败，请稍后再提交:';
					for(x in d.msg) {
						alert_msg += x;
					}
					alert( alert_msg );
			}
	  	}
	})
}

var simplemde = new SimpleMDE({
	element: $('#editor')[0],
	spellChecker: false,
	status: true,
	status: ['submit', 'autosave', 'lines', 'words', 'cursor'],
});
simplemde.render();
$('#submit_toptic').click(function(){
	var btn = $(this).button('loading');
    	postTopic(btn);
});