/* 
* @Author: Administrator
* @Date:   2015-08-06 19:11:36
* @Last Modified by:   Sguar
* @Last Modified time: 2015-08-08 15:27:38
*/
//not finished!!

'use strict';

function getCookie(name) {
	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
	return r ? r[1] : undefined;
}
var _xsrf = getCookie('_xsrf');
function getTopicsHtml (topics) {
	var topicHtml = '';
	for (var i = 0, ii = topics.length; i < ii; i++) {
		topicHtml += loadTopic(topics[i]);
	};
	return topicHtml;
}
function loadTopic (topic) {
	var main = '<div class="topic-item"><div  class="avatar"><a href="/u/' + topic.author_username + '"><img src="/static/images/avatar/' + topic.author_avatar + '_sb.png" alt="' + topic.author_username + '"/></a></div>';
		main += '<div class="main"><h3 class="title"><a href="/t/' + topic.id + '#reply' + topic.reply_count + '">' + topic.title + '</a></h3>';
		main += '<div class="meta"><span class="node"><a href="/node/' + topic.node_slug + '">' + topic.node_name + '</a></span> • <span class="username"><a href="/u/' + topic.author_username + '">' + topic.author_username + '</a></span> • ';
	if( topic.last_replied_username ) {
		console.log(typeof(topic.last_replied_username));
		main += '<span class="last-touched">' + prettyDate(topic.last_touched) + '</span> • <span class="last-reply-username">最后回复来自<a href="/u/' + topic.last_replied_username + '"><strong>' + topic.last_replied_username + '</strong></a></span>';
	}else{
		main +='<span class="last-touched">' + prettyDate(topic.last_touched) + '</span>';
	}
		main += '</div>';
	if (topic.reply_count){
		console.log(topic.reply_count);
		main += '<div class="count"><a href="/t/' + topic.id + '#reply' + topic.reply_count + '">' + topic.reply_count + '</a></div>';
	}

		main += '</div></div>';
	return main;
}
function tabnav(n) {
	console.log(n);
	var data = {};
	var nodeUrl = '/node/';
		data._xsrf = getCookie('_xsrf');
	if(n) {
		console.log(n);
		nodeUrl += n;
	} else {
		return ;
		//do nothing
	}
	$.ajax({
		url: nodeUrl,
		type: 'GET',
		data: data,
		contentType: 'application/json; charset=utf-8',
		contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
		dataType:'json',
		success: function(d){
			console.log(d);
			// var topicHtml = getTopicsHtml(d.topics.list);
			var topicItem = $('.topics .ui-content').html('').html(d.html);
			// $('.topics .ui-content').html('').html(topicHtml);
			//loadTopics(d.topics.list);
		}
	});
}
function prettyDate(time){
	var date = new Date((time || "").replace(/-/g,"/").replace(/[TZ]/g," ")),
		diff = (((new Date()).getTime() - date.getTime()) / 1000),
		day_diff = Math.floor(diff / 86400);
			
	if ( isNaN(day_diff) || day_diff < 0 || day_diff >= 31 )
		return;
			
	return day_diff == 0 && (
			diff < 60 && "刚刚" ||
			diff < 120 && "一分钟以前" ||
			diff < 3600 && Math.floor( diff / 60 ) + " 分钟之前" ||
			diff < 7200 && "一小时之前" ||
			diff < 86400 && Math.floor( diff / 3600 ) + " 小时之前") ||
		day_diff == 1 && "昨天" ||
		day_diff < 7 && day_diff + " 天前" ||
		day_diff < 31 && Math.ceil( day_diff / 7 ) + " 周前";
}
$('#node_nav a').click(function () {
	//e.preventDefault()
	$('#node_nav a.active').removeClass('active');
	$(this).addClass('active');
	var node_sulg = $(this).attr('node-data');

	tabnav(node_sulg);
});