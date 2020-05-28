'use strict';
const nodemailer = require('nodemailer');
const fs = require('fs');
const config = require('./config');

const transporter = nodemailer.createTransport(config);

let mailOptions = {
  from: config.email, // sender address
  to: config.to,
  subject: 'Nintendo Switch in Stock Now!', // Subject line
  text: 'Nintendo Switch', // plain text body
  html: 'Go xan! It should be available <a href="https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625">here</a>.' // html body
};

async function sendMail() {
  let info = await transporter.sendMail(mailOptions);
  console.log('Message sent: %s', info.messageId);
}

async function main(){

  var interval = setInterval(function() {
    fs.readFile('inStock.txt', (err, data) => {
      if (err) throw err;

      console.log(data.toString());
      if(data.toString() == 'true') {
        sendMail();
        clearInterval(interval);
        console.log('data is true');
      }
      else if(data.toString() == 'false') {
        console.log('data is false');
      }
    })
  }, 120000);  // refresh every 2 mins
}

main().catch(console.error);
console.log("reached end of program");
