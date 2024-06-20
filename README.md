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

#### Zachary Lima: 
- Primarily worked on the Django backend, creating and managing all of the different endpoints in the server. Implemented user authentication as well.

#### Alex Gonzalez:
- Primarily handled front end application in Vue.js, as well as docker setup. Dockerized the application.

#### Fernando de Tores: 
- RBAC, custom migrations, custom middleware, and database setup. Implemented the django.sh, 

#### Gavin McDavitt: 
- Wrote the report, and assisted in RBAC.

#### Zachary Herman:
- Prototyped some Vue.js coponents and worked mostly on frontend design.

#### Ethan Burke: 
- Worked on potential Role-Based Access Control implementations, and helped design the capabilities each type of user would have in the database.

