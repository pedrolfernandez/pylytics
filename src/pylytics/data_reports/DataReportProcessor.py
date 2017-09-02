from pylytics.common.Global import logger
from pylytics.data_reports.DataReport import DataReport
from pandas import DataFrame


class DataReportProcessor:
    def __init__(self, reportDef : DataReport):
        self.reportDef = reportDef

    def process(self, dataFrame : DataFrame) -> DataFrame:

        logger.debug('Starting Data Report Generation')
        logger.debug('Initial Data Frame')
        logger.debug(dataFrame.head())

        aggregDict = {}
        colnames = []
        for (colName, colCol, colOp) in self.reportDef.attrCols :
            if not colCol in aggregDict :
                aggregDict[colCol] = []
            aggregDict[colCol].append(colOp)
            colnames.append((colOp, colName))

        df = dataFrame.groupby(self.reportDef.keyCols).agg(aggregDict).rename(columns=dict(colnames))
        df.columns = df.columns.droplevel()

        logger.debug( df )

        return df
