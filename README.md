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

The easiest way to install PyDrive is with `pip`.

    $ pip install pydrive

If `pip` is not already installed on your system, it should be possible to install it with `easy_install`.

    $ easy_install pip

These commands may require superuser privileges, e.g. `sudo`.

Now place `gdcp` somwhere in your path.  For example, if `~/bin` is in your path

    $ git clone https://github.com/ctberthiaume/gdcp.git
    $ cp gdcp/gdcp ~/bin

## Usage
Refer to the `gdcp` built-in help

    $ gdcp -h

or for subcommand help

    $ gdcp <subcommand> -h
