const functions = require('firebase-functions');
const admin = require('firebase-admin');
const nodemailer = require('nodemailer');
const cors = require('cors')({ origin: true });

admin.initializeApp();

const transporter = nodemailer.createTransport({
  // Configure your email service here
});

exports.sendAdminCode = functions.https.onCall(async (data, context) => {
  // Enable CORS using the `cors` express middleware
  return cors()(data.rawRequest, data.rawResponse, async () => {
    const { email } = data;
    const adminCode = Math.random().toString(36).substring(2, 8).toUpperCase();

    await admin.firestore().collection('adminCodes').doc(email).set({
      code: adminCode,
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    });

    const mailOptions = {
      from: 'your-email@example.com',
      to: email,
      subject: 'Your Admin Verification Code',
      text: `Your admin verification code is: ${adminCode}`
    };

    try {
      await transporter.sendMail(mailOptions);
      return { success: true, message: 'Admin code sent to your email' };
    } catch (error) {
      console.error('Error sending email:', error);
      return { success: false, message: 'Failed to send admin code' };
    }
  });
});

exports.verifyAdminCode = functions.https.onCall(async (data, context) => {
  const { adminCode } = data;
  const email = context.auth.token.email;

  const docRef = admin.firestore().collection('adminCodes').doc(email);
  const doc = await docRef.get();

  if (doc.exists && doc.data().code === adminCode) {
    await docRef.delete();
    return { verified: true };
  } else {
    return { verified: false };
  }
});