from fastapi import FastAPI

from mangum import Mangum

from domain.XmlReporter import XmlReporter
from utils.S3Service import S3Service

app = FastAPI()

s3Service = S3Service()

@app.get("/reports")
async def getReports():
    return [
        {
            "id": 1,
            "name": "my-dummy-report",
            "template_path": "test/templates/CancelAck.jrxml",
            "sources": [
                "test/data/CancelAck.xml"
            ]
        }
    ]

@app.post("/reports/{reportId}")
async def generateReport(reportId: int):
    reporter = XmlReporter()
    status, output_path = reporter.fill(1)
    if status:

        s3Service.putObject(bucketName="spring-boot-lambda-jprugo", key= output_path + ".pdf", path= "/tmp/" + output_path + ".pdf")

        results = s3Service.getContentPresignedUrls("spring-boot-lambda-jprugo")
        # File generated succesfully
        response = {
            'files': results
        }
    else:
        # Show error
        response = {
            
        }

    return response

handler = Mangum(app)