PyLove-Release
==============

This is a Python application that help you to distribute your `Love2D`_ game for multiple platforms.

All your builds are driven by a configuration file.

Features:

- Windows (32&64), Linux, OSX supported (more are coming)
- Customisable via configuration file
- Easily hackable
- Create compressed package or not
- Exclude files or directorires by platform specifics
- Pining love version

Usage
-----

Create your configuration file:

::

    love-release init --config=config.ini

::

    cat config.ini  # Truncated
    [general]
    # - name: Game name
    # - version: Game version
    # - copyright: Game copyright
    # - love_version: Version of Love2D to retrieve
    # - build_dir: Relative or absolute path to a build directory
    # - source_dir: Relative or absolute path to game source directory
    name = Invaders
    version = 0.0.1
    copyright = © 2014 Socketubs
    love_version = 0.9.1
    build_dir = build
    source_dir = source

    [...]

    [package:win32]
    # A .exe binary for Windows 32bit platform.
    #
    # - name: Package name
    # - exclude: Comma separated values of regexp path to exclude in package
    # - compress: Will provide compressed archive
    # - compression: Only zip is available
    # - custom_love_binary: Relative or absolute path to love zipped archive
    #                       Extracted folder must have same name as
    #                       zip without .zip
    name = Invaders-win32
    compress = true
    compression = zip

    [...]

You'll have a nicely documented ``.ini`` file. Let's build Windows 32 package:

::

    love-release build win32 --config=config.ini
    INFO:root:Love binary archive already in cache.
    INFO:root:Extracting love binary archive (/home/socketubs/Documents/pylove-release/cache/love-0.9.1-win32.zip)
    INFO:root:Removing older package (/home/socketubs/Documents/pylove-release/build/Invaders-win32)
    INFO:root:Creating .love file (/home/socketubs/Documents/pylove-release/build/Invaders-win32/Invaders.love)
    INFO:root:Done.
    INFO:root:Creating .exe file (/home/socketubs/Documents/pylove-release/build/Invaders-win32/Invaders.exe)
    INFO:root:Copying dlls
    INFO:root:Creating .zip file (/home/socketubs/Documents/pylove-release/build/Invaders-win32.zip)
    INFO:root:Done.

Installation
------------

Not on Pypi for now. Clone this repository and install it with ``python setup.py install``.

Packagers
---------

You can easily add your very own packager. Take a look at ``love_release/packagers`` directory.
More documentations are coming.

More packages are coming, OSX, Android, Linux, Deb, Rpm, etc...

.. _LOVE2D: http://love2d.org/
