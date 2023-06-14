# Soldering

## Solder and Flux

Solder is a metal alloy used to create strong permanent bonds such as attaching
components to a PCB, or joining wires together. It comes in two different types,
lead and lead free, and also can be had in a wide variety of diameters
(typically 0.015" to 0.125"). Inside any solder intended for electronics is the
flux, a material used to clean, strengthen, and improve its mechanical
properties.

Flux does its job by removing impurities from the surface of the joint and
preventing them from interfering with the bond between it and the solder. Flux
comes in liquid, paste, or powder form, and can be used before and during the
soldering process.

There are three main types of flux in common use:

_Rosin_
: Made from pine tree sap which is dissolved in a solvent (usually
isopropyl alcohol). It is slightly acidic, which helps activate it.

_No-Clean Flux_
: This is a rosin-style flux with minimal activation (mostly acidity). This
means you don't _have_ to remove it after assembly. Unfortunately, it's also
less effective at preparing the board for soldering. Also, you should clean it
anyway, as it can leave a sticky residue.

_Water-Soluble Flux_
: This is based on a totally synthetic resin base. It is still quite corrosive
(even more so than rosin in some ways), which does lead to a well-prepared
surface, but it also means it must be cleaned as well. It _may_ generate less
harmful fumes due to its use of water as a solvent.

## Composition of Solder (Lead/Lead-Free)

There are two major categories of solder: lead and lead-free. Before we freak
out about the lead, the lead is _not_ vaporized, and is not part of the smoke
you see when soldering. 

### Lead-Based Solder

Lead based solder is the traditional formulation, and has a low melting point
(180C) and good flow and wetting properties. There are two primary formulations
in use:

* 60Sn/40Pb
* 63Sn/37Pb

The main difference between the two is in how they melt and solidify. 60/40
solder becomes plastic around 183C and fully melts at 188C. The range between
(183-188C) is considered the plastic region. Because it can spend more time in
this plastic region, it has a higher tendency of forming a cold solder joint.

> TIP: **What is a cold solder joint?** A cold solder joint is one where the
> joint has not been properly heated and did not melt completely. It can happen
> for a number of reasons: using too little heat, not applying heat evenly, or
> not applying heat for long enough. Cold solder joints are weaker than proper
> ones and can cause electrical problems.
>
> You can tell a solder joint is cold by looking at it under a magnifying glass.
> A cold solder joint will look dull or grainy, while a well-soldered one will
> be shiny and smooth. You can also try to move the component. If the joint is
> weak, the component will move slightly.

63/37 solder, on the other hand, is a
[eutectic](https://en.wikipedia.org/wiki/Eutectic_system). Unlike 60/40 solder,
63/37 melts and becomes solid at a singe temperature (183C), eliminating its plastic
region and reducing the possibility of cold solder joints. One minor bonus is
that 63/37 solder solidifies into a slightly shinier and smoother surface. It's
also slightly more expensive.

Which should you use? Either. Just buy a decent brand.

### Lead-Free Solder

NOTE: **TODO** Need to write about this, but right now I don't feel like I know
the topic well enough. 

## Wire v Paste

There are two main types of solder that you'll see as a hobbyist: solder wire
and solder paste. Solder wire is primarily used for wires, through-hole
components, and larger SMD devices (although you can do miracles with smaller
with some techniques). Solder paste's sole dominion is surface-mount technology.
If you're just starting out, start with wire.

## Buying Solder

So, now that you know a bit about what solder is, how do you go about buying it.
There's a few things you will need to think about. First, make the choice
between leaded and lead-free. My recommendation would be for leaded solder as it
is much easier to solder as a beginner. Second, choose a formulation (either is
fine). I'd also stick with rosin flux cores. Then you'll need to pick a solder manufacturer. These are the solder brands that I would stick to:

* Chip Quick
* Kester
* MG Chemicals

Lastly, you'll need to pick a solder diameter. My two preferences are for
something around 0.020" (0.51mm) and 0.062" (1.57mm). These give you options for
both fine work and more bulk work (like tinning large wires). Personally, the
main solder I use [Kester
44](https://www.kester.com/products/product/44-flux-cored-wire) in those two
sizes. I also happen to keep them both stored on a [Hakko 611 dual-spool
holder](https://hakkousa.com/611-dual-solder-spool-reel.html). It's inexpensive,
but it keeps things tidy.

## Storing Solder

Solder does/can expire, although solder wire will last much much longer than
paste, and in non-production uses, it's probably going to be fine _forever_.
Solder paste, however, needs to be stored in a controlled environment. [Adafruit
has more](https://learn.adafruit.com/smt-manufacturing/solder-paste-storage) on
this, but I store mine in a cheap little Peltier-cooled fridge that was super
cheap (it's also not super efficient, but it's tiny so it doesn't matter):

![Exterior of small fridge](/img/solder-fridge-exterior.jpg){width="400"} ![Interior of small
fridge](/img/solder-fridge-interior.jpg){width="400"}

## 3rd Party Resources

* [Soldering flux: acids, solids, and solvents]( https://www.protoexpress.com/blog/soldering-flux-acids-solids-and-solvents/)
* [60/40 vs 63/37 solder - what are their similarities and differences](https://www.raypcb.com/60_40-vs-63_37-solder/)
* [What is a cold solder joint?](https://electronicshacks.com/what-is-a-cold-solder-joint/)