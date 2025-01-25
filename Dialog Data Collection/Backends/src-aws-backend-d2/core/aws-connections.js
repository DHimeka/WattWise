const AWS = require("aws-sdk");
module.exports.dynamoDocClient = new AWS.DynamoDB.DocumentClient({ region: "ap-south-1" });
module.exports.s3 = new AWS.S3({ region: "ap-south-1" });
