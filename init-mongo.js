db = db.getSiblingDB('server');
db.createUser({
    'user': process.env.MONGO_USERNAME,
    'pwd': process.env.MONGO_PWD,
    'roles': [
        {
            'role': 'readWrite',
            'db': 'server'
        }
    ]
});

db.createCollection('users', { capped: false} )
db.users.insert([
    {
        "username": process.env.API_USER,
        "password": process.env.API_PWD_HASH
    }
])
