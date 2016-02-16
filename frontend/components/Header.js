/* 
* @Author: o
* @Date:   2016-02-03 18:42:14
* @Last Modified by:   o
* @Last Modified time: 2016-02-16 12:55:13
*/

'use strict';

import React, { PropTypes, Component } from 'react';
import Navlist from '../api/nav.json';

class SearchInput extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: this.props.text || ''
    }
  }

  handleChange(e) {
    this.setState({text: e.target.value})
  }

  handleSubmit(e) {
    const text = e.target.value.trim();
    if (e.which === 13) {
      window.open('https://www.google.com/search?q=site:d2ark.com/' + text)
    }
  }

  render() {
    return (
      <inputWrap className="search-input">
        <input className="input"
               type="text"
               placeholder={this.props.placeholder}
               value={this.state.text}
               onChange={this.handleChange.bind(this)}
               onKeyDown={this.handleSubmit.bind(this)}/>
      </inputWrap>
    )
  }
}

SearchInput.propTypes = {
  text: PropTypes.string,
  placeholder: PropTypes.string
};
class Navmenu extends Component {
	constructor(props) {
    	super(props);
  	}
	render() {
		return (
			<li>
				<a href = {this.props.uri}>{this.props.listname}</a>
			</li>
		)
	}
}
class Nav extends Component {
	constructor() {
		super();
		this.state = {
			data: Navlist,
			count: 0
		};
	}
	handleClick(e) {
		console.log(this.state);
	}
	render() {
		return (
			<nav id='nav'>
				<div className = 'content'>
					<div className = 'navheader'>
					</div>
					<div className = 'navmenu'>
						<ul>
							{this.state.data.map((navmenu, index) => 
								<Navmenu {...navmenu} 
									key = {index}
								/>
							)}
						</ul>
					</div>
					<SearchInput placeholder="搜索新闻、比赛或人"/>
					<div className ='navuserbar'>
						<a>登入</a>
					</div>
				</div>
			</nav>
		)
	}
}
export default Nav