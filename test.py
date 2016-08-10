__author__ = 'KurtXu'

import scrapebid
import pymysql

# db_connection = {"host": {}, "user": {}, "passwd": {}, "db": {}, "table": {}}
# scrapebid.retrieve_db_config("local_line", db_connection)
# print(db_connection)
#
# conn = pymysql.connect(host = db_connection["host"], user = db_connection["user"], passwd = db_connection["passwd"], db = "pymysql")
# cur = conn.cursor()
# cur.execute("USE pymysql")
#
url = "http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&displayZone=&zoneId=&pppStatus=&agentName="
#
# cur.execute("insert into test (test) VALUES (%s)", url)
# cur.connection.commit()
#
# cur.close()
# conn.close()

# scrapebid(url)
# scrape_bid.scrape_page_number(url)
# http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=1&dbselect=infox&kw=&buyerName=&projectId=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&bidSort=0&pinMu=0&bidType=0&displayZone=&zoneId=&pppStatus=&agentName=
# http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=5&dbselect=infox&kw=&buyerName=&projectId=&start_time=2016%3A07%3A27&end_time=2016%3A07%3A27&timeType=0&bidSort=0&pinMu=0&bidType=0&displayZone=&zoneId=&pppStatus=&agentName=

scrapebid.scrape_bid()

# scrapebid.scrape_bid_1page(url)
# print(scrapebid.generate_url(1))