## coding: UTF-8
import const
from csv import reader
import datetime

class CsvFile:
    ## --------------------------------------------------------------------
    newRow = None
    timeStamp = None
    reviewCountJP = 0
    reviewCountUS = 0
    reviewCommentCountJP = 0
    reviewCommentCountUS = 0
    ## --------------------------------------------------------------------
    def __init__(self):
        pass

    def loadRecord(self):
        with open(const.const.dat_csv_file, "r") as f:
            data = reader(f)
            for row in data:
                self.newRow = row
        print(self.newRow)
        self.timeStamp = row[0]
        self.reviewCountJP = int(row[1])
        self.reviewCountUS = int(row[2])
        self.reviewCommentCountJP = int(row[3])
        self.reviewCommentCountUS = int(row[4])
    
    def saveNewRecord(self,reviewCountJP,reviewCountUS,reviewCommentCountJP,reviewCommentCountUS):
        self.reviewCountJP = reviewCountJP
        self.reviewCountUS = reviewCountUS
        self.reviewCommentCountJP = reviewCommentCountJP
        self.reviewCommentCountUS = reviewCommentCountUS
        self.writeNewRecord()
        pass    

    def writeNewRecord(self):
        dt_now = datetime.datetime.now()
        self.timeStamp = dt_now.strftime('%Y%m%d-%H:%M:%S')
        newDat = str(self.timeStamp)+","+str(self.reviewCountJP)+","+str(self.reviewCountUS)+","+str(self.reviewCommentCountJP)+","+str(self.reviewCommentCountUS)
        #newDat = str(self.timeStamp)+","+self.reviewCountJP+","+self.reviewCountUS+","+self.reviewCommentCountJP+","+self.reviewCommentCountUS
        with open(const.const.dat_csv_file, "a") as f:
            data = reader(f)
            print(newDat, file=f)
    
if __name__ == "__main__":
    cf = CsvFile()
    cf.loadRecord()
    cf.writeNewRecord()
    pass
