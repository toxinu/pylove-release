import os
import shutil
import logging
from .base import BasePackager
from .love import Packager as LovePackager


class Packager(BasePackager):
    def __init__(self, *args, **kwargs):
        self.extension = 'exe'
        self.love_config = kwargs.get('love_config')
        self.compressions = ['zip']
        self.love_packager = LovePackager(args[0], args[1], self.love_config)

        self.dlls = [
            'SDL2.dll',
            'license.txt',
            'DevIL.dll',
            'love.dll',
            'lua51.dll',
            'mpg123.dll',
            'OpenAL32.dll',
            'msvcp110.dll',
            'msvcr110.dll']

        super(Packager, self).__init__(*args)

    def package(self):
        love_binary_dir_path = self.prepare_love_binary()

        name = self.get_package_name(with_compression=False)
        build_dir = os.path.join(self.build_dir, name)
        exe_path = os.path.join(
            build_dir,
            self.love_config.get('name')) + '.' + self.extension

        if os.path.exists(build_dir):
            logging.info('Removing older package (%s)...' % build_dir)
            shutil.rmtree(build_dir)
        os.makedirs(build_dir)

        # Creating love file
        self.love_packager.build_dir = os.path.join(build_dir)
        self.love_packager.package()
        love_package_name = self.love_packager.get_package_name(
            with_compression=False) + '.' + self.love_packager.extension
        love_package_path = os.path.join(
            self.love_packager.build_dir, love_package_name)

        # Creating exe file
        with open(exe_path, 'wb') as output:
            logging.info('Creating .exe file...')
            with open(os.path.join(
                    love_binary_dir_path, 'love.exe'), 'rb') as love_exe:
                output.write(love_exe.read())
            with open(love_package_path, 'rb') as love_package:
                output.write(love_package.read())
        os.remove(love_package_path)

        # Copy DLL's
        for dll in self.dlls:
            shutil.copy(
                os.path.join(love_binary_dir_path, dll),
                os.path.join(build_dir, dll))

        if self.package_config.get('compress'):
            if self.package_config.get('compression') == 'zip':
                self.zip_dir(
                    build_dir,
                    os.path.join(self.build_dir, name + '.zip'))
