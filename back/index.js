const express = require('express')
const router = require('express').Router()
let spawn = require("child_process").spawn

const bodyParser = require('body-parser')
const { json } = require('body-parser')
const jsonParser = bodyParser.json()
const urlencodedParser = bodyParser.urlencoded({ extended: false })


const app = express()

const PORT = 3000

app.use(jsonParser)


app.listen(PORT , ()=> {console.log(`server is running on port : ${PORT}`)})

app.post('/' , require('./routes/getPreProccess'))