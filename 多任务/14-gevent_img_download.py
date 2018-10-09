import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(download, "1.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2018/09/18/963308_20180918163952_small.jpg"),
        gevent.spawn(download, "2.jpg", "https://rpic.douyucdn.cn/asrpic/181008/5324159_5737583_728aa_2_1746.jpg")
    ])


if __name__ == "__main__":
    main()