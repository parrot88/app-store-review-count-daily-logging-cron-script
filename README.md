# app-store-review-count-daily-logging-cron-script

## Description
This is script get log review count and review comment count everyday by cron.  
(This script check Japanese, US app store,  
so if you want check other country, you can edit.)  

## Usage
1. edit your application's App Store ID with 'const.py'
> AppStoreID = 1111111111

2. set cron and give permission +x into 'do.py'
If you wanna check review at every pm 10, edit cron.
Please edit as below...
> 0 22 * * * python3 /your/project/path/do.py
And don't forget add permission +x to 'do.py'.

4. check result at 'dat.csv'  
for example:

```20200412-22:00:20,56,14,12,5
20200413-22:00:18,56,15,12,5
20200417-22:00:25,57,15,12,5
```
Log format is ... date Japan review score, US review score, Japan review comment score, US review comment score

## By the way...
I used this script at my Raspberry Pi zero w.  
That is enough spec.  
Python 3.6.5
