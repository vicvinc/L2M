/* 
* @Author: Administrator
* @Date:   2015-08-25 17:25:01
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-28 14:48:32
*/

'use strict';

var __dirname = './dist/js/';
module.exports = {
	devtool: false,
	entry: './src/js/react_avatar.jsx',
	output: {
		path: __dirname,
		filename: 'bundle_react.js'
	},
	module: {
		loaders: [
			{ 
				//test: /\.css$/, loader: 'style!css' 
				test: /\.jsx$/,
				loader: 'jsx-loader'
			}
		]
	},
	resolve: {
		extensions: ['', '.js', '.jsx']
	}
};