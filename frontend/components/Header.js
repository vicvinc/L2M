/* 
* @Author: o
* @Date:   2016-02-03 18:42:14
* @Last Modified by:   o
* @Last Modified time: 2016-02-04 17:43:51
*/

'use strict';

import { Component } from 'react';

class Header extend Component {
	handleClick(e) {
		console.log('nav menu onClicked ');
	}

	render() {
		<nav id='nav' class='nav' onClick={this.handleClick.bind(this)}>
			<div class='navheader'>
				<div class='header-logo'>
				</div>
			</div>
			<div class='navmenu'>
				<ul>
					<li>导航</li>
					<li>导航</li>
					<li>导航</li>
					<li>导航</li>
				<ul>
			</div>
			<div class='navuserbar'>
				<div class='userstatus'>
				</div>
			</div>
		</nav>
	}

}