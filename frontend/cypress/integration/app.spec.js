/* eslint-disable */
// Disable ESLint to prevent failing linting inside the Next.js repo.
// If you're using ESLint on your project, we recommend installing the ESLint Cypress plugin instead:
// https://github.com/cypress-io/eslint-plugin-cypress


describe('Home page', () => {
  beforeEach(() => {


    cy.visit('/')

  })

  it('should navigate to the home page', () => {
    // Start from the index page

    cy.get('title').contains('Breitling')
    cy.get('meta[name="description"]')
      .should("have.attr", "content", "Breitling News")
    cy.get('h1').contains("Breitling News Portal")
  })

  it('should show list on data fetch', () => {
    // Start from the index page
    cy.intercept(`${Cypress.env('apiBaseURL')}/api/news/`, {
      fixture: 'news_data.json'
    }).as("getNewsItems")
  })

})
