## coding: UTF-8
import const
import requests
import json
from collections import OrderedDict
import pprint

# https://www.sejuku.net/blog/51241

class Downlaod:
    ## --------------------------------------------------------------------
    reviewCountJP = 0
    reviewCountUS = 0
    reviewCommentCountJP = 0
    reviewCommentCountUS = 0
    ## --------------------------------------------------------------------
    def __init__(self):
        pass

    def getReviewCountAll(self):
        self.reviewCountJP = self.getReviewCount(const.const.url_jp_app_json)
        self.reviewCountUS = self.getReviewCount(const.const.url_us_app_json)

    def getReviewCount(self,url):
        r = requests.get(url)
        #print(r.content)
        d = json.loads(r.text)
        pprint.pprint(d['results'][0]['userRatingCount'], width=40)
        return d['results'][0]['userRatingCount']

    def getReviewCommentCountAll(self):
        self.reviewCommentCountJP = self.getReviewCommentCount(const.const.url_jp_comment_num)
        self.reviewCommentCountUS = self.getReviewCommentCount(const.const.url_en_comment_num)

    def getReviewCommentCount(self,url):
        r = requests.get(url)
        d = json.loads(r.text)
        count = len(d['feed']['entry']) 
        #print(count)
        return count

if __name__ == "__main__":
    dl = Downlaod()
    dl.getReviewCountAll()
    dl.getReviewCommentCountAll()
    #print("done")