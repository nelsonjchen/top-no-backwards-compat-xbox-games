import scrapy
import re


class XboxBackwardsCompatGameScraper(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.xbox.com/en-US/xbox-one/backward-compatibility/js/bc-GamesList.js']

    def parse(self, response):
        all_titles = set(re.findall("title: '(?P<title>.*?)',", response.body.decode('utf-8')))
        for title in all_titles:
            title = title.replace('®', '')
            title = title.replace('ñ', '')
            title = title.replace('™', '')
            title = title.strip()
            yield {
                'title': title,
            }