# Labeling

## Process

Step 1: Purchase a label maker.

Step 2: Use it consistently.

## Label Makers

Personally, I prefer Brother's P-Touch label makers. There are better (companies like
Brady, etc.), but they're affordable, and in my experience the actual laminated
label is _very durable_, which is what I'm looking for. If you buy knock-off TZe
labels (see random Amazon searches, etc) they're quite affordable, and also seem
to be close enough in quality. Sadly, the OEM labels are very pricey.
Fortunately, unlikely certain other companies (see: HP and Epson), they don't
try and DRM their way to profit.

I've had 2 Brother P-Touch label makers. For many years, I used a [PT-1290](https://www.brother-usa.com/products/pt1290) which
was a little handheld model (shown below). I'm pretty sure I had it for 10+
years without a single problem.

![A well-used Brother PT-1290 label maker](/img/brother-pt-1290.jpg){width=500px}

Recently, I replaced it with a
[PT-750W](https://www.brother-usa.com/products/PTP750W) for a couple reasons:

1. It plugs into my computer, and lets me print a series of labels easily.
2. It plugs into power, and therefore doesn't burn through AA batteries quickly.
3. It supports a much wider variety of labels. The old one couldn't handle
   anything except 9 and 12mm label stock.
4. It's higher resolution and faster.
5. I can print to it from my phone if I need to.
6. It prints all kinds of bar codes correctly.

If I have any complaint, it's that opening the side door to change the print
cartridge, while easy, does require picking it up as it lifts the bottom. Still,
overall, I'm very happy with it.

## Label Layout

This is the layout I use for inventory labels:

![Inventory label for ESP32-WROOM-32U](/img/sample-inventory-label.png)

This is composed of a few things:

* A quick description of the thing being labeled: "ESP32-WROOM-32U"
* A part number: `001.0844.00`
* A [data matrix](https://en.wikipedia.org/wiki/Data_Matrix) barcode that can be
  easily scanned.

On the label, you can see a two little colored boxes with the number one (1) in
them. These are linked fields that mean that the data matrix 2D barcode is
always up-to-date.

The main reason for a data matrix, rather than a [QR
code](https://en.wikipedia.org/wiki/QR_code), is that it consumes much less real
estate on the label and has a much higher information density. For example, the
two barcodes below store the exact same information (the part number above).

![QR code](/img/sample-qr-code.png) ![Data matrix](/img/sample-data-matrix.png)

## Barcode Scanner

<!-- TODO: Add picture of scanner. -->
I am in the process of developing a better workflow for dealing with bar codes.
Obviously, if you just print them, they serve no purpose. I'm working to try and
integrate them into my [inventory](inventory.md) system so that things are more
easily tracked.

The barcode scanner I am using is the [Tera
HW0006](https://tera-digital.com/products/2d-barcode-scanner-hw0006). Not all
scanners can handle 2D codes, or even anything but a QR code. Make sure you keep
that in mind. This one comes with a Li-Ion battery, charging cradle, and 2.4GHz
wireless dongle (Bluetooth as well). Recognition of a data matrix seems to be
well under 1/2 second.