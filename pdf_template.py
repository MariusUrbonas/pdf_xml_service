from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import io


class ReportTemplate:
    def __init__(self, report_json):
        self.report_json = report_json

    def reportBytes(self):
        with io.BytesIO() as bytes_io:
            c = canvas.Canvas(bytes_io)
            c.setFont('Helvetica', 30)
            c.drawString(80*mm,260*mm,"The Report")
            c.setFont('Helvetica', 14)
            c.drawString(115*mm,240*mm,"Organisaion: {}".format(self.report_json['organization']))
            c.drawString(115*mm,234*mm,"Reported: {}".format(self.report_json['reported_at']))
            c.drawString(115*mm,228*mm,"Created: {}".format(self.report_json['created_at']))
            l = self.report_json['inventory']
            text_width = 6
            count = 0
            for a in l:
                c.drawString(90*mm,150*mm-(text_width*count)*mm,"{}: {}".format(a['name'],a['price']))
                count += 1
            c.showPage()
            c.save()
            return bytes_io.getvalue()

