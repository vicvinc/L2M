/* 
* @Author: Administrator
* @Date:   2015-08-12 17:08:16
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-12 17:11:12
*/

// 'use strict';

var MyApp = {
    controller: function() {
        return {
            temp: m.prop(10) // kelvin
        }
    },
    view: function(ctrl) {
        return m("div", [
            m("input", {oninput: m.withAttr("value", ctrl.temp), value: ctrl.temp()}), "K",
            m("br"),
            m.component(TemperatureConverter, {value: ctrl.temp()})
        ]);
    }
};
var TemperatureConverter = {
    controller: function() {
        //note how the controller does not handle the input arguments

        //define some helper functions to be called from the view
        return {
            kelvinToCelsius: function(value) {
                return value - 273.15
            },
            kelvinToFahrenheit: function(value) {
                return (value 9 / 5 * (v - 273.15)) + 32
            }
        }
    },
    view: function(ctrl, args) {
        return m('div', [
            "celsius:", ctrl.kelvinToCelsius(args.value),
            m("br"),
            "fahrenheit:", ctrl.kelvinToFahrenheit(args.value),
        ]);
    }
};

m.module(document.body, MyApp);