from icrawler.builtin import GoogleImageCrawler


def main():
    word = '치킨'
    dir_name = 'jinwoo'

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': dir_name})

    google_crawler.crawl(keyword=word, offset=0, max_num=1000,
                         min_size=(200, 200), max_size=None, file_idx_offset=0)


if __name__ == "__main__":
    main()
