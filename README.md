# WeightBook: A Workout Tracking App
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

### Backend Libraries

- Django
- psycopg2-binary
- djangorestframework
- django-cors-headers
- djangorestframework-simplejwt
- timedelta 



### Frontend Libraries

- mdi/font
- pinia
- vue
- vue-router
- vuetify

## Separation of work

#### Zachary Lima
- Created the endpoints in the Django HTTP server
- Designed and implemented the serializers in Django
- Implemented user authentication

#### Alex Gonzalez
- Created the frontend application that interacts with the backend
- Designed the Vue.js components and views
- Dockerized the application.

#### Fernando de Tores
- Implemented Role Based Access through custom migrations
- Created custom middleware to allow users to access the database through their role

#### Gavin McDavitt
- Wrote the distributed computing report
- Assisted with RBAC
- Name the app

#### Zachary Herman
- Prototyped some Vue.js coponents
- Worked mostly on frontend design.

#### Ethan Burke
- Worked on potential Role-Based Access Control implementations
- Helped design the capabilities each type of user would have in the database

