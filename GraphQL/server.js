const Express = require('express');
const { graphqlHTTP } = require('express-graphql');
const Schema = require('./schema');

const APP_PORT = 3000;

const app = Express();

// run the graphql middleware
app.use('/graphql', graphqlHTTP({
	schema: Schema,
	pretty: true,
	graphiql: true
}));

app.listen(APP_PORT, ()=>{
	console.log(`App listening on ${APP_PORT}`);
});
