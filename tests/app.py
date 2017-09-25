from flask import Flask, render_template, request, redirect
import os
from pylytics.input_processor.InputCSVFileProcessor import InputCSVFileProcessor
from pylytics.input_processor.InputReport import InputReport
from pylytics.data_reports.DataReport import DataReport
from pylytics.data_reports.DataReportProcessor import DataReportProcessor

import configparser
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#UPLOAD_FOLDER = '/pylytics/tests/static/'
#CONFIG_FILE = UPLOAD_FOLDER + 'pylyticsFlow1.cfg'
#IN_FILE = UPLOAD_FOLDER + 'call-export-Foo.csv'
#OUT_FILE = '/pylytics/res/testdata/gen-out-call-export-Foo.csv'

# PATHS for Cloud Froundry
UPLOAD_FOLDER = './tests/static/'
CONFIG_FILE = UPLOAD_FOLDER + 'pylyticsFlow1.cfg'
IN_FILE = UPLOAD_FOLDER + 'call-export-Foo.csv'
OUT_FILE = './res/testdata/gen-out-call-export-Foo.csv'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return render_template('index.html')



def gen_report():
        # Input Processing
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        inputReportDef = InputReport(config)
        inputFileProcessor = InputCSVFileProcessor(IN_FILE, OUT_FILE, inputReportDef)
        df = inputFileProcessor.process()

        # Data Processing
        dataReportDef = DataReport(config,'datareport1')
        dataReportProcessor = DataReportProcessor(dataReportDef)
        df = dataReportProcessor.process(df)

        return df




@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if ('config' not in request.files) or ('inputcsv' not in request.files) :
           return redirect(request.url)

    config = request.files['config']
    inputcsv = request.files['inputcsv']

    if config.filename == '' or inputcsv.filename == '':
        return redirect(request.url)

    if config and inputcsv :
        inputcsv.save(os.path.join(app.config['UPLOAD_FOLDER'], "call-export-Foo.csv"))
        config.save(os.path.join(app.config['UPLOAD_FOLDER'], "pylyticsFlow1.cfg"))

        df = gen_report()
        plt.plot(df)


        plt.xlabel('Min')
        plt.ylabel('Spoken Minutes')
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(UPLOAD_FOLDER + 'datareport1.png')

        return render_template('genreport.html', table=df.to_html())

    return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)