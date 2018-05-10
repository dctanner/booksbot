# -*- coding: utf-8 -*-

BOT_NAME = 'getapp_scrapy'

SPIDER_MODULES = ['getapp_scrapy.spiders']
NEWSPIDER_MODULE = 'getapp_scrapy.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

RETRY_TIMES = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 10
RANDOMIZE_DOWNLOAD_DELAY = True
# DOWNLOAD_DELAY = 1
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '46d8f62db0fc4bfa94ffd26b5acff161'
DOWNLOADER_MIDDLEWARES = {
    # The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560,
    'scrapy_crawlera.CrawleraMiddleware': 610
}
