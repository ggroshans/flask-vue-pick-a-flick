// https://docs.cypress.io/api/introduction/api.html

import { v4 as uuidv4 } from "uuid";

let username = uuidv4();
let password = uuidv4();

describe("Register New User", () => {
  it("Click Register Button", () => {
    cy.visit("http://localhost:8080/");
    cy.get("[cy-test=splash-register-btn]").click();
    cy.url().should("include", "/register");
  });
  it("Enter Credentials", () => {
    cy.get("[cy-test=register-username]").type(username);
    cy.get("[cy-test=register-password]").type(password);
  });
  it("Submit Registration", () => {
    cy.get("[cy-test=register-submit").click();
    cy.url().should("include", "/login");
  });
});

describe("Login New User", () => {
  it("Enter Credentials", () => {
    cy.get("[cy-test=login-username]").type(username);
    cy.get("[cy-test=login-password]").type(password);
  });
  it("Submit Login", () => {
    cy.get("[cy-test=login-submit]").click();
    cy.url().should("include", "/genres");
  });
});

describe("Pick and Submit Genres", () => {
  it("Pick Genres", () => {
    cy.get("[cy-test=genre-button-container]").within(() => {
      cy.get("button").should($button => {
        expect($button).to.have.length(19);
        let randIndices = Array.from(Array(3)).map(x =>
          Math.floor(Math.random() * 19)
        );
        randIndices.forEach(index => $button[index].click());
      });
    });
    cy.get("[cy-test=genre-submit]").click();
    cy.url().should("include", "/movies");
    
  });
});
