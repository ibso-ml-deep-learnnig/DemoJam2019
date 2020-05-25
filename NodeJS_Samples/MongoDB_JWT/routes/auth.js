const router = require('express').Router();
const User = require('../model/User.js');
const { registerValidation, loginValidation } = require('../validation');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

router.post('/register', async (req, res) => {

    //do validations before create user
    //const validation = joi.validate(req.body, schema);
    const { error } = registerValidation(req.body);
    
    //res.send(validation.error.details[0].message);
    if( error) return res.status(400).send(error.details[0].message);
    
    //check email is already in db
    const emailExist = await User.findOne({email: req.body.email});
    if(emailExist) return res.status(400).send('Email already exist');

    //Hash passwords
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(req.body.password, salt);

    //create new user
    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: hashedPassword
    });
    try{ 
        const saveduser = await user.save();
        res.send({user: saveduser._id});
    }catch(err){
        res.status(400).send(err);
    };
});

router.post('/login', async (req, res) => {
    //check format
    const { error } = loginValidation(req.body);
    if( error) return res.status(400).send(error.details[0].message);   
    //check email exist
    const user = await User.findOne({email: req.body.email});
    if (!user) return res.status(400).send('Email is not found');
    //password is correct
    const validPass = await bcrypt.compare(req.body.password, user.password);
    if(!validPass) return res.status(400).send('Invalid password')

    //create and assign jwt token
    const token = jwt.sign({id: user.id}, process.env.TOKEN_SECRET);
    res.header('auth-token', token).send(token);

});

router.post('/login')

module.exports = router;