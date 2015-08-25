/* 
* @Author: Administrator
* @Date:   2015-08-25 17:25:01
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-25 18:08:16
*/

'use strict';

var __dirname = './dist/js/';
module.exports = {
	entry: './src/js/nav.js',
	output: {
		path: __dirname,
		filename: 'bundle.js'
	},
	module: {
		loaders: [
			{ test: /\.css$/, loader: 'style!css' }
		]
	}
};