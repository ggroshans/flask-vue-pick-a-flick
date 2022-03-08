/* eslint-disable */

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        currentMovieObj: {}
    },
    getters: {
        getCurrentMovie (state) {
            return state.currentMovieObj;
        }
    },
    mutations: {
        setCurrentMovieObj (state, obj) {
            state.currentMovieObj = obj;
        }
    }
})