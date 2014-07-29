import os
import shutil
import zipfile
import logging

import requests

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class Manager(object):
    def __init__(self, cache_dir=os.path.join('./cache')):
        self.cache_dir = os.path.realpath(cache_dir)
        self.love_url = 'https://bitbucket.org/rude/love/downloads/'
        self.systems = ['win32', 'win64', 'macosx-x64']

        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def get_folder_name(self, system, version):
        assert (
            system in self.systems), "System not available (%s)" % self.systems
        return 'love-%s-%s' % (version, system)

    def get_zip_name(self, system, version):
        assert (
            system in self.systems), "System not available (%s)" % self.systems
        return 'love-%s-%s.zip' % (version, system)

    def has(self, system, version):
        if self.get_zip_name(system, version) in os.listdir(self.cache_dir):
            return True
        return False

    def download(self, system, version):
        url = urljoin(self.love_url, self.get_zip_name(system, version))
        logging.info('Downloading %s ...' % url)
        r = requests.get(url, stream=True)
        with open(os.path.join(
                self.cache_dir,
                self.get_zip_name(system, version)), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

    def extract(self, system, version):
        assert (self.has(system, version)), "Need to download before"
        love_binary_archive_path = os.path.join(
            self.cache_dir, self.get_zip_name(system, version))
        logging.info(
            'Extracting love binary archive (%s)' % love_binary_archive_path)
        with zipfile.ZipFile(love_binary_archive_path, "r") as z:
            z.extractall(self.cache_dir)
        if system == 'macosx-x64':
            shutil.rmtree(os.path.join(self.cache_dir, '__MACOSX'))

    def get(self, system, version):
        if not self.has(system, version):
            logging.info("Not in cache. Let's download it.")
            self.download(system, version)
        else:
            logging.info("Love binary archive already in cache.")
        self.extract(system, version)
