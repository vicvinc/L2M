/* 
* @Author: o
* @Date:   2016-02-03 16:38:57
* @Last Modified by:   o
* @Last Modified time: 2016-02-04 19:12:04
*/

'use strict';

import { Component } from 'react';

import Header from 'component/Header';
import 'less/main.less';

class App extend Component {
	render() {
		return (
			<div>
				<Header />
			</div>
		);
	}
}

export default App;