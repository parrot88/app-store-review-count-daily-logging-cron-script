## coding: UTF-8
import download
import csvFile

##日本、アメリカAppStoreレビュー数を取得する
if __name__ == "__main__":
    dl = download.Downlaod()
    ## レビュー数を取得
    dl.getReviewCountAll()  
    ## レビューコメントの数を取得する
    dl.getReviewCommentCountAll()
    ## dat.csvで前回の記録と比較しなにか違えば追記を行う
    cf = csvFile.CsvFile()
    cf.loadRecord()
    if dl.reviewCountJP != cf.reviewCountJP or dl.reviewCountUS != cf.reviewCountUS or dl.reviewCommentCountJP != cf.reviewCommentCountJP or dl.reviewCommentCountUS != cf.reviewCommentCountUS:
        cf.saveNewRecord(dl.reviewCountJP,dl.reviewCountUS,dl.reviewCommentCountJP,dl.reviewCommentCountUS)
    #print("done")
