'use strict';
const nodemailer = require('nodemailer');
const fs = require('fs');
const config = require('./config');


async function main(){
	const transporter = nodemailer.createTransport(config);
  var inStock = false;

  let mailOptions = {
    from: config.email, // sender address
    to: config.to,
    subject: 'test subject', // Subject line
    text: 'test body', // plain text body
    html: 'test html' // html body
  };

  var interval = setInterval(function() {
    fs.readFile('inStock.txt', (err, data) => {
      if (err) throw err;

      console.log(data.toString());
      if(data.toString() == 'true') {
        inStock = true;
        clearInterval(interval);
        console.log('data is true');
      }
      else if(data.toString() == 'false') {
        console.log('data is false');
      }
    })
  }, 10000);

  if(inStock) {
    let info = await transporter.sendMail(mailOptions);
    console.log('Message sent: %s', info.messageId);
  }
}

main().catch(console.error);
console.log("reached end of program");
