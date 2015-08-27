/* 
* @Author: Administrator
* @Date:   2015-08-27 10:13:16
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-27 13:50:55
*/

'use strict';

var data = [
	{author: "Pete Hunt", text: "This is one comment"},
	{author: "Jordan Walke", text: "This is *another* comment"}
];

var commentList = React.createClass({
	render: function(){
		var commentNodes = this.props.data.map(function (comment) {
			return (
				<Comment author={comment.author}>
					{comment.text}
				</Comment>
			);
		});
		return (
			<div className="commentList">
				{commentNodes}
			</div>
		);
	}
});

var commentForm = React.createClass({
	handleSubmit: function(e) {
		e.preventDefault();
		var author = React.findDOMNode(this.refs.author).value.trim();
		var text = React.findDOMNode(this.refs.text).value.trim();
		if (!text || !author) {
			return;
		}
		this.props.onCommentSubmit({author: author, text: text});
		React.findDOMNode(this.refs.author).value = '';
		React.findDOMNode(this.refs.text).value = '';
		return;
	},
	render: function() {
		return (
			<form className="commentForm" onSubmit={this.handleSubmit}>
				<input type="text" placeholder="Your name" ref="author" />
				<input type="text" placeholder="Say something..." ref="text" />
				<input type="submit" value="Post" />
			</form>
		);
	}
});

var  commentBox = React.createClass({
	loadCommentsFromServer: function() {
		this.setState({data: data});
		// $.ajax({
		// 	url: this.props.url,
		// 	dataType: 'json',
		// 	cache: false,
		// 	success: function(data) {
		// 		this.setState({data: data});
		// 	}.bind(this),
		// 	error: function(xhr, status, err) {
		// 		console.error(this.props.url, status, err.toString());
		// 	}.bind(this)
		// });
	},
	handleCommentSubmit: function(comment) {
		var comments = this.state.data;
		var newComments = comments.concat([comment]);
		this.setState({data: newComments});
		this.setState({data: data});
		// $.ajax({
		// 	url: this.props.url,
		// 	dataType: 'json',
		// 	type: 'POST',
		// 	data: comment,
		// 	success: function(data) {
		// 	this.setState({data: data});
		// 	}.bind(this),
		// 	error: function(xhr, status, err) {
		// 	console.error(this.props.url, status, err.toString());
		// 	}.bind(this)
		// });
	},
	getInitialState: function() {
		return {data: []};
	},
	componentDidMount: function() {
		this.loadCommentsFromServer();
		setInterval(this.loadCommentsFromServer, this.props.pollInterval);
	},
	render: function() {
		return (
			<div className="commentBox">
				<h1>Comments</h1>
				<CommentList data={this.state.data} />
				<CommentForm onCommentSubmit={this.handleCommentSubmit} />
			</div>
		);
	}
});

var Comment = React.createClass({
	render: function() {
		return (
			<div className="comment">
				<h2 className="commentAuthor">
					{this.props.author}
				</h2>
				{this.props.children}
			</div>
		);
	}
});

React.render(
	<commentBox url="comments.json" />,
	document.getElementById('content')
);