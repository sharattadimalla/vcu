from pattern.web import Crawler

class Polly(Crawler):
    def visit(self, link, source=None):
        print 'visited: ', repr(link.url), 'from: ', link.referrer
    def fail(self, link):
        print 'failed: ', repr(link.url)

p = Polly(links=['http://www.snagajob.com/'], delay=5)

while not p.done:
    p.crawl()