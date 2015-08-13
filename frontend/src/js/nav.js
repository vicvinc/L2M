/* 
* @Author: Administrator
* @Date:   2015-08-12 17:08:16
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-13 21:24:58
*/

'use strict';
var nav = {}

nav.item = [
	{
		'mu': 'home',
		'href': '/home',
		'dis': '首页'
	},{
		'mu': 'news',
		'href': '/news',
		'dis': '新闻'
	},{
		'mu': 'forum',
		'href': '/forum',
		'dis': '社区'
	}
]
nav.controller = function(){
	return nav.item.map(function(item){
		return m('a#navMenu',{href: item.href}, item.dis);
	});
};
nav.view = function (ctrl) {
    return m('nav#navigation',[
    			m('div#navContainer',nav.controller())
    	]);
};

m.module(document.body, nav);
