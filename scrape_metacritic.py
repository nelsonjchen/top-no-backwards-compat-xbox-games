import scrapy


class MetacriticXbox360GameScoreScraper(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/all/xbox360/filtered?page=0']

    def parse(self, response):
        body = response.css('#main > div.module.filter.score_filter > div.module.products_module.list_product_condensed_module > div.body')
        for product in body.css('li.product'):
            title_element = product.css('.basic_stat.product_title')
            title = title_element.css('a ::text').extract_first().strip()
            user_score = product.css('.product_avguserscore > span.data.textscore ::text').extract_first()
            # Just multiply it up by 10.
            user_score = user_score.replace('.', '')
            critic_score = product.css('.basic_stat.product_score.brief_metascore > div::text').extract_first()
            yield {
                'title': title,
                'user_score': user_score,
                'critic_score': critic_score,
            }

        for next_page in response.css('a.action[rel=next]'):
            yield response.follow(next_page, self.parse)