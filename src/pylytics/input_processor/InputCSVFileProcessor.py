import pandas as pd
from pandas import DataFrame
from pylytics.input_processor.InputDataFrameProcessor import InputDataFrameProcessor
from pylytics.input_processor.InputReport import InputReport

class InputCSVFileProcessor :
    def __init__(self, inputFilePath : str, outputFilePath : str, inputReportDef : InputReport):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath
        self.inputReportDef = inputReportDef

    def process(self) -> DataFrame :
        df = pd.read_csv(self.inputFilePath)
        input_df_processor = InputDataFrameProcessor(self.inputReportDef)
        df = input_df_processor.process(df)
        return df
