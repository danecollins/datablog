Title: Fitbit as a Platform
Date: 2014-08-07 18:58:08
Category: posts
Tags: Fitbit, Fitness
author: Dane Collins
Summary: Using the Fitbit site as a platform

When I started using an activity monitor I was using a Nike Fuel Band.  I used it for about a year and liked it, but was not impressed by the Nike software. I decided to try out a Fitbit Flex and the Fitbit software which I found much better.

After using the Fitbit website and iPhone app for a year, I can't imagine going back, but I started worrying about being locked into another platform where I could not get my data out, or in. For example, I'd love to have my Nike+ data in my Fitbit account, so I could have the full history.

I started digging in and found a great website, the [Nike+ data exporter](https://nikeplusexporter.rhysmccaig.com/), that lets you extract your data from Nike into .csv or .json files. The .json gives you mileage and calories which is the primary data you can enter manually into the Fitbit website. It's a manual process but at least it is a path.

Of course, the next question was, if I move the data to fitbit.com can I get it out of there?

It turns out that fitbit.com has a full API that you can use to both read and write your fitness data. Now I just have to figure out how to do it! It seems there are two paths to this.

* The [fitbit dev site](http://dev.fitbit.com/) which seem javascript oriented
* The [Python API](http://python-fitbit.readthedocs.org/en/latest/)

In selecting a tracker, I think it's crucial to think about the long-term access to your data and the Fitbit API makes me feel much more comfortable about using Fitbit for my data.