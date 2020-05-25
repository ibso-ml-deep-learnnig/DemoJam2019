const express = require('express');
const app = express();

app.use(express.json());

const courses = [
    {id: 1, name: 'course1'},
    {id: 2, name: 'course2'},
    {id: 3, name: 'course3'}
];

//Get method
//-----------------------------------------------------------------------------------------------
//http://localhost:3000
app.get('/',(req, res)=>{
    res.send('Hello World');
})

//http://localhost:3000/api/courses
app.get('/api/courses',(req, res)=>{
    res.send([1,2,3]);
})
//http://localhost:3000/api/courses/1
app.get('/api/courses/:id', (req, res) => {
    res.send(req.params.id);
});

//http://localhost:3000/api/findcourse/1
app.get('/api/findcourse/:courseid', (req, res) => {
    const course = courses.find(c => c.id === parseInt(req.params.courseid));
    if (!course) res.status(404).send('The course with given ID was not found');
    res.send(course);
});

//http://localhost:3000/api/courses/2019/09
app.get('/api/courses/:year/:month', (req, res) => {
    res.send(req.params);

    //http://localhost:3000/api/courses/2019/09?para=sort
    console.log(req.query);
    
});

const port = process.env.PORT || 3000;
app.listen(port,() => console.log(`Listening on port ${port}`)
);

//post method
//-------------------------------------------------------------------------------------------
app.post('/api/courses', (req, res) => {
    if (!req.body.name || req.body.name.length < 3){
       return res.status(404).sendStatus('Name is not valid');
    }
    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
});
//-------------------------------------------------------------------------------------------
//put method
//-------------------------------------------------------------------------------------------
app.put('/api/courses/:id', async (req, res) => {
    const course = courses.find(c => c.id === parseInt(req.params.id));
    await validation(course, req, res).then(course => {
        course.name = req.body.name;
        res.send(course);
    }, err => {
        return res.status(400).send(err);
    });
});

    function validation (course,req, res) {
    return new Promise( (resolve, reject) => {
        if (!course) {
            //res.status(404).send('The course with given ID was not found');
            let err = 'The course with given ID was not found';
            return reject(err);
        };
        if (!req.body.name || req.body.name.length < 3){
            // res.status(404).sendStatus('Name is not valid');
            let err = 'Name is not valid';
            return reject(err);
        };
        resolve(course);
    });
};

//-------------------------------------------------------------------------------------------
//delete method
//-------------------------------------------------------------------------------------------
app.delete('/api/courses/:id', (req, res) => {
    //validation   
    const course = courses.find(c => c.id === parseInt(req.params.id));
    if (!course) return res.status(404).send('The course with given ID was not found');

    //delete
    const index = courses.indexOf(course);
    courses.splice(index, 1);

    res.send(courses);
});
//you can use npm i -g nodemon to install auto restart functinallity by run 'nodemon Express.js'
//npm install --save-dev nodemon(have to add "start": "nodemon express.js" to package.json)
//npm install -g nodemon