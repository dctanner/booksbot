# -*- coding: utf-8 -*-
import scrapy

class ListingsSpider(scrapy.Spider):
    name = "listings"
    allowed_domains = ["getapp.com"]
    start_urls = [
        'https://www.getapp.com/business-intelligence-analytics-software/analytics/',
    ]

    def parse(self, response):
        for listing_url in response.css("a.serp-read-more ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(listing_url), callback=self.parse_listing_page)
        next_page = response.css("ul.pagination > li:last-child > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_listing_page(self, response):
        item = {}
        listing = response.css("div.product_main")

        item["name"] = response.css("h2 > a ::text").extract_first()
        item["desc"] = response.css("p.lead > span ::text").extract_first()
        item["rating"] = response.css('span[itemprop="ratingValue"] ::text').extract_first()
        item["num_reviews"] = response.css('meta[itemprop="ratingCount"] ::attr(content)').extract_first()

        item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
