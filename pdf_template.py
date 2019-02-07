from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import io


class ReportTemplate:
    def __init__(self, report_json):
        self.report_json = report_json

    def __makeTitle(self, canv):
        canv.setFont('Helvetica', 30)
        canv.drawString(80*mm,260*mm,"The Report")

    def __makeMeta(self, canv):
        canv.setFont('Helvetica', 14)
        # TODO: Make text does wrap at the end, longer texts currently don't fit
        canv.drawString(115*mm,240*mm,"Organisaion: {}".format(self.report_json['organization']))
        canv.drawString(115*mm,234*mm,"Reported: {}".format(self.report_json['reported_at']))
        canv.drawString(115*mm,228*mm,"Created: {}".format(self.report_json['created_at']))

    def __makeItems(self, canv):
        inventory = self.report_json['inventory']
        text_width = 6
        count = 0
        for item in inventory:
            canv.drawString(90*mm,150*mm-(text_width*count)*mm,"{}: {}".format(item['name'],item['price']))
            count += 1

    def reportBytes(self):
        with io.BytesIO() as bytes_io:
            c = canvas.Canvas(bytes_io)
            self.__makeTitle(c)
            self.__makeMeta(c)
            self.__makeItems(c)
            c.showPage()
            c.save()
            return bytes_io.getvalue()

