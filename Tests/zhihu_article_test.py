import unittest

from LinkCrawler.Zhihu import ZhihuArticle


class ZhihuArticleTest(unittest.TestCase):
    def test_zhihu_artile(self):
        url = 'https://zhuanlan.zhihu.com/p/613356779'
        ZhihuArticle(url)


if __name__ == '__main__':
    unittest.main()
