# Changelog or What's New

> NOTE: **What is a Changelog?** A
> [changelog](https://keepachangelog.com/en/1.0.0/) is a curated list of
> notable changes, typically ordered by date or version. For the
> purposes of this site, I'm going to try and add an entry anytime I add
> or substantially update something. I thought about just stuffing the
> Git logs into this, but that has a lot more noise in it than most
> people want to read.
>
> This changelog will be kept in reverse chronological order, with the
> newest things on top. 
>
> If you wish to use an [RSS reader](https://newsblur.com/), and _you
> should_, there is an RSS feed of both [new
> things](/feed_rss_created.xml) and [updated
> things](/feed_rss_updated.xml).

### 2023-12-27

* Wrote up the [Pmod
  "standard"](electronics/connectors/standard-pmod.md) since I've found
  it a bit confusing at times, and it's quite common in the FPGA world. 
* Covered [logic levels](electronics/logic-levels.md) with a bit on the
  74-series families that implement them since they're the most common
  basic blocks.

### 2023-12-13

* Added [a new design](3d/my-designs.md) for the Rigol DHO800/900 series
  scopes.

### 2023-12-01

* Updated the [Fusion360 CSV to import for metric
  fasteners](3d/fusion360.md#default-user-parameters). This now includes
  M2-M12 clearance holes in normal, close, and loose.

### 2023-11-11

* Started a little [today I learned](til.md) page to collect some little
  things. I really need to figure out how to make it a bit more
  discoverable, but for now, I just want to make it super simple.
  
### 2023-10-20

* Added a quick tip from
  [Blondihacks](https://www.youtube.com/blondihacks) for storing
  sandpaper and emery cloth.

### 2023-09-11

* Started collection [tips and
  tricks](organization/random-tips-and-tricks.md) around organization
  that I've seen.
  
### 2023-09-09

* Added a [writeup](tools/workstation.md) of my workstation setup.
  Nothing too fancy, but I figured it'd be an interesting discussion
  give it's been recently updated.
* Added a [few new
  extensions](3D/fusion360.md#add-ons-and-extensibility) to my Fusion
  360 information.

### 2023-09-03

* Wrote up [cleaning up some cheap telescoping hole
  gauges](projects/decrunching-telescoping-gauges/index.md) I picked up
  cheap at a garage sale.
  
### 2023-09-01

* [Wrote up my experiment with multiple PCB
  suppliers](electronics/pcb/supplier-comparison.md). I sent the same
  small PCB to 3 different suppliers and saw how they dealt with it, and
  what they produced.
* [Documented a new approach to sorting box
  inventory](organization/inventory.md#storage-boxes) that seems to be
  really working well for me. It does require a little specialized
  equipment, but it's not prohibitively expensive.
  
### 2023-08-23

* Added a small
  [tip](electronics/random-tips-and-tricks.md#parts-management) about
  sorting SMD parts and reducing static cling.
* Minor link cleanup. There were a few broken links.

### 2023-08-21

* [A few new YouTube channels](resources/video.md).
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
* Added a quick update to the
  [labeling](organization/labeling.md#labeling) section about how to
  keep all the labels together to simplify batch printing.

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
  Schwartz](https://en.wikipedia.org/wiki/Aaron_Swartz), who was taken
  too soon (f- you MIT and feds), and others who contributed to this
  amazing tech.