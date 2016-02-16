/* 
* @Author: o
* @Date:   2016-02-03 16:38:57
* @Last Modified by:   o
* @Last Modified time: 2016-02-16 11:12:21
*/

'use strict';

import React, { Component } from 'react';
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'

import Nav from '../components/Header';
import '../less/main.less';

class App extends Component {
	render() {
		return (
			<div className='app'>
				<Nav />
			</div>
		)
	}
}

export default App;