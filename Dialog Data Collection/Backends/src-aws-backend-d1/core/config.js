module.exports.config = {
	deviceName: 'WattWiseD1',
	
	dynamoDb: {
		table: process.env.DYNAMO_DB_TABLE,
	},

	s3: {
		bucket: process.env.S3_STORAGE_BUCKET
	}
};