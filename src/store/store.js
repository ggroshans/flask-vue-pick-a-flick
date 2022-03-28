/* eslint-disable */

import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

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
        getAuthStatus (state) {
            return state.authStatus;
        }
    },
    mutations: {
        setCurrentMovieObj (state, obj) {
            state.currentMovieObj = obj;
        },
        setAuthStatus(state, status) {
            state.authStatus = status;
        }
    },
    plugins: [vuexLocal.plugin]
})