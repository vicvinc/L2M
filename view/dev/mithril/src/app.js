/* 
* @Author: Administrator
* @Date:   2015-08-12 15:47:12
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-12 17:08:09
*/

'use strict';

var Contact = function(data) {
	data = data || {}
	this.id = m.prop(data.id)
	this.name = m.prop(data.name)
	this.email = m.prop(data.email)
}
Contact.list = function(data) {
	return m.request({method: "GET", url: "http://localhost:9541", data: data})
}
Contact.save = function(data) {
	return m.request({method: "POST", url: "http://localhost:9541", data: data})
}

var Observable = function() {
	var channels = {}
	return {
		register: function(subscriptions, controller) {
			return function self() {
				var ctrl = new controller
				var reload = controller.bind(ctrl)
				Observable.on(subscriptions, reload)
				ctrl.onunload = function() {
					Observable.off(reload)
				}
				return ctrl
			}
		},
		on: function(subscriptions, callback) {
			subscriptions.forEach(function(subscription) {
				if (!channels[subscription]) channels[subscription] = []
				channels[subscription].push(callback)
			})
		},
		off: function(callback) {
			for (var channel in channels) {
				var index = channels[channel].indexOf(callback)
				if (index > -1) channels[channel].splice(index, 1)
			}
		},
		trigger: function(channel, args) {
			console.log(channel)
			channels[channel].map(function(callback) {
				callback(args)
			})
		}
	}
}.call()
var ContactsWidget = {
	controller: Observable.register(["updateContact"], function() {
		this.contacts = Contact.list()
	}),
	view: function(ctrl) {
		return [
			m.component(ContactForm),
			m.component(ContactList, {contacts: ctrl.contacts})
		]
	}
}

var ContactForm = {
	controller: function(args) {
		this.contact = m.prop(new Contact())
		this.save = function(contact) {
			Contact.save(contact).then(Observable.trigger("updateContact"))
		}
	},
	view: function(ctrl, args) {
		var contact = ctrl.contact()

		return m("form", [
			m("label", "Name"),
			m("input", {oninput: m.withAttr("value", contact.name), value: contact.name()}),

			m("label", "Email"),
			m("input", {oninput: m.withAttr("value", contact.email), value: contact.email()}),

			m("button[type=button]", {onclick: ctrl.save.bind(this, contact)}, "Save")
		])
	}
}

var ContactList = {
	view: function(ctrl, args) {
		return m("table", [
			args.contacts().map(function(contact) {
				return m("tr", [
					m("td", contact.id()),
					m("td", contact.name()),
					m("td", contact.email())
				])
			})
		])
	}
}

// m.module(document.body, ContactsWidget);