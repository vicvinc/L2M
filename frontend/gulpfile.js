/* 
* @Author: Administrator
* @Date:   2015-08-12 19:33:21
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-19 14:53:51
*/

'use strict';

var gulp = require('gulp')
var uglify = require('gulp-uglify')
var babel = require('gulp-babel')

var minfycss = require('gulp-minify-css')
var less = require('gulp-less')

gulp.task('js', function() {
	gulp.src('src/js/*.js')
		.pipe(uglify())
		.pipe(gulp.dest('dist/js'));
});

gulp.task('less', function() {
	gulp.src('src/less/main/*.less').pipe(less()).pipe(gulp.dest('dist/css'))
})

gulp.task('dev', function () {
	gulp.watch('js/*.js', ['js', 'less']);
});

gulp.task('default', ['js', 'less', 'dev']);

