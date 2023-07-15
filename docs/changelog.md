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


### 2023-07-14 16:20

* Formalized the structure of the site. Previously, I had been just
  letting MkDocs figure it out from directory structure, but this often
  led to some weird organization. While it's more work to keep a manual
  nav structure up-to-date, I think it will be more useful as a
  consumer.
* Added an RSS feed for [changes](/feed_rss_updated.xml) and
  [creations](/feed_rss_created.xml) using the
  [mkdocs-rss-plugin]([Title](https://github.com/guts/mkdocs-rss-plugin)).