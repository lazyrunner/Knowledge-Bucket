const { GraphQLObjectType, GraphQLInt, GraphQLString, GraphQLList, GraphQLSchema, GraphQLNonNull} = require('graphql');
const Db = require('./db');

//overlay the schema in db.js with graphql schema - sequelize is the layer under it
const Person = new GraphQLObjectType({
	name: 'Person',
	description: 'This represents a person',
	fields: () => {
		return {
			id: {
				type: GraphQLInt,
				resolve(person){
					//come from sequelize
					return person.id;
				}
			},
			firstName: {
				type: GraphQLString,
				resolve(person){
					return person.firstName;
				}
			},
			lastName: {
				type: GraphQLString,
				resolve(person){
					return person.lastName;
				}
			},
			email: {
				type: GraphQLString,
				resolve(person){
					return person.email;
				}
			},
			posts: {
				type: new GraphQLList(Post),
				resolve(person) {
					// provided by sequelize by the relationship
					return person.getPosts();
				}
			}
		};
	}
});

const Post = new GraphQLObjectType({
	name: 'Post',
	description: 'This represents a post',
	fields: () => {
		return {
			id: {
				type: GraphQLInt,
				resolve(person){
					//come from sequelize
					return person.id;
				}
			},
			title: {
				type: GraphQLString,
				resolve(post){
					return post.title;
				}
			},
			content: {
				type: GraphQLString,
				resolve(post){
					return post.post;
				}
			}
		};
	}
});


const Mutation = new GraphQLObjectType({
	name: 'Mutation',
	description: 'For insertion and updation',
	fields() {
		return {
			// like public api
			addPerson : {
				type: Person,
				args: {
					firstName: {
						type: new GraphQLNonNull(GraphQLString)
					},
					lastName: {
						type: new GraphQLNonNull(GraphQLString)
					},
					email: {
						type: new GraphQLNonNull(GraphQLString)
					}
				},
				resolve(_, args) {
					return Db.models.person.create({
						firstName: args.firstName,
						lastName: args.lastName,
						email: args.email.toLowerCase()
					});
				}
			}
		};
	}
});

// query type - starting point where graphql looks to shape the data

const Query = new GraphQLObjectType({
	name: 'Query',
	description: 'This is root query',
	fields: () => {
		return {
			people: {
				type: new GraphQLList(Person),
				args: {
					id: {
						type: GraphQLInt
					},
					email: {
						type: GraphQLString
					}
				},
				// args are variables to be fed into graphql query
				// root is userdefined
				resolve(root, args){
					// returns promise
					return Db.models.person.findAll({where: args});
				}
			},
			posts: {
				type: new GraphQLList(Post),
				resolve(root, args){
					return Db.models.post.findAll({where: args});
				}
			}
		};
	}
});


// starting point for the query
// only 1 root query for all public apis
const Schema  = new GraphQLSchema({
	query: Query,
	mutation: Mutation
})


module.exports = Schema;