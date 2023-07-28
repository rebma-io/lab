# Bosch/Sortimo

![A stackup of many Bosch L-Boxx components on a rolling
platform](img/bosch-stackup.jpg){: width=240 align=right }

Years ago, I saw [Adam Savage talk about his love for Sortimo storage](https://www.youtube.com/watch?v=1OPSbF6kM9k
), but when I did some investigating, I found it was prohibitively
expensive for my uses. It 100% makes sense for it's target professional
audience, and for someone like Adam that works in his shop constantly,
but for me, it was simply too expensive. Then, I discovered that Bosch
made a compatible system. In fact, the system is produced by Sortimo for
Bosch. It isn't _quite the same_, but it's darned close, and it's a good
bit cheaper, if a lot more limited. It is, however, 100% compatible, so
you can mix and match.

## Unique Characteristics

There are a bunch of other systems out there, for example, Milwaukee's
"Pack Out" system, but there's a few things that I think set the
Sortimo/Bosch system apart as slightly better:

* They latch together _very quickly_, and in a very secure and study
  fashion. I was able to cary the entire set you see in the photograph,
  minus the rolling base, up a set of stairs by the handle without any
  issue.
* In my quick cross-referencing, they seem to be slightly lighter for
  the same storage space. They certainly are not flimsy, but they seem
  to have very optimized use of plastics to ensure strength without
  adding weight. A few ounces adds up.
* The design of the latching allows you to open boxes in the middle
  without removing boxes on top of it. This is super helpful.
* It has a great roll-around platform with large ball-bearing wheels
  that it latches and unlatches to quickly.

## Differences with Sortimo

I've never touched a Sortimo system hands-on, but from watching videos
and looking at data sheets, there's a few things, besides the obvious
color differences, that set the two apart:

1. The i-Boxx systems have no system to lock storage in place, so you
   really need to make sure it's "full" to hold everything in places so
   it doesn't get mixed up. This may also just be something unique to
   the
   [T-Boxx](https://www.mysortimo.us/en_US/Storage-Bins-%26-Boxes/T-BOXX-G/c/47220)
   line from Sortimo.
2. There's slightly more wasted space in the i-Boxx, with both ribs and
   just more material along the outside. I think you lose a centimeter
   or two in this in all dimensions.

## Alternatives to Sortimo

The other big system out there, at least at the high-end, is
Tanos/Systainer.
[Festools](https://www.festoolusa.com/products/systainer,-sortainer-and-systainer-port/systainer)
is the big retailer of these in the US. They are priced similarly to
Sortimo, and as best as I can determine, are every bit as good.

## Dimensions

These are a combination of Bosch's measurements (for the outside), and
my measurements for the inside. For situations, like with the L-Boxx,
where there are "ribs" that intrude into the box, I have measured
_excluding_ the ribs. These will typically gain you another 1/4" on each
dimension.

| Model     | Outside Dimensions (WxDxH) | Inside Dimensions (WxDxH) |
| --------- | -------------------------- | ------------------------- |
| L-Rack    | 17.5x13.5x12"              | N/A                       |
| L-Rack-S  | 17.5x13.5x4"               | N/A                       |
| L-Boxx-3D | 17.5x14x12"                | N/A                       |
| L-Boxx-1  | 17.5x14x4.5"               | 16.25/14.5x12x3.25"       |
| L-Boxx-3  | 17.5x14x10"                | TBD                          |
| i-Boxx53  | 14.25x12.5x2.25"           | 13.25x10.375x1.75"        |
| i-Boxx72  | 14.25x12.5x3"              | 13.25x10.375x2.5"         |
| LST92-OD  | 14.5x12.5x3.625"           | 13.75x10.375x2.75"        |

NOTE: **Apology** Yes, I know these are customary/imperial
measurements. So shoot me. I flip back and forth constantly. Weirdly, I
modeled in metric, but measured in customary, largely because I only
have a tape measure that reads in inches.

## i-Boxx Inserts

A big open space isn't the most useful thing for organizing parts. While
Bosch does [offer some
compartments](https://www.boschtools.com/us/en/boschtools-ocs/tool-and-accessory-storage-org53-12-46580-p/),
and while being injection molded means they're stronger and lighter, I
wanted something with more flexible sizing, especially since I actually
needed smaller containers to achieve higher density. 

I built a 12x8 grid parametric design, and then created every
combination under 4x4 on the grid. The basic X/Y grid is 28x32.375mm.

FUTURE: **Random Strings of Numbers** I realize the 32.375mm is a _very_
weird measurement. In the future, I might use `floor()` in the
parameters to get to something more "even". The problem with doing this,
though, is that 32mm creates an extra gap of almost 5mm at the end. SO
MUCH WASTAGE!

### Models

All of the models (STL and Fusion 360 `f3d` file) are [available on
Printables](https://www.printables.com/model/538356-boschsortimo-i-boxx72-sorting-containers),
at least for the i-Boxx72 size. The difference between 2x3 and 3x2 is
the orientation and how the label is placed on it. I've also included
the Fusion 360 original.

### Labels

What is organization with [labeling](labeling.md)? I have put together
some templates, but first, some dimensions that will help, I hope, for
Brother P-Touch TZe cartridge sizes:

| Location                | Label Width | Length |
| ----------------------- | ----------- | ------ |
| Label for 1xN           | 9mm         | 25mm   |
| Label for 2xN and anove | 9mm         | 52mm   |
| Label for i-Boxx        | 12mm        | 130mm  |

You can find a collection of templates for the P-Touch Editor in [this
Github repository](https://github.com/rebma-io/brother-label-templates). 

## Third-Party Resources

* [Acme Tools](https://acmetools.com/). This is where I bought mine
  from.
* [Review of the L-Boxx system](https://toolsinaction.com/bosch-l-boxx-review/).
* [Sortimo US](https://www.mysortimo.us/en_US/).