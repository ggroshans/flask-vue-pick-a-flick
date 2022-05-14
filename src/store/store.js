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
        authStatus: false,
        genresQuery: {},
        userMovieList: {},
        darkMode: false,
    },
    getters: {
        getCurrentMovie (state) {
            return state.currentMovieObj;
        },
        getAuthStatus (state) {
            return state.authStatus;
        },
        getGenresQuery (state) {
            return state.genresQuery;
        },
        getUserMovieList (state) {
            return state.userMovieList;
        },
        getDarkMode (state) {
            return state.darkMode;
        }
    },
    mutations: {
        setCurrentMovieObj (state, obj) {
            state.currentMovieObj = obj;
        },
        setAuthStatus(state, status) {
            state.authStatus = status;
        },
        setGenresQuery(state, array) {
            state.genresQuery = array;
        },
        setUserMovieList(state, array) {
            state.userMovieList = array;
        },
        setDarkMode(state, status){
            state.darkMode = status;
        }

    },
    plugins: [vuexLocal.plugin]
})