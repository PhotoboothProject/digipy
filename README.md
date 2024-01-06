# digipy

This tool is a small wrapper around the [digicamcontrol.com](https://digicamcontrol.com/) API.
It is used to control my Canon EOS 600D camera in my [photobooth](https://github.com/PhotoboothProject/photobooth) setup.

## install

There are two ways to use this.

1. From Source
2. Packaged pyinstaller version (easier)

### From source

1. Download python 11 from [here](https://www.python.org/downloads/windows/)
2. Install python
3. Download the [digipy](./digipy) directory and [start script](./bin/digipy)
4. Put these files into `C:\Apache24\htdocs\api\`

### Packaged version

Download the packaged exe file from [here](https://github.com/dadav/digipy/releases) and put it in your api directory (usually `C:\Apache24\htdocs\api\`).

## Usage

You need to give digipy the following informations:

Which **mode** you want to use, [slc](https://www.digicamcontrol.com/doc/userguide/singlecmd) or [cmd](https://www.digicamcontrol.com/doc/userguide/web).

The cmd or slc command you want to use.

And the parameters you want to use.

### Examples

```bash
# change the session folder to c:\foo\bar
digipy slc set session.folder c:\foo\bar

# list available cameras
digipy slc list cameras

# capture photo and save it to c:\foo.jpg
digipy slc capture c:\foo.jpg
```

### Photobooth

Adjust the commands in your photobooth setup to this:

```bash
# Before photo command
digipy cmd LiveViewWnd_Show

# Capture command
digipy slc capture %s

# Before photo command
digipy cmd LiveViewWnd_Show
```
