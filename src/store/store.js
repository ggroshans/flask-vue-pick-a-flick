/* eslint-disable */

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        currentMovieObj: {},
        token: null,
    },
    getters: {
        getCurrentMovie (state) {
            return state.currentMovieObj;
        },
        getToken (state) {
            return state.token;
        }
    },
    mutations: {
        setCurrentMovieObj (state, obj) {
            state.currentMovieObj = obj;
        },
        setToken(state, token) {
            state.token = token;
        }
    }
})