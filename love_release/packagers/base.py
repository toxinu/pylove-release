import os
import zipfile
from ..manager import Manager


class BasePackager(object):
    def __init__(self, system, config, package_config):
        self.system = system
        self.config = config
        self.package_config = package_config
        self.manager = Manager()

        if not hasattr(self, 'compressions'):
            self.compressions = []

        self.build_dir = os.path.realpath(self.config.get('build_dir'))
        self.source_dir = os.path.realpath(self.config.get('source_dir'))

        if not self.config.get('source_dir'):
            raise Exception('Need source_dir in general config')
        if not self.config.get('build_dir'):
            raise Exception('Need build_dir in general config')

        if self.package_config.get('compress'):
            if not self.package_config.get('compression') in self.compressions:
                raise Exception("Compression %s not available (%s)" % (
                    self.package_config.get('compression'),
                    ', '.join(self.compressions)))

        if not os.path.exists(self.config.get('build_dir')):
            os.makedirs(self.config.get('build_dir'))

    def prepare_love_binary(self):
        if self.package_config.get('custom_love_binary'):
            p = os.path.realpath(
                self.package_config.get('custom_love_binary'))
            with zipfile.ZipFile(p, "r") as z:
                z.extractall(self.manager.cache_dir)
            return os.path.splitext(p)[0]
        else:
            self.manager.get(self.system, self.config.get('love_version'))
            p = os.path.realpath(os.path.join(
                self.manager.cache_dir, self.manager.get_folder_name(
                    self.system, self.config.get('love_version'))))
            return p

    def get_package_name(self, with_compression=True):
        base_name = self.package_config.get('name')
        if with_compression and self.package_config.get('compress'):
            base_name += '.zip'
        return base_name

    def zip_dir(self, src, dst):
        zip_file = zipfile.ZipFile(dst, 'w')

        initial_dir = os.getcwd()
        os.chdir(os.path.join(src, '..'))

        for root, dirs, files in os.walk(os.path.basename(src)):
            for f in files:
                zip_file.write(os.path.join(root, f))
        zip_file.close()

        os.chdir(initial_dir)
