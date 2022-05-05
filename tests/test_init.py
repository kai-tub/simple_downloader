import time

from simple_downloader import download


def test_download(tmp_path):
    # TODO: Add tests!
    fp = download("http://speedtest.ftp.otenet.gr/files/test1Mb.db", tmp_path)
    assert fp.exists()
