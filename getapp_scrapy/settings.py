# -*- coding: utf-8 -*-

BOT_NAME = 'getapp_scrapy'

SPIDER_MODULES = ['getapp_scrapy.spiders']
NEWSPIDER_MODULE = 'getapp_scrapy.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

CONCURRENT_REQUESTS_PER_DOMAIN = 1
RANDOMIZE_DOWNLOAD_DELAY = False
DOWNLOAD_DELAY = 1
DOWNLOADER_MIDDLEWARES = {
    # The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'getapp_scrapy.middlewares.CloudFlareMiddleware': 560
}
