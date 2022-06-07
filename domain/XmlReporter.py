from pyreportjasper import PyReportJasper

import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))

from utils.ReportService import ReportService

class XmlReporter(object):

    def fill(self, reportId):

        reportService = ReportService()

        result = reportService.getReportInformation(reportId)

        # Path with the file to be filled
        template_file = result["template_path"]

        # List of source files where the data will be retrieved
        data_file = result["sources"][0]

        # Path where locate files
        output_path = "outputs/" + result["name"]

        xml_path = result["xml_path"]

        pyreportjasper = PyReportJasper()

        pyreportjasper.config(
            template_file,
            "/tmp/" + output_path,
            output_formats=["pdf"],
            db_connection={
                'driver': 'xml',
                'data_file': data_file,
                'xml_xpath': xml_path,
            }
        )

        result_process = pyreportjasper.process_report()
        return result_process , output_path