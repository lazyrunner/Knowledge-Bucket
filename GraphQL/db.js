const Sequelize = require('sequelize');
// for the times functionality to insert multiple entries in database
const _ = require('lodash');
const Faker = require('faker');


const Conn = new Sequelize(
 	//name of database
 	'postgres',
 	// username
 	'postgres',
 	//password
 	'root',
 	{
 		dialect: 'postgres',
 		host: 'localhost',
 	}

);

 
// tables 
const Person = Conn.define('person', {
 	firstName: {
 		type: Sequelize.STRING,
 		allowNull: false

 	},
 	lastName: {
 		type: Sequelize.STRING,
 		allowNull: false

 	},
 	email: {
 		type: Sequelize.STRING,
 		allowNull: false,
 		validate: {
 			isEmail: true
 		}

 	},
});


const Post = Conn.define('post',{
	title : {
		type: Sequelize.STRING,
		allowNull: false
	},
	content: {
		type: Sequelize.STRING,
		allowNull: false
	}
});

// Relationships
Person.hasMany(Post);
Post.belongsTo(Person);

// 'force' checks table exist
Conn.sync({force: true}).then(()=>{
	_.times(10, ()=>{
		return Person.create({
			firstName: Faker .name.firstName(),
			lastName: Faker.name.lastName(),
			email: Faker.internet.email()
		}).then(person => {
			return person.createPost({
				title: `Sample title by ${person.firstName}`,
				content: 'This is sample article'

			});

		});
	});

});


module.exports = Conn;