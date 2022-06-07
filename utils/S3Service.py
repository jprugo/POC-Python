import boto3

class S3Service():

    def __init__(self):
        self.s3_client = boto3.client("s3")

    def getObject(self, bucketName, key):
        return self.s3_client.get_object(Bucket=bucketName, Key=key)["Body"].read().decode("utf-8")
    
    def putObject(self, bucketName, key, path):
        with open(path, "rb") as data:
            return self.s3_client.put_object(
                Body=data, 
                Bucket=bucketName, 
                Key=key
            )

    def generatePreSignedUrl(self, bucketName, key):
        return self.s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucketName,
                                                            'Key': key},
                                                    ExpiresIn=15000)

    def getContentPresignedUrls(self, path):
        results = []
        for fileKey in self.s3_client.list_objects(Bucket=path)['Contents']:
            print(fileKey['Key'])
            results.append(self.generatePreSignedUrl(path, fileKey['Key']))
        return results