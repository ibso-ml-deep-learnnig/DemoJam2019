# Frontend

Frontend exposes an HTTP server (a Flask app) to browse the website for users.
It forwards each request to the corresponding backend service to process, behind, responses processing result to user. 

The Docker image @dockerhub:  ericwudocker01/demojam2019_frontend

The list of backend services.

| Action            | Backend Service        | Exposed Port | Language      | Description                  |
| ----------------- | -----------------------| ------------ | ------------- | -----------------------------|
| Login             | account/login          | 50050        | Python        | Handler user's login request |
| Register          | account/register       | 50050        | Python        | Handler register request  |
| Create Asset      | AssetCreation      | 50051        | Node.js        | Create asset  |
