# Filters



## Pi Filters

A Pi filter is a type of filter constructed with 3 elements rather than the
traditional two-element passive filter. Since the constructed arrangement of all
the components creates something that looks like the Greek letter Pi ($\pi$),
the name Pi filter is used. Pi filters are pretty easy to calculate and design,
and if needed, you can often buy off-the-shelf pre-configured ones for very
cheap.

Pi filters have a few advantages over simpler LC filters:

1. Can handle very high voltage across the filter, which makes it suitable for
   high voltage DC applications.
2. Low ripple. When used in a DC filtration purpose, it's very effective and
   leaves very little ripple behind in the output.
3. Easy to use for high-frequency applications.

Their disadvantages are mostly around cost:

1. High wattage inductors are required in power situations. High wattage
   inductors are pricey.
2. High value input capacitor. This can create space constraints and also
   increase cost.
3. Poor voltage regulation in situations where the load is fluctuating constantly

### Low-Pass

A low-pass filter only allows frequencies _below_ its design point to pass. The
design of a low-pass Pi filter is pretty simple. The circuit consists of two
capacitors connected in parallel with an inductor in series which forms the Pi
shape as shown below:

![Low pass Pi filter](/img/schematic-pi-filter-low-pass.png)

We can find the -3dB point of a low-pass filter using this equation:

$$f_c = {1\over{2\pi\sqrt{LC}}}$$

### High Pass

Reversed from a low-pass filter, a high-pass filter only allows frequencies
_above_ its design point to pass. A high-pass filter has just a flipped design
with the the inductors in parallel and the capacitor in series:

![High pass Pi filter](/img/schematic-pi-filter-high-pass.png)

It's -3dB point can be calculated exactly the same.

$$f_c = {1\over{2\pi\sqrt{LC}}}$$

