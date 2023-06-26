# LEDs and Lasers

CONSTRUCTION: **Work in Progress** I've just started this part of the
site, and there is, as you can well imagine, a lot to talk about with
LEDs.

LEDs, or [light emitting
diodes](https://en.wikipedia.org/wiki/Light-emitting_diode), are exactly
like every other semiconductor diode in the world, except, instead of
just getting hot and emitting a sporadic photon here and there, they are
doped to release many more photos. [The
physics](https://en.wikipedia.org/wiki/Light-emitting_diode_physics) of
how diodes works is a fascinating topic, but not one for this place.

## Indicator LEDs

TODO: Explain the name.

## Chip on Board (COB)

TODO: Side emitting LED.

## Other LED Packaging

TODO: LED "filament"

TODO: LED strips

## Driving LEDs Correctly

Driving LEDs safety is an important job, but not super complicated.
There are three possibilities, one easy, and two just a little more
difficult. Just using a series resistor will work, but a little more
effort and you can use a constant current source, or you can also use an
IC dedicated to driving LEDs.

### Series Resistor

One resistor per LED, not just one for a group. TODO: Schematic
comparison

Some diodes do have built-in series resistors, but if they don't
explicitly say they do, they very much don't.

Calculating using [Ohm's law](fundamentals.md#ohms-law)

$$R = {{V_{in} - V_f}\over{I_f}}$$

where:

* $V_{in}$ is the input voltage. This is the value of your power supply,
  battery, etc.
* $V_f$ is the forward voltage drop. This should be available from the
  manufacturer's data sheet. If it isn't, there are tools to measure it,
  or you can just wing it with something like 1.7V for a red LED and 3V
  on any other color. There's [more details based on color and
  materials](https://en.wikipedia.org/wiki/Light-emitting_diode_physics#Materials)
  available.
* $I_f$ is the desired forward current. Remember, LEDs care about
  current most of all. Too much current releases the magic smoke.

So, if we want to drive [this blue Cree
LED](https://www.digikey.com/en/products/detail/creeled-inc/C5SMF-BJE-CR0U0451/4793773)
properly, we can check the [data
sheet](https://assets.cree-led.com/a/ds/h/HB-C5SMF-RJF-RJE-GJF-GJE-BJF-BJE.pdf)
(see [how to read a data sheet](data-sheets.md)) and on the 2nd page we
will find an $I_f$ of 35mW (typical) to 100 (max), and a $V_f$ of 3.4V
(typical). If we want to power this with a 5V supply, We can stick those
into our equation:

$$\begin{aligned}
R &= {{5 - 3.4}\over{0.035}}\\[10pt]
&= {1.6 \over 0.035}\\[10pt]
&= 45.71428571
\end{aligned}
$$

Great, now we just need to find a 45.71428571 ohm resistor. Wait, there
isn't one, and while we could certainly construct a resistor arrangement
that would achieve it, we also need to take into consideration that most
hobby grade resistors are 1% tolerance at best. Since a higher resistor
value will result in a lower current, and therefore more safety, we
should choose a 47 ohm resistor (more about the E-series idea later). 

If we plug that back into our equation, we'll get 0.0340426 watts, or
34.04mW. Close enough. With tolerance taken into account, that's
33.7-34.3mW of current. Perfect.


### Constant Current Source

TODO: depletion mode MOSFET

TODO: constant current source (see current mirrors)

TODO: diagram of 3x current mirroring.

### LED Driver IC

TODO: Some example circuits.

## Laser Diodes

WARNING: **Laser Safety** Lasers are not like other light sources, both
because they are often invisible, but also because of the strength and
coherence of it. These characteristics lead to a lot of possible risks,
even with very low power laser configurations. Please read and follow
all safety recommendations, and I strongly recommend reviewing [detailed
safety
instructions](https://ehs.stanford.edu/manual/laser-safety-manual),
including signage, and wearing [trustworthy eye
protection](https://lasersafety.com/eyewear/laser-glasses/) at all times
when a laser _may_ be operating. Yes, real laser safety glasses are
expensive, but then so are new eyes.

Laser diodes are mostly like regular diodes, except in order to exhibit
the textbook definition of a laser
([coherent](https://en.wikipedia.org/wiki/Coherence_(physics)),
[collimated](https://en.wikipedia.org/wiki/Collimated_beam), and on a
single wavelength), they require some slight changes in their
construction, and integrate collimating optics instead of diffusion.
[This video](https://www.youtube.com/watch?v=tOai-C1fxIM) provides a
good introduction to them.

If we look at the breakdown of what's inside of a typical TO-5 can laser
diode, we can understand better what's going on.

![Breakdown diagram of a laser diode](/img/laser-diode-diagram.png)

The pieces that make up the photo diode are, from top to bottom:

* Protective can. Keeps dust and also outside air out of the can.
  Typically, the can is actually held at a medium vacuum.
* Window. The window allows the light to leave the can while maintaining
  the seal.
* Laser diode. The main part of the show.
* Heat sink. Removes heat from the laser diode itself and transfers it
  to the metal protective can.
* Monitoring photodiode. Used to monitor the output of the laser diode
  and adjust the current to it. Like all LEDish diodes, they need
  constant current to behave their best.

For these configurations, you'll have 3 pins so that you can access to
laser and photodiode separately and use the photodiode to help provide
feedback and drive the laser diode at a constant power. Because of the
complexity in driving a laser diode, I'd strongly recommend using laser
diode _modules_, which integrate the driver circuit into them directly.
[Adafruit](https://www.adafruit.com/search?q=laser+diode) carries a few
of them.

Laser diodes are available in a bunch of colors, but some typical ones
and their uses are:

| Wavelength (nm)  | Color    | Usage                                                                             |
| ---------------- | -------- | --------------------------------------------------------------------------------- |
| 1625, 1550, 1310 | Infrared | Fiber-optic data communications                                                   |
| 650              | Red      | Inexpensive laser pointers and CD/DVD drives (some)                               |
| 635              | Red      | Better laser pointers as the frequency appears much brighter to the human eye     |
| 500-535 (varies) | Green    | The most common real green laser for pointers, but also used in laser projectors. |
| 405              | Violet   | Blu-Ray players                                                                   |

For typical hobbyist uses, laser diodes range in power from 1mW to
around 500mW. You will find more powerful laser diodes in things like
hobbyist laser cutter/engraver where they can reach from 5-20W
typically. Note that most (all?) laser diodes above 5W are actually
composed of multiple 5W laser diodes focused together to the same spot.

Also, like all LEDs, once you get about a few mW of power, you will need
to begin thinking about heat dissipation and (potentially) active
cooling. Laser diodes are, perhaps, 10-50% efficient (10% is probably
accurate for most cheap models), which means that 500mW laser diode
needs to dissipate several watts of energy as heat. Oh, and they
generally want to operate in the 25-50C (77-122F), which requires
substantial considerations if you intend to operate them at full power
continuously (called CW, or continuous wave).  Obviously operating them
pulsed averages things out and reduces the amount of heat that needs to
be dissipated. 

## 3rd Party Material

* [An introduction to laser
  diodes](https://www.allaboutcircuits.com/technical-articles/an-introduction-to-laser-diodes/)