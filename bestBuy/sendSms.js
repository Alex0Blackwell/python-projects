'use strict';
const nodemailer = require('nodemailer');
const config = require('./config');

async function main(){
	const transporter = nodemailer.createTransport(config);

  let mailOptions = {
    from: config.email, // sender address
    to: config.to,
    subject: 'test subject', // Subject line
    text: 'test body', // plain text body
    html: '<b>test html</b>' // html body
  };

  let info = await transporter.sendMail(mailOptions)

  console.log('Message sent: %s', info.messageId);
}

main().catch(console.error);
