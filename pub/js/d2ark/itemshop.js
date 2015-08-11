/* 
* @Author: Sguar
* @Date:   2015-08-01 16:10:03
* @Last Modified by:   Sguar
* @Last Modified time: 2015-08-03 18:43:38
*/

'use strict';

function getCookie(name) {
	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
	return r ? r[1] : undefined;
}

var itemCategory = 1;
var _xsrf = getCookie('_xsrf');

function updateFilter() {
	$.post('/itemshop', {
		action: 'filter',
		category: itemCategory,
		_xsrf: _xsrf,
	}, function(data) {
		$('#shop_items').html('');
		var html = '';
		var text;
		var button_extra;
		$(data.items).each(function() {
			html += '<div class="sf-block';
			if (data.login_status == 0) {
				text = '登录购买';
				/*html += ' unbuyable';*/
				button_extra = ' disabled';
			} else if (this.cost > data.available_gold) {
				text = '金币不足';
				html += ' unbuyable';
				button_extra = ' disabled';
			} else if (data.available_slots == 0) {
				text = '物品栏已满';
				html += ' unbuyable';
				button_extra = ' disabled';
			} else {
				text = '购买';
				button_extra = ' class="buy_item" data-item-id="' + this.itemid + '"';
			}
			html += '"><div><div class="sf-item"><img src="/static/images/itemshop/' + 
						this.itemid + '.png" alt=""></div><div class="sf-cost"><div>' + 
						this.name + '</div><div><span class="goldico-bg"></span>' + 
						this.cost + '</div><button type="button"' + 
						button_extra + '>' + text + '</button></div></div></div>';
		});
		$('#shop_items').html(html);
	});
}
function updateUserInv(itemlist) {
	var sf_block = '';
	for (var i = 0, ii = itemlist.length; i < ii; i++) {
		var item = itemlist[i];
		if( item != null){
			sf_block += '<div class="sf-block"><div><div class="sf-item active">' + 
						'<img src="/static/images/itemshop/'+ item.itemid +'.png" alt="">' + 
						'</div><div class="sf-cost"><div>'+ item.name +'</div><div>' + 
						'<span class="goldico"></span>'+ item.cost +'</div>'+
						'<button type="button" class="sell_item" data-item-slot="'+ item.slot +
						'"data-item-id="'+ item.itemid +'">出售</button></div></div></div>';
		}else{
			sf_block += '<div class="sf-block"><div><div class="sf-item"></div>' +
						'<div class="sf-cost"><div></div><div></div></div></div>' + 
						'</div></div>';
		}
	}
		return sf_block;
}
$(document).ready(function() {
	$('#shop_items').on('click', '.buy_item', function() {
		var item_id = $(this).data('item-id');
		$.post('/itemshop', {
			action: 'buy_item',
			item_id: item_id,
			_xsrf: _xsrf,
		}, function(data) {
			if (data.success) {
				var new_html = updateUserInv(data.user_inv_list, data.available_gold);
				
				$('#inv_item').html('').html(new_html);
				setupInventoryBindings();
				updateFilter();
				//if (!isElementInViewport ($('#my_inventory')))
				//  $('html, body').animate({scrollTop: $("#my_inventory").offset().top}, 500);
				if ($('#dota-item-buy').get(0).play) {
					$('#dota-item-buy').get(0).currentTime = 0;
					$('#dota-item-buy').get(0).play();
				}
				$('#goldnumber').text(data.available_gold);
			} else {
				alert(data.error);
			}
		});
	});
	$('#my_inventory').on('click', '.sell_item', function() {
		var item_id = $(this).data('item-id');
		var slot = $(this).data('item-slot');
		$.post('/itemshop', {
			action: 'sell_item',
			item_id: item_id,
			slot: slot,
			_xsrf: _xsrf,
		}, function(data) {
			if (data.success) {
				//$('#my_inventory').html(data.html);
				var new_html = updateUserInv(data.user_inv_list, data.available_gold);
				
				$('#inv_item').html('').html(new_html);
				setupInventoryBindings();
				updateFilter();
				if ($('#dota-item-sell').get(0).play) {
					$('#dota-item-sell').get(0).currentTime = 0;
					$('#dota-item-sell').get(0).play();
				}
				$('#goldnumber').text(data.available_gold);
			} else {
				alert(data.error);
			}
		});
	});
	$('.itemfilter').change(function() {
		updateFilter();
	});
	// $('#itemsearchbox').keyup(function() {
	// 	updateFilter();
	// });
	// $('.itemcategory').click(function() {
	// 	$('.itemcategory').removeClass('active');
	// 	$(this).addClass('active');
	// 	itemCategory = $(this).data('category');
	// 	updateFilter();
	// });
	updateFilter();
	// setupInventoryBindings();
});

function setupInventoryBindings() {
	/*$('.sf-item.active').draggable({ distance: 10, revert: 'invalid' }).on ('dragstart', function() {
					$('.sf-cost').hide ();
					$('.goldico').hide ();
				});
			$('.sf-item').droppable ({ accept: '.sf-item.active'});*/
}

function isElementInViewport(el) {
	//special bonus for those using jQuery
	if (el instanceof jQuery) {
		el = el[0];
	}
	var rect = el.getBoundingClientRect();
	return (
		rect.top >= 0 &&
		rect.left >= 0 &&
		rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
		rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
	);
}
