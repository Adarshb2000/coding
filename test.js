const express = require('express')
const app = express()

const router = express.Router()

app.use('/home', router)



router.get('/home/user', (req, res, next) => {
    console.log(1)
    next()
})

router.get('/user', (req, res, next) => {
    next();
    console.log(2);
})

router.get("/home", (req, res, next) => {
    console.log(3)
    next();
})
router.get('/:user', (req, res, next) => {
    next();
    console.log(4);
})
app.listen(3000)
