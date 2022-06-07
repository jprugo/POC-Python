import json

class ReportService():

    def getReportInformation(self, reportId):
        json_file = open('reports.json', 'r')
        
        data = json.load(json_file)

        result =  list(filter(lambda e: e["id"] == reportId, data))

        print(result)

        return result[0]
