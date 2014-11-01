from time import sleep
from multiprocessing.pool import ThreadPool
import gc

from memory_profiler import profile
import requests


@profile
def garbage_collect(url):
    """garbage collect on every 100th query"""
    i = url.split('?gws_rd=ssl#q=')[1]
    if int(i) % 100 == 0:
        gc.collect()


@profile
def google_search(url):
    #: No, let's not slash-dot our friend google
    sleep(0.5)

    r = requests.get(url)
    garbage_collect(url)
    return r.content


@profile
def main():
    pool = ThreadPool(10)
    base_url = 'https://www.google.com/?gws_rd=ssl#q='
    urls = [base_url+str(i) for i in xrange(1000)]
    pool.map(google_search, urls)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
