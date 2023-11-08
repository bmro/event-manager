# Event Manager

## Planning

1. User registers a new event.
 - [X] Create backend to accept a new event
 - [X] Define api to register a new event POST /api/events (name and date)
   - [X] Logs the event instead of saving to the DB
 - [X] Create front-end app to make the new event 
 - [X] Create form to submit a new event (name and date)
 - [X] Dockerize the frontend and backend.
 - [X] Add connection to MySQL
   - [X] Persist the created event

2. Deploy it on Kubernetes
 - [ ] StatefulSet, Service, ConfigMap, Secrets Database
 - [ ] Deployment, Service, ConfigMap, Secrets Backend
 - [ ] Deployment, Service, ConfigMap, Secrets Frontend
