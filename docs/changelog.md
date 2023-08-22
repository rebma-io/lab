# Changelog or What's New

> NOTE: **What is a Changelog?** A
> [changelog]([Title](https://keepachangelog.com/en/1.0.0/)) is a
> curated list of notable changes, typically ordered by date or version.
> For the purposes of this site, I'm going to try and add an entry
> anytime I add or substantially update something. I thought about just
> stuffing the Git logs into this, but that has a lot more noise in it
> than most people want to read.
>
> This changelog will be kept in reverse chronological order, with the
> newest things on top. 
>
> If you wish to use an [RSS reader](https://newsblur.com/), and _you
> should_, there is an RSS feed of both [new
> things](/feed_rss_created.xml) and [updated
> things](/feed_rss_updated.xml).

### 2023-08-21

* [Added some
  information](tools/guides/precision-voltage-and-current-signal-generator.md)
  about a rather inexpensive, but precision current and voltage source,
  so long as you can work within its limits.
* Updated the
  [mkdocs-material](https://squidfunk.github.io/mkdocs-material/changelog/#9.2.1)
  to 9.2.1, which includes all of 9.2.0 from the 9.1 release. This also
  brought in mkdocs v1.5.2. I also needed to update
  [mknotebooks](https://github.com/greenape/mknotebooks/releases/tag/0.8.0)
  to v0.8.0 to fix an import issue.

### 2023-08-20

* [Wrote up the project](projects/replacement-microscope-base/index.md)
  to replace the base of my Joyalens JL-249 10.1" video microscope. This
  added a heavy magnetic steel base as a replacement. 

### 2023-08-15

* Added a few new barcode-related [Python
  libraries](software/python/libraries.md). 
  
### 2023-08-14

* Added an [introduction to barcodes](software/barcode-formats.md), both
  1D and 2D. 

### 2023-07-28

* Added information on the [Bosch-Sortimo
  system](organization/sortimo.md), including labeling and other
  details.

### 2023-07-25

* Added information on [reference
  designators](electronics/reference-designators.md) for schematics. 
  
### 2023-07-20

* Added ITO glass to the [interesting
  materials](mechanical/materials.md) section. Super fun material used
  in touch screens and other applications.
* Added diagrams showing a visual example of the [types of
  fit](mechanical/fit.md). 
* Some coverage of screws, specifically. This includes a discussion of
  the various types, materials, thread variations, and uses. 

### 2023-07-14

* Formalized the structure of the site. Previously, I had been just
  letting MkDocs figure it out from directory structure, but this often
  led to some weird organization. While it's more work to keep a manual
  nav structure up-to-date, I think it will be more useful as a
  consumer.
* Added an RSS feed for [changes](/feed_rss_updated.xml) and
  [creations](/feed_rss_created.xml) using the
  [mkdocs-rss-plugin]([Title](https://github.com/guts/mkdocs-rss-plugin)).
  Thank you to [Aaron
  Schwartz]([Title](https://en.wikipedia.org/wiki/Aaron_Swartz)), who
  was taken too soon (f- you MIT), and others who contributed to this
  amazing tech.