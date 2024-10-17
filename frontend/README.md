# ** Dependencies **
1. React 
- React is a JavaScript library for building user interfaces, UI components and manage the state and lifecycle of these components.
- React-DOM is a package that provides DOM-specific methods for React. It is responsible for rendering React components to the browser's DOM and handling the interaction between React and the web browser.
- From installation perspective, React-DOM will be used to attach your React application to a specific DOM element in your HTML.
- React provides the core functionality for building UI components, while React-DOM connects those components to the web page, rendering them into the DOM.

2. React-Scripts
- React-Scripts is a set of scripts used by Create React App (CRA) to simplify the development process. It provides a set of pre-configured scripts for common tasks like starting the development server, building the app for production, running tests, and ejecting configurations.

- React-Scripts helps streamline and automate common tasks in a React development environment. It does not directly interact with React or React-DOM but facilitates their use by handling build processes and development utilities.

3. Axios
- Axios is a promise-based HTTP client for making HTTP requests from a web application. It allows you to fetch data from APIs and handle responses.
- From Installation perspective, we include Axios in your project to perform network requests to external services or APIs.
- Axios is not directly related to React, React-DOM, or React-Scripts. Instead, it is used within React components to perform data fetching or send data to a server. React components can utilize Axios to retrieve or submit data as part of their functionality.

In essence, React and React-DOM work together to create and render your UI, React-Scripts manages your development environment, and Axios handles data fetching.
