# Bearings

<!-- 
* TODO: Slip ring? Does this belong here, or elsewhere?
-->
Bearings are everywhere there is motion. Bearings are a machine element
that either support, or permits, a specific type of motion in a system
under load. It always (?) reduces the [degrees of
freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)).
There's likely hundreds of types of bearings, but I want to address a
few that are super common and useful to have around.

NOTE: **Source of Images** All the images here are taken from
[SKF](https://www.skf.com) who is one of the largest manufacturers of
bearings in the world. Their site has a wealth of useful information on
very specific use cases that you might find interesting.

## Force on Bearings

Before we talk about the bearings, though, we need to talk about loads.
All loads fall into two categories: static and dynamic. The difference
lies in the forces produced by the object. For a static load, the load
remains constant and doesn’t change over time. In a dynamic load, some
external factor causes the forces of the load to change.

Some of the factors that can affect a load and convert it to dynamic
include: 

* Movement. If the load is in motion, the force created by the weight
  distribution could (and will) change.
* Increased tension. When two loads are in conflict, it can cause the
  force to shift from one load to the other.
* Other outside force. Hundreds of other things can cause dynamic loads,
  including environmental such as water, air, or even ground movement
  (earthquakes).

Once we know whether a load is static or dynamic, we need to understand
how that load presents itself. It can be radial, axial (or thrust), or
centrifugal.

![Drawing of radial versus axial load](/img/radial-v-axial-load.jpg){: width=300 align=right }

Bearing radial loads are forces that are perpendicular to the axis of
the shaft and parallel to the bearing’s radius. In the drawing, the
shaft assembly pushes radially on the inner ring of the bearing
transferring a load through the rolling elements to the outer ring.

Radial loads don’t transfer force equally or uniformly onto the rolling
elements. The rolling element directly under the application load is
usually the one that’s receiving the most force. Then each successive
rolling element in each direction transfers less and less load to the
other.

Some examples of a radial load on a bearing are the weight of a
horizontal shaft assembly, gears, or pulleys.

An axial load is a force that acts parallel to the axis of the shaft.
This is also called a thrust load (see thrust bearing later). Usually,
you’ll find an axial load directly in line with the shaft, like you
would see on a drill. Sometimes, however, an axial load can be a dynamic
or reactive load offset from the shaft axis, like a bevel gear.

Unlike a radial load, an axial loads transfer force both equally and
uniformly onto the rolling elements thereby creating a balanced load.


## Plain Bearings (Bushings)

![A selection of various sized plain bushings](/img/bushing-plain.jpg){: width=300 align=right }

A plain earing, sometimes called a bushing in certain forms, is the
most fundamental and simple type of bearing. It consists of a bearing
surface, and there are no moving components. To ensure smooth movement,
materials with a low coefficient of friction are used. Commonly this is
some kind of [red
metal](https://blog.boydmetals.com/everything-you-need-to-know-about-red-metals)
(copper alloy), with bronze being one of the most common.  Sometimes the
metal is [oil
impregnated](https://www.onlinemetals.com/en/product-guide/alloy/SAE%20841),
which makes them self-lubricating (the physics is super cool).
Sometimes it's uses another material as a surface layer, such as
[Babbitt](https://en.wikipedia.org/wiki/Babbitt_(alloy)). This is what
you'll see in many automotive bearings.

The bearing is basically a sleeve mounted on the shaft and it fits into
the bore. Plain bearings are inexpensive, compact and lightweight. They
have high load-carrying capacity. The bearing remains fixed while the
other surface slides on the bearing’s inner surface. 

![A cutaway of a radial spherical plain
bearing](/img/bearing-radial-spherical-plain.jpg){: width=250 align=left }

If you take one bearing with a spherical exterior surface and place it
inside another bearing with a spherical interior surface, you have
created a radial spherical plain bearing. (Say that 5 times
fast!). They're mostly useful, in my experience, where you have a
sliding motion through the bearing while also sustaining either some
movement or oscillation. While they look like a ball bearing, they are
not because there is no rolling element. There's simply two low friction
surfaces sliding against one another.

## Ball

Ball bearings are, as the label on the tin implies, composed of
spheres that are rotating to reduce friction and constrain degrees of
freedom. They come in 3 main forms (besides sometimes loose that are
used in very customized ways): grooved, thrust, and linear.

### Grooved

![Cutaway of a deep groove ball bearing](/img/bearing-ball-groove.jpg){: width=400 align=right }

Probably the most common form of ball bearing is the grooved ball
bearing. In this configuration, the balls are "captured" in a groove
between two outer rings. Sometimes, there are two rows in very heavy
load situations, and often they are lubricated and have a seal to hold
the lubricant and balls in the right place.

Grooved ball bearings accommodate radial and axial loads in both
directions and are very low maintenance. 

One of the most common form of these in the maker community is are
bearing models 608 (22x7mm for 8mm shaft) and 625 (16x5mm for 5mm
shaft). Often you will see the suffix "-2RS" which means that the
bearing is sealed on both sides. There are, however [a very wide
variety](https://www.mcmaster.com/products/bearings/bearings-1~/stainless-steel-ball-bearings-8/).

Note that a industrial high quality bearing, like the SKF 625-2RS will
cost 10x as much as what you can get a cheap mediocre quality version
for on Amazon or AliExpress. Having said that, the cheap mediocre ones
are more than good enough for a vast majority of use cases, and because
the designs are almost universally standardized, you can upgrade to a
high quality one if you need it without a major redesign.

Personally, I keep a stock of inexpensive 608 and 625 series bearings
around for most purposes, and they're good enough to get started.


### Thrust

![Cutaway of a thrust ball bearing](/img/bearing-ball-thrust.jpg){: width=400 align=right }

If you take the balls and you arrange them between two plates (rather
than rings), you create a thrust ball bearing. A thrust bearing is, almost
exclusively, for a radial load. An axial load is likely to dislodge the
balls and break things. For example, if you need a [lazy
susan](https://en.wikipedia.org/wiki/Lazy_Susan) to rotate smoothly so
that your condiments are quickly available to anyone at the table, a
thrust bearing is what you're looking for.

It's important to notice that not all thrust bearings have a guide that
will keep everything in place as some are loose. Keep this in mind when
you're choosing a bearing.

Note that thrust bearings come in roller form as well.


### Linear

![Inner view of a linear ball bearing](/img/bearing-ball-linear.jpg){: width=400 align=left }

Linear bearings have a bunch of different names: linear motion bearings,
slide bearings, and at least bearing sliders. All of these refer to a
cylindrical holder that contains a large number of small ball bearings.
These are typically retained in a cage (otherwise they'd fall out), and
often are then placed inside of some mounting unit. 

Regardless of their exact form, linear ball bearings are very similar to
regular plain bearings (bushings) in that they are specifically designed
to control movement in one direction. You will see these a lot in things
like 3D printers.

## Roller Bearings

Roller bearings are very similar to ball bearings, except that the balls
are replaced with cylinders of some size and proportion. This allows
them to handle more load than a ball bearing while also exhibiting
higher precision under most circumstances.

### Cylindrical

![Cutaway of a cylindrical roller
bearing](/img/bearing-roller-cylindrical.jpg){: width=400 align=right }

Cylindrical roller bearings are very similar to ball bearings, except
rather than balls in raceways, you have cylinders  in there. Because of
the increased surface area, this kind of bearing can handle _very high_
radial loads at high speed.

For higher loads, you also will occasionally find multiple rows of
rollers in the same bearing. This can, of course, be replicated through
the use of multiple bearings.

Cylindrical roller bearings are (if not a plain bearing) what you would
typically see on a crankshaft of a high performance machine.

Cylindrical roller bearings can also be found in a thrust configuration.

### Needle

![Cutaway of a needle roller bearing](/img/bearing-roller-needle.jpg){: width=400 align=left }

Needle rollers are nearly identical to cylindrical rollers except for
the ratio of length and diameter of the rollers themselves. While
there's no official ratio, typical normal cylindrical roller bearings
will have a length to diameter ratio of less than 5:1, whereas needle
(hence the name) are greater than 5:1, creating a longer surface for
contact, while reducing the relative height of the bearing. 

Needle roller bearings can also be found in a thrust configuration, in
which case they're "needle roller thrust bearings". Lots of words, but
they are very explicit about their design. And like most other bearings,
they are available in sealed and unsealed variants. For hobby uses,
always choose a sealed one if you can, as it will bring less trouble
long-term. 

### Tapered

![Cutaway of a tapered roller
bearing](/img/bearing-roller-tapered.jpg){: width=400 align=right }

Tapered roller bearings feature two distinct pieces: a cup and cone
assembly. The cup is comprised of the outer ring which holds the cone
assembly. The cone assembly consists of inner ring, rollers, and cage.
This bearing construction accommodates combined (both axial and radial)
loads.

One of the neat behaviors of a tapered roller bearing is that, when you
have a two row tapered roller bearing assembly, you can adjust one
single row tapered roller bearing against a second tapered roller
bearing. When you apply an [appropriate
preload](https://insights.globalspec.com/article/12036/bearing-preload-what-is-it-and-why-is-it-important),
a rigid configuration can be achieved.

## 3rd Party Resources

* [Guide to bearings and bushings](https://www.bearings.saint-gobain.com/media-center/blog/guide-bearings-and-bushings)
* [SKF manufacturer](https://www.skf.com)
* [Bearing numbers explained](http://www.engineerstudent.co.uk/bearing_numbers_explained.html)