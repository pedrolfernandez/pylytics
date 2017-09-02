from configparser import ConfigParser


class InputReport:

    def __init__(self, configObj : ConfigParser):
        # First we filter out non desired columns
        self.columns = configObj['columns']['columns'].split(',')
        self.mappings = [ (col, configObj['mappings'][col]) for col in configObj['mappings'] ]
        self.newcols = []
        for newCol in configObj['newcols']:
            newColStrDef = configObj['newcols'][newCol]
            col = newColStrDef.split(',')[0]
            funcStr = newColStrDef.split(',')[1]
            self.newcols.append( (newCol, col, funcStr) )
        self.filter=None
        if configObj['filter'] and configObj['filter']['filter']:
            self.filter=configObj['filter']['filter']
