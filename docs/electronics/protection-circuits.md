# Protection Circuits

## Snubber Networks

A snubber is a device/circuit that is used to limit (snub) voltage transients in
circuits. Often there can be a sudden interruption of current flow, which drives
a significant rise in voltage across a device. This can lead to both EMI, but
also potential damage to the device due to [back
EMF](https://en.wikipedia.org/wiki/Counter-electromotive_force). There are three
major types of snubbers you can use. The simplest is a snubber diode. The more
complicated is an RC snubber, and while it's marginally more complicated, it is
also better behaved. Finally, you can build one out of solid-state
(semiconductor) components, typically using a pair of Zener diodes.


### Snubber Diode

> NOTE: **Alternate Naming** Snubbers can also be called _flyback_ protection, for
> example, a _flyback diode_. They can also just be called a _suppression diode_. 
>
> Flyback is a sudden voltage spike across an inductive load when its supply
> current is suddenly interrupted. It originated in its use in early CRT technology.

A snubber diode is the simplest possible solution and typically works well in DC
circuits. It leverages the diode as a
[rectifier](https://en.wikipedia.org/wiki/Rectifier). We wire the diode in
parallel with the load (say a relay), but set so that it doesn't conduct under
normal use. 

![Diode snubber with relay](/img/schematic-diode-snubber.png)

When current is interrupted, the magnetic field of the inductor (the coil in a
relay) collapses, causing back EMF. This can drive a big spike in voltage. With
the snubber diode, the inductor's current flows through the diode instead, and
the energy is slowly released via the diode's inherent voltage drop.

WARNING: **Possible Problems** One reason that snubber diodes aren't that
popular is that they are _slow_. Because of this, the inductor can stay active
longer than you want. For example, it can cause the turn-off time of a relay to
increase substantially.

You can watch [this great video](https://www.youtube.com/watch?v=c6I7Ycbv8B8)
discussing it in more detail

### RC Snubber

RC snubbers operate on a similar principle to diode snubbers and are more
"popular" in the industry as they work with both AC and DC systems. Since the
voltage across a capacitor cannot change instantly, any voltage spikes are
mitigated. An example, using the above basic schematic is:

![RC snubber with relay](/img/schematic-rc-snubber.png)

Unlike a diode snubber, there's some calculations you'll need to do to choose R
and C correctly. This is [quite
complicated](https://www.eetimes.com/calculating-an-r-c-snubber/), and so I
generally just use a diode snubber unless the timing is critical.