---
tags:
  - python
  - software
  - libraries
  - barcodes
---
# Python Libraries

Look, there's a [staggeringly gigantic collection of Python
libraries](https://pypi.org) out there. This isn't that. This isn't even
1% of that. This isn't even 0.01% of that. What this is is just a list
of libraries that I _personally_ use regularly and find to be good.
Hopefully that might be a lead for people looking for something to
scratch an itch.

## HTTP

[HTTPX](https://www.python-httpx.org/)
: An alternative to the ever-popular
[requests](https://docs.python-requests.org/en/latest/index.html). I
switched a while back because it had better type annotations, but I feel
like there was another reason I switched, but I can't for the life of me
remember what it is.

## Barcodes and Labels

[Blabel](https://github.com/Edinburgh-Genome-Foundry/blabel/tree/master)
: This library from the Edinburgh Genome Foundry provides a simple
interface to use HTML+CSS+Python to define labels, including lots of
barcode symbology. While things like the Brother P-Touch editor are
great for small sets of labels, this is the thing you want if you need
to generate labels in the hundreds or programmatically.