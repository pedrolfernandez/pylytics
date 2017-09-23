from unittest import TestCase
from pylytics.input_processor.InputCSVFileProcessor import InputCSVFileProcessor
from pylytics.input_processor.InputReport import InputReport
from pylytics.data_reports.DataReport import DataReport
from pylytics.data_reports.DataReportProcessor import DataReportProcessor

import configparser
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import time

class TestInputFileProcessor(TestCase):
    #IN_FILE = 'C:\\Users\\plfernandez\\PycharmProjects\\pylytics\\res\\testdata\\call-export-Foo.csv'
    #OUT_FILE = 'C:\\Users\\plfernandez\\PycharmProjects\\pylytics\\res\\testdata\\gen-out-call-export-Foo.csv'
    #CONFIG_FILE = 'C:\\Users\\plfernandez\\PycharmProjects\\pylytics\\res\\testdata\\pylyticsFlow1.cfg'

    #CONFIG_FILE = '/pylytics/res/testdata/pylyticsFlow1.cfg'
    #IN_FILE = '/pylytics/res/testdata/call-export-Foo.csv'
    CONFIG_FILE = '/pylytics/res/upload/pylyticsFlow1.cfg'
    IN_FILE = '/pylytics/res/upload/call-export-Foo.csv'
    OUT_FILE = '/pylytics/res/testdata/gen-out-call-export-Foo.csv'


    def test_processFile(self):
        # Input Processing
        config = configparser.ConfigParser()
        config.read(self.CONFIG_FILE)
        inputReportDef = InputReport(config)
        inputFileProcessor = InputCSVFileProcessor(self.IN_FILE, self.OUT_FILE, inputReportDef)
        df = inputFileProcessor.process()

        # Data Processing
        dataReportDef = DataReport(config,'datareport1')
        dataReportProcessor = DataReportProcessor(dataReportDef)
        df = dataReportProcessor.process(df)
        # df.plot()
        plt.plot(df)
        plt.savefig('/pylytics/res/datareport1.png')
        # plt.show()

