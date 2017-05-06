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
The name of the files will always be the date creation, plus a counter to be used in case there are multiple files create at the exact same time. This date is extracted from the media file meta-information using [`exiftool`](http://www.sno.phy.queensu.ca/~phil/exiftool/). The service will create the type folders (`Pictures` or `Videos`) and year folder.
As you might have noticed, the file `Funny-thing.gif` has been ignored, as the `.gif` extension is not included in the configuration. Also notice that the original files has been deleted (moved as opposed to copied).

### The shrinker
Most of the camera does not compress the pictures of videos. While the size of a picture file is fairly small, the video files can grow and grow endless. My Canon Ixus generates a nearly 2GB file for 10 minutes of video 720p. That's way too much.
Part of the job of this script is to reduce the size of the files, either pictures or videos, without losing quality. I have called this service _the shrinker_.
The shrinker works basically like the renamer: it reads all the media files in a given directory, does some stuff to each file, and moves it to a different location. In this case, the service reduces the size of the files, depending on its type:
#### Pictures
At the moment, there is no shrinker for pictures. Being exact, there is a shrinker, but it does nothing (just moves the file).
#### Videos
The video shrinker uses the tool [`HandBrake`](https://handbrake.fr/) to transform the original video into a reduced one. There are a couple of configuration parameters that can be used to tweak the transformation:
```
handbrake.profile=Very Fast 720p30
handbrake.destination.extension=mp4
```
You can find more information about the _HandBrake_ profiles in [the documentation](https://handbrake.fr/docs/en/1.0.0/).

### The classifier
Finally, the third and last service is _The classifier_. This is probably the simplest, as its own purpose is to move the _shrinked_ files to the final location. I decided to do this part as an extra service because the final location of my own files is out of the computer where the service are executed (I have the backup in a NAS). I didn't want to link the job of reducing the size of the videos with the transference to the NAS. If for some reason there is no communication with the NAS (the router is down, the NAS is off), it will be this service that fails, but the shrinker could carry on transforming videos without errors.
The result of the execution of this service is that the pictures and videos are moved to a safe place, where the will wait for another service to upload them to Flickr. But this is [another project](https://github.com/nadaesposible/flickr-uploader).

## Dependencies
If you want to run these scripts, there are a number of dependencies that you will need to fulfill.
* Python 2.7.
* `exiftool`. You can find this handy tool in your OS.
* `HandBrake`. This tool has a nice GUI, but we just need the CLI to be installed.

## Scheduling the execution
Although you can run these three services separately by manually executing the corresponding runner (`RunRenamer`, `RunShrinker` or `RunClassifier`), the idea is that they run on their own. I suggest you to configure your `cron` or any other job scheduler to run the three services. Here is an example:
```
15 * * * *   /opt/media-organiser/RunRenamer.py
30 * * * *   /opt/media-organiser/RunShrinker.py
45 * * * *   /opt/media-organiser/RunClassifier.py
```
Every service is independent, that is, it does not need to wait for the previous service to finish. If, for instance, the classifier runs before the shrinker has finished, it will only classify the media files that have been already shrinked. Even if there are no files at all, the classifier service will not fail -- it will simple do nothing.

## Error log
All three services write log traces to `~/.media-organiser.log` (this is configurable). The default level is `ERROR`. If you want to be informed by email of any error log written in that file, you can use a the [log monitor](https://github.com/nadaesposible/log-monitor). This will check the file and send an email if something went wrong. More information in the [project page](https://github.com/nadaesposible/log-monitor).

## TO-DO and improvements
I did this just for fun. There are many things that could be improved and there also are many extra features to be added. I wanted to have a production ready script working as soon as possible, and then take my time to improve things. Here is some of them.

* Remove code duplication: there is some code duplication that I would like to get rid of. In essence, the services are very similar, hence there is room for improve the reusability.
* I haven't tested any of this on Windows. I have a MacBook and a couple of Linux boxes where the scripts work well.
* Improve the documentation, perhaps adding some diagrams.
* Add statistics of processed files, etc.
* Add more points to this list.
