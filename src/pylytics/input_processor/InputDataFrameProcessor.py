from pylytics.common.Global import logger
from pylytics.input_processor.InputReport import InputReport
from pandas import DataFrame


class InputDataFrameProcessor:
    def __init__(self, inputReportDef : InputReport):
        self.inputReportDef = inputReportDef

    def process(self, dataFrame : DataFrame) -> DataFrame:
        # 1. First we filter out non desired columns
        dataFrame = dataFrame.loc[:,self.inputReportDef.columns]

        logger.debug(' ----- INITIAL STATE OF THE DATAFRAME WITH THE DESIRED COLUMNS ')
        logger.debug(dataFrame.head())

        # 2. We apply the mapping definitions to the desired columns
        for (col, mapFuncStr) in self.inputReportDef.mappings:
            dataFrame[col] = dataFrame[col].apply(eval('lambda ' +  col + ' : ' + mapFuncStr))
        logger.debug(' ----- STATE AFTER APPLYING THE MAPPING FUNCTIONS ')
        logger.debug(dataFrame.head())

        # 3. Now we add the new columns as per config file
        for (newCol, col, funcStr) in self.inputReportDef.newcols:
            dataFrame[newCol] = dataFrame[col].apply(eval('lambda ' + col + ' : ' + funcStr))

        logger.debug(' ----- STATE AFTER ADDING THE NEW COLUMNS')
        logger.debug(dataFrame.head())

        # 4. Now we apply the filters
        logger.debug(' Number of rows before ' + str(len(dataFrame.index)))
        if self.inputReportDef.filter :
            dataFrame.query(self.inputReportDef.filter, inplace=True)
            logger.debug(' Number of rows after ' + str(len(dataFrame.index)))
            logger.debug(dataFrame.head())

        return dataFrame