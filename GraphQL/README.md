# GraphQL

## Author : Sudeshna Bora

---

This creates a node js project with graphql server connecting to mysql. 

---

### What is graphql?

It tries to replace REST API. 

In case of rest api, we may need to repeatedly make rest calls to get relevant data.
GraphQL bundles these requests and gives us tailored data.

---

### Steps

#### Step 1:

Install and initialise npm

1. ```sudo apt install npm```
2. ```npm init ```

#### Step 2:

1. Install nodejs.

```
npm i -S nodejs
```

2. Install and setup [postgresql](../Postgresql/introduction.md).


---

### Files and description


#### db.js

This is the ORM for postgresql. 
This file defines the schema as well as gives a functionality to insert 10 random fields.
It uses ```sequelize``` as ORM for postgresql. 
The db connection is present here. 

#### schema.js

This is the schema and query definition file for graphql.
It provides 2 objects ```Person``` and ```Post``` that overlays the schema definition in db.js
It additionally provides a ```query``` and a ```mutation``` type object for get and post calls. 
The important point to note here is there is only one generic ```query``` object that can handle 
a variety of find queries.
Finally, the query and mutation type are defined in a ```schema``` which is the point where these
queries are exposed. 

#### server.js

This is the file that starts and exposes the graphql api server. 
It uses ```/graphql``` as the endpoint and also exposes ```graphiql``` as GUI to see the response to the 
end point and try different combinations.

---

