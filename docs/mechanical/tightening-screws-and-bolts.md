# Tightening Screws and Bolts

I know what you're thinking... you're thinking "you twist the
screwdriver until it stops twisting", and that's probably not the worst
thing, but there is, weirdly enough, some details that can improve your
screw (or bolt) tightening game. To start, we can look at the forces in
a bolted joint:

![Diagram of forces in a bolted joint](/img/load-forces-diagram.png)

We have a couple of forces at play here:

* _Clamping force_.  This is the force being exerted by the bolt to hold
  the two plates together. It should, ideally, be enough to incur a high
  enough friction force to prevent the plates from shearing.
* _Shearing load_. This is the force that occurs when you have two
  bodies acting in opposing directions against one another.
* _Tensile load_. This is the force we are putting on the bolt (in this
  case), which causes the bolt to elongate and exert the _clamping
  force_. 

## Order of Tightening

First, the order of tightening matters. Why? Because the goal is to
distribute both the load and stresses as evenly and consistently across
the joint as possible with the screws or bolts provided.  They break
down into basically two patterns. One for circular arrangements and
another for rectangular arrangements.

For circular arrangements, you want to follow what, to me, looks like a
pentagram pattern. I think the official designation is "criss-cross",
but I like seeing it as dark arcana. I've drawn out the ordering in the
diagram below for a 6-bolt flange joint, but a similar pattern can be
used with any other number of bolts or screws.

![Diagram of tightening pattern for circular
arrangement](/img/bolt-tightening-pattern-circular.png)

The goal is to make sure you basically go to the furthest bolt from the
one you just tightened, alternating "sides" as much as possible.

For a rectangular joint, you use a slightly different approach. Instead
of all the diagonals, you want to use a "spiral" from the inside out on
the joint. In the diagram below, I show how that would look for an 8
bolt joint. Again, this generalizes.

![Diagram of tightening pattern for rectangular
arrangement](/img/bolt-tightening-pattern-square.png)

For hobbyist uses, just do your best to follow something like this. It
will result in sturdier, more durable, and less likely to loosen joints.


## Multiple Passes

Typically, if you're trying to get the most even loading on a joint, you
don't want to do all the tightening in a single pass. While there are a
lot of recommendations you can look into if you're interested (see
below) that depend on using a torque wrench, you can take the following
as a good rule-of-thumb:

1. First pass to what people will call "finger tight". This means to
   tighten something using only _two fingers_. This is when the free
   play in a joint is effectively gone. In absolute, this would be
   20-30% of your target torque, but without a torque
   wrench/screwdriver, you can just estimate.
2. The second pass, in the same pattern, to 50% of full torque load.
3. A third pass to bring it to the final torque load.

Truthfully, I typically only do it in two passes typically, unless it's
something like a metal-on-metal joint with bolts where I know the actual
torque requirements. For hobbyist use, just 2 passes is typically
enough.

When doing serious industrial tightening, you would add a 4th pass to
this, in a different pattern, to ensure everything is tightened down
correctly. Because of how joints load, as you tighten another bolt or
screw, you can end up shifting the loads in previously tightened ones.

## Holding Joints with Loctite

Sometimes (often) you want to ensure that the bolt or screw doesn't come
out due to vibration or stresses. There's a few different ways to do
this, but here I want to discuss the two easiest and most common in the
hobby world: [Loctite Threadlocker Blue
242](https://www.loctiteproducts.com/en/products/specialty-products/specialty/loctite_threadlockerblue242.html)
and [Loctite Threadlocker Red
271](https://www.loctiteproducts.com/en/products/specialty-products/specialty/loctite_threadlockerred271.html).
While there are other products, these two will get you _very far_ in
making things not come apart until you want them to.

The two materials behave very similarly, but have two distinct use
cases:

* _Loctite Blue 242_. For a vast majority of uses cases, this is the one
  you want. It's designed for situations where you want to be able to
  take something apart for service, but you want to reduce the
  likelihood of it loosening on its own.
* _Locktite Red 271_. This is for a much more permanent joint, and
  really can't be removed without using a blowtorch and heating
  something to 260C (500F). Obviously, you can't do that with plastic
  parts, so it is, for all intents, permanent. 

The use of each of them is basically a couple of steps:

1. Clean both sides of the joint/part. I find IPA works really well for
   this in most cases.
2. Shake the little bottle for 20-30s. It's a suspension, so you want to
   make sure it's dispersed evenly.
3. Apply a very small amount to the threaded side of the joint, for
   example, the screw. The surface tension should be enough to hold it
   in place. If it drips, you've added too much. It'll work, but it's
   not a cheap product, so it pays to be a bit more frugal.
4. Screw/bolt it together.
5. Let it cure for 24h.

Like other things in this group of acrylates (think superglue), it has a
short "set time" (10m), but a much longer cure time to reach its full
potential.

NOTE: **Alternatives to Loctite** I have seen people use cyanoacrylate
(superglue) to do the same thing, and while it will "work", it is
definitely a less desirable from a mechanical properties perspective.
Cyanoacrylate has very low shearing strength. This is _specifically_ the
strength you need to hold screws and bolts in place. While the screw or
bolt may be undergoing torsional stress, the material is under sheering
stress. So, while it will be stronger than one without it, it won't be
in the same category as Loctite here. 

## Common Torque Limits

WARNING: **Check with Manufacturer** The table below is just some rough
rules-of-thumb, nd you should definitely check with specific
manufacturers for their recommended torque settings.

| *Use Case*                               | *Torque Target*     |
| ---------------------------------------- | ------------------- |
| Attaching a PCB to a mount point.        | 0.6Nm (0.44 ft-lbs) |
| Putting case pieces together with screws | 1.0Nm (0.74 ft-lbs) |

## 3rd Party Material

* [ASME B16.5 - Pipe Flanges and Flanged Fittings: NPS 1/2 through NPS
24, Metric/Inch Standard
](https://www.asme.org/codes-standards/find-codes-standards/b16-5-pipe-flanges-flanged-fittings-nps-1-2-nps-24-metric-inch-standard#:~:text=ASME%20has%20been%20defining%20piping,pipe%20flanges%20and%20flanged%20fittings.)
* [ASME B16.47 - Large Diameter Steel Flanges: NPS 26 through NPS 60,
  Metric/Inch
  Standard](https://www.asme.org/codes-standards/find-codes-standards/b16-47-large-diameter-steel-flanges-nps-26-nps-60-metric-inch-standard).
* [Fastenal torque-tensioning reference](https://www.fastenal.com/content/merch_rules/images/fcom/content-library/Torque-Tension%20Reference%20Guide.pdf)