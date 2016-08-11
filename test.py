__author__ = 'KurtXu'

import scrapebid
import pymysql
import datetime
import logging

# db_connection = {"host": {}, "user": {}, "passwd": {}, "db": {}, "table": {}}
# scrapebid.retrieve_db_config("local_line", db_connection)
# print(db_connection)
#
# conn = pymysql.connect(host = db_connection["host"], user = db_connection["user"], passwd = db_connection["passwd"], db = "pymysql")
# cur = conn.cursor()
# cur.execute("USE pymysql")
#
# url = "http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&displayZone=&zoneId=&pppStatus=&agentName="
#
# str = "insert into test (test) VALUES (%s)" % url
# str2 = "insert into test (test) values (\"http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&displayZone=&zoneId=&pppStatus=&agentName=\")"
# print(str)
# cur.execute(str2)
# # cur.execute(str)
# cur.connection.commit()
#
# cur.close()
# conn.close()

# scrapebid(url)
# scrape_bid.scrape_page_number(url)
# http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=1&dbselect=infox&kw=&buyerName=&projectId=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&bidSort=0&pinMu=0&bidType=0&displayZone=&zoneId=&pppStatus=&agentName=
# http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=5&dbselect=infox&kw=&buyerName=&projectId=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&bidSort=0&pinMu=0&bidType=0&displayZone=&zoneId=&pppStatus=&agentName=



# url = "http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=104&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2016%3A8%3A10&end_time=2016%3A8%3A10&timeType=0&displayZone=&zoneId=&pppStatus=&agentName="
url = "http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=72&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2016%3A8%3A8&end_time=2016%3A8%3A8&timeType=0&displayZone=&zoneId=&pppStatus=&agentName="
header = "123"

# # log = logging.getLogger("test.py")
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
# log.debug('debug message')
# log.info('info message')
# log.warning('warning message')
# log.error('error message')
# log.critical('critical message')

# print(datetime.timedelta(days=1))
# print(datetime.date.today()-datetime.timedelta(days=1))
# print(scrapebid.generate_query_date(datetime.date.today()-datetime.timedelta(days=1)))

# def func(date = datetime.date.today(), index = 1):
#     print(date, index)
#     return
#
# func()

# scrapebid.scrape_bid()
# scrapebid.scrape_bid(datetime.date.today()-datetime.timedelta(days=10))

# scrapebid.scrape_bid_1page(url)
# print(scrapebid.generate_url(1))


# SQL_str_bid = "(%s,%s)," % (url, header)
# print(SQL_str_bid)
# print(SQL_str_bid.strip(','))




