import os
import logging

from .base import BasePackager


class Packager(BasePackager):
    def __init__(self, *args, **kwargs):
        self.extension = 'love'
        super(Packager, self).__init__(*args, **kwargs)

    def package(self):
        name = self.get_package_name(
            with_compression=False) + '.' + self.extension
        build_path = os.path.join(self.build_dir, name)
        if os.path.exists(build_path):
            logging.info('Removing older package (%s)' % build_path)
            os.remove(build_path)

        logging.info('Creating .love file (%s)' % build_path)
        excludes = self.package_config.get('exclude', [])
        if excludes:
            excludes = excludes.split(',')
        self.zip_dir(
            self.source_dir,
            build_path,
            excludes=excludes)

        logging.info('Done.')
