# gdcp
An scp-like tool to interact with Google Drive from the command-line (Google Drive cp).

Notable features:

* supports large file uploads and downloads
* optional MD5 checksum verification for uploads and downloads
* recursive folder upload and download
* recursive depth-limited folder listing

## Installation
`gdcp` is a python script which depends on

* Python 2.7
* [PyDrive](https://pypi.python.org/pypi/PyDrive)

The easiest way to install `PyDrive` is with `pip`.

    $ pip install pydrive

**N.B.** `PyDrive` and its dependencies (notably `six`) may not install correctly in OS X when using system Python and `pip`. To get around this, use a non-system Python (e.g. from [MacPorts](https://www.macports.org/) or [Homebrew](http://brew.sh/)) and/or use [virtualenv](https://virtualenv.pypa.io/en/latest/). See [pypia/pip#2468](https://github.com/pypa/pip/issues/2468) for more details.

If `pip` is not already installed on your system, it should be possible to install it with `easy_install`.

    $ easy_install pip

These commands may require superuser privileges (e.g. `sudo`) if you wish to install to system locations. Otherwise, install libraries with `--user` to install to your home directory or install libraries in an isolated Python environment with `virtualenv`.

Now place `gdcp` somwhere in your path.  For example, if `~/bin` is in your path

    $ git clone https://github.com/ctberthiaume/gdcp.git
    $ cp gdcp/gdcp ~/bin

## Usage
Refer to the `gdcp` built-in help

    $ gdcp -h

or for subcommand help

    $ gdcp <subcommand> -h
