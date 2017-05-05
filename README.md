# Media organiser
A simple Python script used to rename, compress and classify media files (photos and videos).
## Introduction
This is a personal project created to help me with the annoying job of tiding up all my videos and pictures. I have a phone and a camera, I have Dropbox, MEGA, Flickr, Google drive, a NAS, a mini PC and a laptop. These means that my pictures and videos are all over the place. Of course, I never found them when I need them.

The idea of this script is to keep all the media files in an unique safe place, classified by date. And the most important feature: it has to be automatic. I don't want to have to worry about moving files here and there manually. I want the script to do it for me.

## Structure
The script consist of three main services:
* The renamer
* The shrinker
* The classifier

### The renamer
This service reads all the existing media files from a configured directory, rename them using the creation date, and move them to another directory where they will be classified by type (picture or video) and year.

In order not to overload the computer where the service is run, this will only rename a certain number of files per execution (this number is configurable). It will abort the execution after a number of failures (e.g. if the service does not have rights to write in the destination folder, it does not make any sense to keep trying to move 1000 files -- the service will abort after 5 failures).

This service use the following configuration parameters (the names are self-explanatory)

```
renamer.path.sources = /Users/johndoe/MEGA,/Users/johndoe/Dropbox
renamer.path.sources.file.extensions = jpg,jpeg,mov,3gp,avi,mkv,mp4
renamer.path.destination = /Users/johndoe/MediaClassifier/renamed
renamer.max.number.of.files=1000
renamer.max.number.of.errors=5
```

#### Example

Given the configuration above and the following content:

```
/Users
    /johndoe
        /Dropbox
            /My pictures
                London.jpg
                Funny-thing.gif
                /Family
                    MySon.jpeg
            /Camera
                MV_RTTI_2342.mov
        /MEGA
            photo002.jpg
            video001.avi
```
If we ejecute the renamer service...

```
$ RunRenamer.py
```
The result will be...
```
/Users
    /johndoe
        /Dropbox
            /My pictures
                Funny-thing.gif
                /Family
            /Camera
        /MEGA
        /MediaOrganiser
            /Pictures
                /2016
                    2016-03-06_11.44.19_001.jpg
                    2016-04-11_13.44.58_001.jpg
                /2017
                    2017-05-05_11.55.47_001.jpg
            /Videos
                /2015
                    2015-05-05_11.55.47_001.mov
                    2015-01-12_13.12.04_001.mov
```
The name of the files will always be the date creation, plus a counter to be used in case there are multiple files create at the exact same time. This date is extracted from the media file meta-information using `exiftool`. The service will create the type folders (`Pictures` or `Videos`) and year folder.
As you might have noticed, the file `Funny-thing.gif` has been ignored, as the `.gif` extension is not included in the configuration. Also notice that the original files has been deleted (moved as opposed to copied).

## Dependencies
* exiftool
* HandBrake

## TO-DO and improvements

* Remove code duplication
* Test it in different platforms
