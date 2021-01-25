const router = require("express").Router()
const axios =require("axios")
let spawn = require("child_process").spawn

router.post('/', (req , res)=>{
    
    const tweet = req.body.tweet
    console.log(tweet)
    let proccess = spawn('python' , ['C:/Users/amir/Desktop/FinalPeoject/pre.py' , tweet] , {cwd: __dirname})
    proccess.stdout.on('data', async function(data) { 
    let sent = data.toString()
    sent = sent.replace('[' , "")
    sent = sent.replace(']' , "")
    sent = sent.split(',')
    sent[2] =sent[2].replace("\r\n" , "")
    for (i =0 ; i<3 ; i++)
    {
        sent[i] = parseFloat(sent[i])
    }
    console.log(sent)
    response =await axios({
        method: 'post',
        url: 'http://localhost:5000',
        data: {
          tweet : sent
        }
      });
      console.log(response.data.response)
      res.send(response.data.response)
    
   } ) 
} )

module.exports = router