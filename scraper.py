from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': 'image'})
filters = dict(
    date=((2017, 1, 1), (2017, 11, 30)))
google_crawler.crawl(keyword='cat face', filters=filters, offset=0, max_num=1000,
                     min_size=(200,200), max_size=None, file_idx_offset=0)

bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'image'})
bing_crawler.crawl(keyword='cat face', filters=None, offset=0, max_num=1000)

baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'image'})
baidu_crawler.crawl(keyword='cat face', offset=0, max_num=1000,
                    min_size=(200,200), max_size=None)