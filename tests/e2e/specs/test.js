// https://docs.cypress.io/api/introduction/api.html

import { v4 as uuidv4 } from 'uuid';

let username = uuidv4()
let password = uuidv4()

describe('Register User', () => {
  it('Click Register Button', () => {
    cy.visit('http://localhost:8080/')
    cy.get('[cy-test=splash-register-btn]').click()
    cy.url().should('include', '/register')
  })
  it('Enter Credentials', () => {
    cy.get('[cy-test=register-username]').type(username)
    cy.get('[cy-test=register-password]').type(password)
  })
  it('Submit Registration', () => {
    cy.get('[cy-test=register-submit').click()
    cy.url().should('include', '/login')
  })
})

describe('Login User', () => {
  it('Enter Credentials', () => {
    cy.get('[cy-test=login-username]').type(username)
    cy.get('[cy-test=login-password]').type(password)
  })
    it('Submit Login', () => {
    cy.get('[cy-test=login-submit').click()
    cy.url().should('include', '/login')
  })
})