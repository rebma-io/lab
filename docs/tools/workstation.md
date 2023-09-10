---
tags:
  - computer
  - lab
  - workstation
---
# Workstation

NOTE: **Personal Preference** This is 100% personal preference, and lots
of people will choose to work in a different environment. I just thought
I'd share what I find useful.

## Main Workstation

WARNING: **Beware Minisforum** I had previously been using a minisforum
HX90G, which is an AMD mini PC with a dedicated laptop GPU (not far off
from what I have now). Unfortunately, after a few months, it died, and
[as I documented on my
blog](https://blog.amber.org/blog/2022/09/minisforum-hx90-quick-review-updated-big-warning/),
I had a horrific experience of trying to get it repaired, which soured
me on their hardware permanently. I'm still fighting over refunds and
have had to involve my credit card company.

![A small 4L chassis Lenovo ThinkStation P360
Ultra](img/lenovo-p360-ultra.jpg){: width=200 align=right }

My main workstation is a Lenovo P360 Ultra that I got off eBay, but
which was, as far as I can tell, never used. It still had the little
peal-off protective stickers on the logo and other parts of the chassis.
It was a good deal for the price 
([[ usd(1500.00, as_of="20 August 2023") ]]). As it's currently setup,
it has the following configuration:

* Intel [i9
  12900K](https://www.intel.com/content/www/us/en/products/sku/134599/intel-core-i912900k-processor-30m-cache-up-to-5-20-ghz/specifications.html).
  16 cores, 24 threads, 30MB cache, 5.2GHz peak speed.
* nVidia
  [A5000](https://www.nvidia.com/en-us/design-visualization/rtx-professional-laptops/)
  GPU. 6,144 [CUDA](https://en.wikipedia.org/wiki/CUDA) cores, 16GB
  GDDR6 memory. This is a wildly overkill GPU for what I do, but given
  the deal I got, I can't complain. It's approximately equal to a 3080
  consumer GPU.
* 128GB RAM (DDR5-4800)
* 2 x 2TB Samsung 980 Pro SSD

This is a (largely) Windows 11 Pro machine, although I lean quite
heavily on [WSL2](https://learn.microsoft.com/en-us/windows/wsl/).
There's still a lot of things in the embedded world that run better on
Windows than they do Mac, so it felt like a good use. 

![A 3Dconnexion Space Mouse with a El Gato Stream Deck behind
it](img/space-mouse-stream-deck-combo.jpg){: align=left width=200}

On that machine, which I use for most of my 3D work, I also have an [El
Gato Stream Deck](https://www.elgato.com/us/en/p/stream-deck-mk2-black)
and a [3Dconnexion Space Mouse
Compact](https://3dconnexion.com/uk/product/spacemouse-compact/), which
I [discuss
elsewhere](../3d/modeling-tools.md#accessories-to-make-your-life-better).
They're hardly required, but they are a huge quality-of-life
improvement. I have them mounted together in a [3D design by
wit4r7](https://www.printables.com/model/42505-spacemouse-streamdeck-mount),
which reminds me of the old button boxes that IBM made for their CAD
workstations. It's printed in a slightly too pink pink (Sakura Pink from
Overture).

Finally, I have a pair of [Audio Engines A2+
speakers](https://audioengine.com/shop/wirelessspeakers/a2-wireless-computer-speakers/)
hooked up to the system. This is my main source of music when I'm in my
workshop, if I'm not using a local [HomePod
Mini](https://www.apple.com/homepod-mini/). 



## Macbook Air M1

My other main personal machine is a Macbook Air with the original M1
chip. It has 16GB RAM and 1TB of SSD in it, and it's just an absolute
joy to use. It's not quite as fast as my main workstation, but it is
smooth, absolutely silent, cool to the touch, and weighs so little. The
only downside is that with 3D modeling, I just can't get the hang of
using the trackpad. I've contemplated picking up a Bluetooth Spacemouse,
but they're even more expensive. 

Since I mostly use the laptop on the couch and such, I figure I can just
go upstairs to my workstation when I need to do modeling. 

This shares a [Belkin Thunderbolt 3 Pro
dock](https://www.belkin.com/thunderbolt-3-dock-pro/P-F4U097.html),
which is ... meh? It's fine, I suppose. But it seems to have random
occasions where it just can't deal with a monitor, and I have to power
cycle the dock and get it back to some sane state. Sometimes this
happens 3x a day, and sometimes it's weeks between occurrences. 

## Shared Peripherals

![Dasher MT3 keycaps on a Varmillo keyboard](img/dasher-keycaps.jpg){: align=right width=300 }

As you can imagine, and like many other people in the tech industry, I
have _strong opinions_ about input devices. Personally, I use a a
[Varmillo MAv2
keyboard](https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=8381)
with [Cherry MX Clear](https://switchandclick.com/cherry-mx-guide/)
switches. Sadly, Varmillo doesn't offer the Cherry switches any more.
The MX Clears have been my go-to because they offer great tactile
feedback, but without the noise that comes with many. I would love to
use my
[Unicomp](https://www.pckeyboard.com/mm5/merchant.mvc?Screen=PROD&Product_Code=SPACESAVER_M)
keyboard with it's glorious buckling-springs, but it's simply far too
loud if I have to do calls with people, and I share these peripherals
with my work laptop.

The keyboard is augmented with a set of [Dasher MT3
keycaps](https://drop.com/buy/drop-mt3-dasher-keycap-set), because you
can _never_ have enough glorious '70s Data General colors. Seriously, we
lost something when we abandoned the land of color for whatever we have
now, and I don't mean gaudy RGB lighting of everything. I don't want my
computer to be like a Las Vegas casino.

For navigation, I'm a big trackball fan. I don't think I've really used
anything else when sitting at a desk for decades. My go-to trackball is
the [Kensington Export
Mouse](https://www.kensington.com/p/products/electronic-control-solutions/trackball-products/expert-mouse-wired-trackball/)
with a big honk'n 55mm ball in it. It's just glorious. If I have any
complaint, it's that the scroll wheel around the ball is a bit crunchy,
and in spite of my best efforts, I've never figured out _why_. 

To put photons in my eyeballs, I have a pair of [Dell U2723QE 27" 4k
monitors](https://www.dell.com/en-us/shop/dell-ultrasharp-27-4k-usb-c-hub-monitor-u2723qe/apd/210-bdpf/monitors-monitor-accessories),
in spite of the best efforts by [certain
people](https://macaw.social/@april) trying to convince me to pop for an
Apple Studio Display. It might be marginally better quality, but it
costs more than both the Dell displays, and that's 14,745,600 versus
16,588,800 pixels for the twins, and as you'll see below, I use the twin
monitors to my advantage for more than extra real-estate. Those are
mounted on a gigantic Ergotron LX stand, which is almost 40# all by
itself.  I've had it for 13+ years though, and it's still bulletproof. 

Finally, all of this is hooked up with a 2x2 4K KVM from TESmart
([HKS0402A1U-USBK](https://www.tesmart.com/collections/dual-monitor/products/hks0402a1u-2-port-dual-monitor-kvm-switch-kit-hdmi-4k60hz-with-edid?_pos=1&_fid=ed6efc85d&_ss=c)).
This works great because it allows me to either have both monitors on a
single machine, or to split the two monitors between two machines and
use the right hand "Windows" key to pop back and forth. It has a small
remote control, but honestly, I just press the button the front when I
have it set with both monitors attached to a single machine (the usual
configuration).

WARNING: **Separation of Work and Personal** As tempting as it is, I'm a
big believer in keeping a _very strict_ separation between my work and
personal devices. I don't even open email on my work laptop, much less
anything else. Using a KVM lets me still check email and such during the
day without interfering. 