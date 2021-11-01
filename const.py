## coding: UTF-8

class const:
    AppStoreID = 111111111111
    url_jp_app_json = "http://itunes.apple.com/lookup?id="+str(AppStoreID)+"&country=JP"
    url_us_app_json = "https://itunes.apple.com/lookup?id="+str(AppStoreID)

    url_jp_comment_num = "https://itunes.apple.com/jp/rss/customerreviews/id="+str(AppStoreID)+"/json"
    url_en_comment_num = "https://itunes.apple.com/rss/customerreviews/id="+str(AppStoreID)+"/json"

    dat_csv_file = "dat.csv"
