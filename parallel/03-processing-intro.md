# Introduction to Processing

[<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Processing_Logo_Clipped.svg/200px-Processing_Logo_Clipped.svg.png" align="left" width="75" height="75">rocessing](https://processing.org/) is the open source language developed over the Java programming language to aid teaching computer programming through visual interactions. Today we will be learning the basics of processing to aid us in understanding distributed computing. First, you need to install processing on your Raspberry Pi 2.

# Installation

There is no official ARM version of processing available, but luckily it runs in java. Processing 2.2.1 (stable) requires Oracle Java 7, so we'll need to download and install that from the Raspbian repositories.

```shell
sudo apt-get install oracle-java7-jdk
```
Now that we have java, we can download and un-tar processing.

```shell
wget http://download.processing.org/processing-2.2.1-linux32.tgz
tar -xzf processing-2.2.1-linux32.tgz
```

The -xzf parameters tell tar to e(x)tract, un(z)ip, the (f)ile: processing-2.2.1-linux32.tgz. The gz in tgz denotes a gzipped tarball. Now, we just need to link in our new Java to make it functional.

```shell
cd processing-2.2.1
rm -rf java
ln -s /usr/lib/jvm/jdk-7-oracle-armhf java
```

The ln command makes a [symbolic link](http://en.wikipedia.org/wiki/Symbolic_link) to our Oracle Java 7 without having to move or copy the installation. We can now test to make sure everything worked by launching Processing.

```shell
./processing
```
After some messages on your console, the graphical IDE pictured below should appear.

![processing IDE](images/processing.png)

IDE stands for *Integrated Development Environment* and usually allows code editing, building, and debugging all from inside the program. All of our Processing development will be taking place inside of this IDE, so you won't be learning any new keyboard shortcuts! Even though IDE development is easier, knowing how to edit text inside a terminal is invaluable when working on remote systems like stampede. Up next, we'll be making our first program, or sketch.

[:arrow_right: First Sketch](04-first-sketch.md)
