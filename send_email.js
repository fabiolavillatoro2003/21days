//
// send_email.js
// This script sends an email reminder using Nodemailer.
//

// Use the 'nodemailer' library to send emails
const nodemailer = require('nodemailer');

// Set up the transporter using SMTP with an App Password from GitHub Secrets
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER, // Your Gmail address
    pass: process.env.EMAIL_PASSWORD // Your App Password from GitHub Secrets
  }
});

// Define the email options
const mailOptions = {
  from: process.env.EMAIL_USER,
  to: process.env.EMAIL_USER,
  subject: 'Daily Cold Plunge Reminder',
  text: `
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
  `
};

// Send the email
transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log("An error occurred!");
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});

