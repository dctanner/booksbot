# -*- coding: utf-8 -*-
import scrapy

class ListingsSpider(scrapy.Spider):
    name = "listings"
    allowed_domains = ["getapp.com"]
    start_urls = [
        'https://www.getapp.com/business-intelligence-analytics-software/data-quality/'
    ]

    def parse(self, response):
        for listing_url in response.css("a.serp-read-more ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(listing_url), callback=self.parse_listing_page, meta={'start_url':response.url})
        next_page = response.css("ul.pagination > li:last-child > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_listing_page(self, response):
        item = {}
        listing = response.css("div.product_main")

        item["name"] = response.css("h2 ::text").extract_first()
        item["logo"] = response.css("div#apps img.img-responsive.img-fluid ::attr(data-src)").extract_first()
        item["desc"] = response.css("p.lead > span ::text").extract_first()
        item["rating"] = response.css('span[itemprop="ratingValue"] ::text').extract_first()
        item["num_reviews"] = response.css('meta[itemprop="ratingCount"] ::attr(content)').extract_first()
        item["website_click_out"] = response.css('a.btn-primary[data-evca="ua_click_out"] ::attr(href)').extract_first()
        item["category"] = response.meta['start_url']
        yield item
