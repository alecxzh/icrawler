from icrawler.builtin import BingImageCrawler


bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'image'})
bing_crawler.crawl(keyword='cat face', filters=None, offset=0, max_num=1000)

