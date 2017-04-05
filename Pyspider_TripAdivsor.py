# -*- encoding: utf-8 -*-
# Project: TripAdvisor

from pyspider.libs.base_handler import *
import pymongo

class Handler(BaseHandler):
    crawl_config = {
    }
    
    client = pymongo.MongoClient('localhost')
    db = client['trip']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.tripadvisor.cn/Attractions-g186338-Activities-c47-London_England.html', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc(' .property_title > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)
        
        next = response.doc('.pagination .nav.next').attr.href
        self.crawl(next, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        
        name = response.doc('h1').text()
        rating = response.doc('.heading_ratings .more').text()
        address = response.doc('.addressReset > span > .format_address').text()
        phone = response.doc('.phoneNumber').text()
        duration = response.doc('div.above_fold_listing_details > div > div:nth-child(5) > div > div:nth-child(1)').text()
        introduction = response.doc('#OVERLAY_CONTENTS .listing_details > p').text()
        
        return {
            "url": response.url,
            "name": name,
            "rating": rating,
            "address": address,
            "phone": phone,
            "duration": duration,
            "introduction": introduction,
        }
    def on_result(self, result):
        if result:
            self.save_to_mongo(result)
            
    def save_to_mongo(self, result):
        if self.db['longdon'].insert(result):
            print('saved to mongo',result)
