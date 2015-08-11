/* 
* @Author: vicvinc
* @Date:   2015-08-04 20:19:24
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-05 20:38:44
*/

'use strict';
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
function postTopic (btn) {
	//after post topic success change btn to reset state
	var node_slug = $('#editor').attr('node-slug');
	var data = {};
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
				if(d.hasOwnProperty('msg')){
					alert(d.msg);
					//currently redirect the view of this topic
					var redirect_url = '/t/'+ d.topic_id;
					//$(location).attr('pathname',redirect_url);
				}
			}else if(d.error == 'form'){
				if( d.msg.content || d.msg.title ){
					alert('帖子提交失败:' + d.msg.content + d.msg.title);
				}else{
					alert('帖子提交失败:' + d.error);
				}
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
$('#submit_toptic').on('click', function(){
	var btn = $(this).button('loading');
		postTopic(btn);
});