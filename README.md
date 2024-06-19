# WeightBook: A Workout Tracking app
WeightBook is a web app that allows users to create workouts with specific numbers of sets, reps and weight.
Upon creating an account, you can select your role. Free users don't have the ability to add workouts, but can browse the app and view its features. Premium users get access to all of the available features on the app, including creating, adding and logging workouts. They can also view a graph displaying their progress. Administrators have access to all parts of the website.


## Installation
`git clone git@github.com:yeehaw114/COP4521-Project.git`

## Dependencies
Download these dependencies before running the project.
- [NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [Docker](https://docs.docker.com/engine/install/)

[![NPM](https://skillicons.dev/icons?i=npm)](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
[![Docker](https://skillicons.dev/icons?i=docker)](https://docs.docker.com/engine/install/)

WSL is recommended as well.

## Getting Started
You want to ensure the backend is running before starting up the frontend to avoid network errors.

__Backend:__ `docker compose up`

__Frontend:__ `npm ci && npm run dev`
