const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const authroute = require('./routes/auth');
const postRoute = require('./routes/posts');

dotenv.config();

const app = express();

//connect to mongodb
mongoose.connect(process.env.DB_CONNECT,
{ useNewUrlParser: true, useUnifiedTopology: true },
() => console.log('connected to db')
);

//middleware
app.use(express.json());
//route middleware
app.use('/api/user', authroute);
app.use('/api/posts', postRoute);

app.listen(3000, () => console.log("Server is running") );

