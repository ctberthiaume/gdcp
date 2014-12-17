# gdcp (Google Drive cp) - An scp-like tool to interact with Google Drive from the command-line

## Installation
`gdcp` is a python script which depends on [PyDrive](https://pypi.python.org/pypi/PyDrive).  The easiest way to install PyDrive is with `pip`.

    $ pip install pydrive

If `pip` is not already installed on your system, it should be possible to install it with `easy_install`.

    $ easy_install pip

These commands may require superuser privileges, e.g. `sudo`.

Now make place `gdcp` somwhere in your path and make sure it's executable.  For example, if `~/bin` is in your path

    $ git clone https://github.com/ctberthiaume/gdcp.git
    $ cp gdcp/gdcp ~/bin
    $ chmod +x ~/bin/gdcp

## Usage
Refer to the `gdcp` built-in help

    $ gdcp -h

or for subcommand help

    $ gdcp <subcommand> -h
