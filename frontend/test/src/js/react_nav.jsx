/* 
* @Author: Administrator
* @Date:   2015-08-27 14:53:34
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-27 14:58:37
*/

'use strict';

//import React from 'react';
var React = require('react');

var HelloComponent = React.createClass({
	render: function(){
		return (
			<div className='hello'>
				hello react 
			</div>
		);
	}
});
var LikeButton = React.createClass({
    getInitialState: function() {
        return {liked: false};
    },
    handleClick: function(event) {
        this.setState({liked: !this.state.liked});
    },
    render: function() {
        var text = this.state.liked ? 'like' : 'haven\'t liked';
        return (
            <button onClick={this.handleClick} title={text}>
                like
            </button>
        );
    }
});
var CommentBox = React.createClass({
	render: function() {
	return (
		<div className='commentBox'>
			Hello, world! I am a CommentBox.
		</div>
	);
  }
});

// React.render(
// 	// <CommentBox />,
// 	<LikeButton />,
// 	document.getElementById('react')
// );

var GroceryList = React.createClass({
    handleClick: function(i) {
        console.log('You clicked: ' + this.props.items[i]);
    },

    render: function() {
        return (
            <div>
                {this.props.items.map(function(item, i) {
                    return (
                        <button onClick={this.handleClick.bind(this, i)} key={i}>{item}</button>
                    );
                }, this)}
            </div>
        );
    }
});

React.render(
    <GroceryList items={['Apple', 'Banana', 'Cranberry']} />, document.getElementById('react')
);
