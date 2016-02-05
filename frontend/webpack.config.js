/* 
* @Author: Administrator
* @Date:   2015-08-25 17:25:01
* @Last Modified by:   o
* @Last Modified time: 2016-02-04 22:17:40
*/

'use strict';

var path    = require('path');
var webpack = require('webpack');

var config = {
  devtool: 'cheap-module-eval-source-map',
  entry: [
    'webpack-hot-middleware/client',
    './index'
  ],
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
    publicPath: '/pub/'
  },
  plugins: [
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  ],
  module: {

    loaders: [
    { 
      test: /\.js$/, 
      exclude: /node_modules/, 
      loader: "babel-loader",
      query: {
        presets: 'react'
      }
    }, {
      test: /\.json$/,
      loaders: ['json'],
      exclude: /node_modules/
    }, {
      test: /\.less?$/,
      loaders: ["style", "css-loader?sourceMap", "less-loader"]
    }, {
      test: /\.(png|jpg)$/,
      loader: 'url?limit=25000'
    }]
  }
};
module.exports = config;