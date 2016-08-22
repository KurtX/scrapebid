__author__ = 'KurtXu'

import datetime
import configparser
import pymysql
import time
import logging
import urllib.request
from bs4 import BeautifulSoup
from logging.handlers import TimedRotatingFileHandler


def get_logger():
    log_format = '[%(asctime)s][%(filename)s][line:%(lineno)d][func:%(funcName)s()][%(levelname)s]: %(message)s'

    handler = TimedRotatingFileHandler('scrapebid.log', 'midnight', 1)
    handler.suffix = "%Y-%m-%d.log"
    handler.setFormatter(logging.Formatter(log_format))

    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(log_format))

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(logging.DEBUG)
    return logger


def retrieve_db_config(line_name, db_connection):
    cfg = configparser.ConfigParser()
    cfg.read("db_conf.cfg")
    db_connection["host"] = cfg.get(line_name, "host")
    db_connection["user"] = cfg.get(line_name, "user")
    db_connection["passwd"] = cfg.get(line_name, "passwd")
    return


def scrape_page_number(url):
    html = request_url(url)
    bsObj = BeautifulSoup(html, "html.parser")
    str(bsObj)
    pager = bsObj.find("p", {"class", "pager"})
    # print(pager.get_text())  # pager_str = "Pager({size:318, current:0, prefix:'data2',suffix:'.jsp&'});"
    pager_str = pager.get_text()
    index1 = pager_str.find("size:")
    index1 += 5
    index2 = pager_str.find(",")
    # size = pager_str[index1,index2]
    page_number = pager_str[index1: index2]
    return int(page_number)


def request_url(url):
    request = urllib.request.Request(url)
    request.add_header('Host', 'search.ccgp.gov.cn')
    request.add_header('Connection', 'keep-alive')
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    request.add_header('Referer', 'http://www.ccgp.gov.cn/')
    html = urllib.request.urlopen(request)
    return html


def generate_query_date(date=datetime.date.today()):
    query_date = "&start_time=%d%%3A%d%%3A%d&end_time=%d%%3A%d%%3A%d" \
                 % (date.year, date.month, date.day, date.year, date.month, date.day)
    return query_date


def scrape_bid_1page(url):
    html = request_url(url)
    bsObj = BeautifulSoup(html, "html.parser")
    str(bsObj)
    bsbids = bsObj.find("ul", {"class", "vT-srch-result-list-bid"})

    SQL_str = "INSERT INTO tb_bid (url, title, abstract, datetime, location, type, buyer, pinmu, created) VALUES"

    created = datetime.date.today()

    for bid in bsbids.select("li"):
        # bid basic info, string op
        bidspan = bid.span.get_text()
        index_1st_separator = bidspan.find("|")
        index_buyer = bidspan.find("采购人：")
        lens = len("采购人：")
        index_2nd_separator = bidspan.find("|", index_buyer)
        index_last_separator = bidspan.rfind("|")

        bid_url = bid.a.get("href")
        bid_title = bid.a.string
        bid_abstract = bid.p.string  # <p></p> maybe null
        if bid_abstract is None:
            bid_abstract = "null"
        bid_abstract = bid_abstract.strip().strip('?').replace('"', '*').replace('\\', '/')
        bid_datetime = bidspan[0:index_1st_separator]
        bid_buyer = bidspan[index_buyer + lens:index_2nd_separator]
        bid_location = bid.span.a.get_text()
        bid_type = bid.span.strong.get_text()
        bid_pinmu = bidspan[index_last_separator + 1:]

        SQL_str_bid = "(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")," % (
            bid_url,
            bid_title.strip().replace('"', '*'),
            bid_abstract,
            bid_datetime.strip(),
            bid_location.strip().replace('"', '*'),
            bid_type.strip().replace('"', '*'),
            bid_buyer.strip().replace('"', '*'),
            bid_pinmu.strip().replace('"', '*'),
            created)

        # print(SQL_str_bid)
        SQL_str += SQL_str_bid

    record_bid_into_db(SQL_str.strip(','))
    return


def record_bid_into_db(SQL_str):
    db_connection = {"host": {}, "user": {}, "passwd": {}, "db": {}, "table": {}}
    retrieve_db_config("local_line", db_connection)
    conn = pymysql.connect(host=db_connection["host"],
                           user=db_connection["user"],
                           passwd=db_connection["passwd"],
                           db="BID")
    conn.set_charset('utf8')
    cur = conn.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute("USE BID")
    cur.execute(SQL_str)
    cur.connection.commit()
    cur.close()
    conn.close()
    return


def generate_url(query_date=datetime.date.today(), page_index=1):
    request_url = "http://search.ccgp.gov.cn/dataB.jsp"
    request_parameter_search_type = "?searchtype=2"
    request_parameter_page_index = "&page_index="
    request_parameter_bid_sort = "&bidSort=0"
    request_parameter_buyer_name = "&buyerName="
    request_parameter_project_id = "&projectId="
    request_parameter_pin_mu = "&pinMu=0"
    request_parameter_bid_type = "&bidType=0"
    request_parameter_db_select = "&dbselect=bidx"
    request_parameter_kw = "&kw="
    request_parameter_query_date = ""
    request_parameter_time_type = "&timeType=0"
    request_parameter_display_zone = "&displayZone="
    request_parameter_zone_id = "&zoneId="
    request_parameter_ppp_status = "&pppStatus="
    request_parameter_agent_name = "&agentName="

    url = request_url \
          + request_parameter_search_type \
          + request_parameter_page_index + str(page_index) \
          + request_parameter_bid_sort \
          + request_parameter_buyer_name \
          + request_parameter_project_id \
          + request_parameter_pin_mu \
          + request_parameter_bid_type \
          + request_parameter_db_select \
          + request_parameter_kw \
          + generate_query_date(query_date) \
          + request_parameter_time_type \
          + request_parameter_display_zone \
          + request_parameter_zone_id \
          + request_parameter_ppp_status \
          + request_parameter_agent_name
    return url


def scrape_bid(bid_date=datetime.date.today()):
    logger = get_logger()
    page_index = 1
    page_number = scrape_page_number(generate_url(bid_date, page_index))  # get page number
    logger.debug("total page number is: %s" % page_number)
    logger.debug("begin scrape each page")
    while (page_index <= page_number):
        time.sleep(1)  # sleep 1 second
        url = generate_url(bid_date, page_index)
        logger.info("%s %03d/%d %s" % (bid_date, page_index, page_number, url))
        page_index += 1  # ++page_index must result in a infinite loop
        scrape_bid_1page(url)
    logger.debug("end scrape each page")
    return
