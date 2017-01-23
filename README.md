# gdcp

gdcp (**G**oogle **D**rive **cp**) is a command-line tool that supports robust and fast file transfers to and from Google Drive, somewhat analogous to using `scp` to transfer files to and from a Linux/Unix server. It is designed to be used in a workflow where large data sets stored in Google Drive are downloaded to a server for processing and results are uploaded back to Google Drive.


Notable features:

* supports large file transfers
* MD5 checksum verification
* recursive folder upload and download
* recursive depth-limited folder listing
* recursive ownership transfer
* compensates for errors during uploads and downloads, resuming partial transfers when possible and retrying complete transfers otherwise

## Installation
`gdcp` is a python script which depends on

* Python **2.7**. **Python 3 is not supported**. If you see syntax errors about exception handling or print statements make sure `gdcp` is not being run with Python 3.
* [PyDrive](https://pypi.python.org/pypi/PyDrive)
* [backoff](https://pypi.python.org/pypi/backoff)

The easiest way to install Python dependencis is with `pip`.

```
$ pip install pydrive
$ pip install backoff
```

**OS X Note** `PyDrive` and its dependencies (notably `six`) may not install correctly in OS X when using system Python and `pip`. To get around this, use a non-system Python (e.g. from [MacPorts](https://www.macports.org/) or [Homebrew](http://brew.sh/)) and/or use [virtualenv](https://virtualenv.pypa.io/en/latest/). See [pypia/pip#2468](https://github.com/pypa/pip/issues/2468) for more details.

If `pip` is not already installed on your system, it should be possible to install it with `easy_install`.

```
$ easy_install pip
```

These commands may require superuser privileges (e.g. `sudo`) if you wish to install to system locations. Otherwise, install libraries with `--user` to install to your home directory or install libraries in an isolated Python environment with `virtualenv`.

Now place `gdcp` somwhere in your path.  For example, if `~/bin` is in your path

```
$ git clone https://github.com/ctberthiaume/gdcp.git
$ cp gdcp/gdcp ~/bin
```

## Usage

### Setup
The first time you run `gdcp` a new directory `~/.gdcp/` will be created and you'll be greeted with the following instructions for obtaining your own OAuth2 client ID.

```
- Visit https://console.developers.google.com/
- Create a new project and select it
- Under 'APIs' make sure the 'Drive API' is turned on
- Under 'Credentials' create a new OAuth client ID
  Choose 'Installed -> Other' for application type
- Click 'Download JSON' to download the secrets file
- Copy the secrets file to ~/.gdcp/client_secrets.json
```

Once you've created `~/.gdcp/client_secrets.json`, run `gdcp` again to authorize access to your Google Drive. You should see something like

```
Go to the following link in your browser:
```

followed by a long URL. Visiting this URL in a browser where you're already logged into your Google account will yield a verification code. Copy and paste this code into the terminal to complete the authentication process. A new file, `~/.gdcp/credentials.json`, will be created which grants access to your Google Drive files. If you want to use `gdcp` on a different computer without going through authentication again, just copy `~/.gdcp/` to the new computer.

### Subcommands

#### list
List file metadata. For example, to list information about a Googel Drive folder with ID `0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp`.

```
$ gdcp list -i 0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp
foo 0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp	folder
foo/bar.txt	0Bxt5Ia3JxzdHZGtabW9xTEduSkE	file	7	14758f1afd44c09b7992073ccf00b43d
```

This prints information about that folder and its first-level contents. Tab-delimited columns are **title**, **id**, **type**, **fileSize**, **md5Checksum**. Type will be **file** or **folder** for downloadable files and folders. For files created with a Google Apps app - documents, spreadsheets, maps, third-party apps, etc - the type reported will be the name parsed from the file's MIME type. For example, a Google Sheets file with MIME type `application/vnd.google-apps.spreadsheet` has type **spreadsheet**. To increase the depth of the recursive metadata listing specify a `--depth` value greater than 0.

#### upload
Recursively upload files or folders. For example, to upload a local folder into a Google Drive parent folder with ID `0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp`.

```
$ gdcp upload -p 0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp ./subfolder
subfolder/
subfolder/subfile.txt
  100.00% 209715200 44.08MB/s 4.76s MD5...OK
Uploaded 2 file(s) and folder(s)
```

By default `gdcp` will compare the MD5 checksum of local files against the checksum reported by Google after upload.

#### download
Recursively download files or folders. For example, to download a Google Drive folder with ID  `0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp`.

```
$ gdcp download -i 0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp .
./foo/subfolder/
./foo/subfolder/subfile.txt
  100.00% 209715200 50.32MB/s 4.17s MD5...OK
./foo/bar.txt
  100.00% 7 0.00MB/s 0.49s MD5...OK
Downloaded 4 file(s) and folder(s)
```

By default `gdcp` will compare the MD5 checksum of local files against the checksum reported by Google after download.

#### transfer
Recursively transfer ownership of files or folders to another Google Apps account. For example, to transfer folder `0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp ` and all of its contents.

```
gdcp transfer -i 0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp -e newowner@gmail.com
foo	0Bxt5Ia3JxzdHfkJDeUxCQ3RyaWp
subfolder	0Bxt5Ia3JxzdHcVJxVTRfYVdOdmc
subfile.txt	0Bxt5Ia3JxzdHN0NqUEh3RnJic28
bar.txt	0Bxt5Ia3JxzdHZGtabW9xTEduSkE
Transferred ownership for 4 file(s)
```
