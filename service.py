from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from models import Report
from config import DB_URL
from pdf_template import ReportTemplate
import json
from dicttoxml import dicttoxml

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = True
db = SQLAlchemy(app)


@app.route('/generate-report')
def generate_report():
    report_type = request.args.get('type')
    if not correct_type(report_type):
        return "Incorrect report type given"
    report_type = report_type.lower()
    report_id = get_int(request.args.get('id'))
    if report_id is None:
        return "Non integer report id given"
    report_entry = get_report(report_id)
    if report_entry is None:
        return "Report with given id does not exist"
    report = parse_report(report_entry)
    if report_type == 'pdf':
        return pdf_response(report, 'report_{}.pdf'.format(report_id))
    if report_type == 'xml':
        return xml_response(report)
    return 'Something unexpected happened while generating your report'


def pdf_response(report, filename):
	resp = Response(ReportTemplate(report).reportBytes())
	resp.headers['Content-Disposition'] = "inline; filename={}".format(filename)
	resp.headers["Content-Type"] = "application/pdf; charset=utf-8"
	return resp

def xml_response(report):
    resp = Response(dicttoxml(report))
    resp.mimetype = 'text/xml'
    return resp

def get_int(str_of_int):
    try:
        return int(str_of_int)
    except Exception as e:
        return None

def correct_type(report_type):
    if report_type is not None:
        return report_type.lower() in ['xml', 'pdf']
    return False

def parse_report(report_reponse):
    report_body = report_reponse.type
    try:
        return json.loads(report_body)
    except Exception as e:
        raise Exception(e)

def get_report(report_id):
    try:
        return db.session.query(Report).get(report_id)
    except Exception as e:
        raise Exception(e)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)