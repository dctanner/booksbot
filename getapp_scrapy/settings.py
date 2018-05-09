# -*- coding: utf-8 -*-

BOT_NAME = 'getapp_scrapy'

SPIDER_MODULES = ['getapp_scrapy.spiders']
NEWSPIDER_MODULE = 'getapp_scrapy.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    # The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'scraping_hub.middlewares.CloudFlareMiddleware': 560
}
