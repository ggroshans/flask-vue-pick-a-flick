/* eslint-disable */

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        currentMovieObj: {},
        token: null,
        authStatus: false,
    },
    getters: {
        getCurrentMovie (state) {
            return state.currentMovieObj;
        },
        getToken (state) {
            return state.token;
        },
        getAuthStatus (state) {
            return state.authStatus;
        }
    },
    mutations: {
        setCurrentMovieObj (state, obj) {
            state.currentMovieObj = obj;
        },
        setToken(state, token) {
            state.token = token;
        },
        setAuthStatus(state, status) {
            state.authStatus = status;
        }
    }
})