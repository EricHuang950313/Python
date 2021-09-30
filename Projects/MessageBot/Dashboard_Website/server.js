const express = require('express')
const cors = require('cors')
const axios = require('axios')
require('dotenv').config()
const app = express()
const port = 3000

app.use(cors())
app.use(express.json())
app.use(express.static('dist'))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/sendMsgToChannel', async(req, res) => {
  if (req.body.id===process.env.A){
    await axios({
      method: 'post',
      url: `https://discord.com/api/channels/${req.body.id}/messages`,
      headers: {
        Authorization: `Bot ${process.env.BOT_TOKEN}`
      },
      data: {
        content: req.body.msg
      }
    })
    res.send('Done!')
  } else{
    res.send('Not available!')
  }
  
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})