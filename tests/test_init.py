from pathlib import Path

import pytest

from simple_downloader import download


def test_download(tmp_path):
    # TODO: Add tests!
    fp = download("http://speedtest.ftp.otenet.gr/files/test100k.db", tmp_path)
    assert fp.exists()


def test_download_missing_target_path(tmp_path):
    p = tmp_path / "icannotimagethatafolderhasthisname"
    fp = download("http://speedtest.ftp.otenet.gr/files/test100k.db", p)
    assert fp.exists()


def test_force(tmp_path):
    fp = download("http://speedtest.ftp.otenet.gr/files/test100k.db", tmp_path)
    fp = download("http://speedtest.ftp.otenet.gr/files/test100k.db", tmp_path)
    assert fp.exists()


def test_path_to_file(tmp_path):
    fp = Path(tmp_path) / "file"
    fp.touch()
    with pytest.raises(ValueError, match="must be directory"):
        download("http://speedtest.ftp.otenet.gr/files/test100k.db", fp)
