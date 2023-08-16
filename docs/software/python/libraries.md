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

[pylibdmtx](https://github.com/NaturalHistoryMuseum/pylibdmtx/)
: From the Natural History Museum in the UK, this library lets you both
create a parse [Data Matrix](../barcode-formats.md#data-matrix)
barcodes. You can see a use in [this
project](/projects/Signed-GS1-data-matrix/). There's another library,
[pystritch](https://pypi.org/project/pyStrich/), which is used by
`blabel` below, but it seems to be somewhat abandoned. It works, but... 

[python-barcode](https://github.com/WhyNotHugo/python-barcode)
: Great library that does nearly all the 1D barcode formats:  Code 39,
Code 128, EAN-13, EAN-8, JAN, ISBN-13, ISBN-10, ISSN, UPC-A, EAN14, and 
GS1-128.

[qrcode](https://github.com/lincolnloop/python-qrcode)
: Library for creating [QR codes](../barcode-formats.md#qr-code).

[Blabel](https://github.com/Edinburgh-Genome-Foundry/blabel/tree/master)
: This library from the Edinburgh Genome Foundry provides a simple
interface to use HTML+CSS+Python to define labels, including lots of
barcode symbology. While things like the Brother P-Touch editor are
great for small sets of labels, this is the thing you want if you need
to generate labels in the hundreds or programmatically.