from configparser import ConfigParser

# Basic supported stats in here: https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
class DataReport:

    def __init__(self, configObj : ConfigParser, reportCfgId : str):
        self.reportCfgId = reportCfgId
        self.name = configObj[reportCfgId]['name']
        self.filterExp = configObj[reportCfgId]['filter']
        self.keyCols = configObj[reportCfgId]['keys'].split(',')
        self.attrCols = [] # [ (colName, colCol, colOp) ]

        i=1
        while configObj.has_option(reportCfgId, 'col'+str(i)+'_name') :
            self.attrCols.append((configObj[reportCfgId]['col'+str(i)+'_name'],
                                  configObj[reportCfgId]['col' + str(i) + '_col'],
                                  configObj[reportCfgId]['col' + str(i) + '_op']))
            i += 1
