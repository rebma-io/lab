# Units of Measure

There are a lot of units of measure that you end up working with. In
this section, I want to talk about a few that have always tripped me up,
and hopefully, by explaining them to others, I can better understand
them myself.

## International System of Units (SI)

Yes, the acronym doesn't play out. Blame the French. But, while this
information is all over the Internet, I'm just going to include it here
for reference from other places as needed.

### SI Units

| Quantity                                | Unit                                                  | Symbol |
| --------------------------------------- | ----------------------------------------------------- | ------ |
| Length                                  | [meter](https://en.wikipedia.org/wiki/Metre)          | m      |
| Mass                                    | [gram](https://en.wikipedia.org/wiki/Gram)            | g      |
| Temperature                             | [Celsius](https://en.wikipedia.org/wiki/Celsius)      | C      |
| Time                                    | [second](https://en.wikipedia.org/wiki/Second)        | s      |
| Force                                   | [Newton](https://en.wikipedia.org/wiki/Newton_(unit)) | N      |
| Electric potential difference (voltage) | [Volt](fundamentals.md#voltage-pressure)              | V      |
| Electrical current                      | [Ampere](fundamentals.md#current-volume)              | A      |
| Power                                   | [Watt](fundamentals.md#power)                         | W      |
| Energy, work, or heat                   | [Joule](https://en.wikipedia.org/wiki/Joule)          | J      |
| Electrical charge                       | [Coulomb](https://en.wikipedia.org/wiki/Coulomb)      | C      |
| Resistance                              | [Ohm](fundamentals.md#resistance)                     | &ohm;  |
| Capacitance                             | [Farad](fundamentals.md#capacitance)                  | F      |
| Inductance                              | [Henry](fundamentals.md#inductance)                   | H      |
| Frequency                               | [Hertz](https://en.wikipedia.org/wiki/Hertz)          | Hz[^1] |

[^1]: Why did we end up with this one that is _two letters_ rather than
    one like every other sane unit? Did an American sneak in?
    
### Prefixes

While you likely learned some of the basic (milli, kilo, etc.) prefixes
of the SI (ney metric) system, in electronics, we often use others that
you may not have learned. We'll break them into "small things" and "big
things". There are others that you will see, [which you can find
here](https://en.wikipedia.org/wiki/Metric_prefix), but almost never in
electronics (so far!).

For each of the prefixes, I'll denote what components you might
typically see these prefixes around. They'll be noted as capacitors (C),
inductors (L), and resistors (R) as above.

#### Small Things

| Prefix | Symbol  |   Power |                   Scale | Words         | Component |
| ------ | ------- | ------: | ----------------------: | ------------- | --------- |
| -      | (none)  |   10^0^ |                       1 | unit          | C, L, R   |
| milli  | m       |  10^-3^ |                 1/1,000 | thousandth    | C, L, R   |
| micro  | &micro; |  10^-6^ |             1/1,000,000 | millionth     | C, L, R   |
| nano   | n       |  10^-9^ |         1/1,000,000,000 | billionth     | C, L      |
| pico   | p       | 10^-12^ |     1/1,000,000,000,000 | trillionth    | C         |
| femto  | f       | 10^-15^ | 1/1,000,000,000,000,000 | quadrillionth |           |

In the electronics world, you will see milli, micro, nano, and pico
quite frequentl. 1pF capacitors aren't uncommon at all, and while there
are use cases to talk about femtoamps (for example), it's not a
situation you are likely to ever come across.

#### Big Things

| Prefix | Symbol |  Power |                     Scale | Words        | Component |
| ------ | ------ | -----: | ------------------------: | ------------ | --------- |
| -      | (none) |  10^0^ |                         1 | unit         | C, L, R   |
| kilo   | k      |  10^3^ |                     1,000 | thousands    | R         |
| mega   | M      |  10^6^ |                 1,000,000 | millions     | R         |
| giga   | G      |  10^9^ |             1,000,000,000 | billions     | R         |
| tera   | T      | 10^12^ |         1,000,000,000,000 | trillions    |           |
| peta   | P      | 10^15^ |     1,000,000,000,000,000 | quadrillions |           |
| exa    | E      | 10^18^ | 1,000,000,000,000,000,000 | quintillions |           |

Like small values, we don't use the really huge values (normally). You
will see resistance measured up to gigaohms quite commonly. Other than
that, the only places you're likely to run into the bigger units is in
storage, bandwidth, and processing performance (TFLOPS, trillions of
floating port operations per second).

## Decibels

While nobody uses the original unit of measure, the bel, the decibel (deci
meaning tenth) is everywhere in electronics where signals are being processed in
non-digital circuits. While the decibel (dB) on its own is specifically a
_ratio_ between two signal levels and therefore expresses only relative
relationships. 

If you want to use an absolute value, you can add on a modifier to the dB
notation.There are a couple specialized ones that you will see, generally in
audio or RF circuits:

| dB Units | Meaning                               |
| -------- | ------------------------------------- |
| dBV      | Decibels relative to 1 Volt           |
| dBm      | Decibels relative to 1 milliwatt (mW) |


For handy use, here's a table of some common conversions between decibels and
how they reflect in $V$, $I$, or $P$.

| Decibels | $V$ or $I$ Multiplier | $P$ Multiplier                     |
| -------- | --------------------- | ---------------------------------- |
| +40 dB   | $100$                 | $10000$ or $10^4$                  |
| +30      | $\sqrt{100}$          | $1000$ or $10^3$                   |
| +20 dB   | $10$                  | $100$ or $10^2$                    |
| +10 dB   | $\sqrt{10}$           | $10$ or $10^1$                     |
| +6 dB    | $2$                   | $4$ or $10^{0.60206\ldots}$        |
| +3 dB    | $\sqrt{2}$            | $2$ or $10^{0.30103\ldots}$        |
| 0 dB     | $1$                   | $1$ or $10^0$                      |
| -3 dB    | $\sqrt{1\over2}$      | $1\over2$ or $10^{-0.30103\ldots}$ |
| -6 dB    | $1\over2$             | $1\over4$ ot $10^{-0.60206\ldots}$ |
| -10 dB   | $\sqrt{1\over10}$     | $1\over10$ or $10^{-1}$            |
| -20 dB   | $1\over10$            | $1\over100$ or $10^{-2}$           |
| -30 dB   | $\sqrt{1\over100}$    | $1\over1000$ or $10^{-3}$          |
| -40 dB   | $1\over100$           | $1\over10000$ or $10^{-4}$         |

This is just a fleshed out version of this equation for voltage ($V$) and
current ($I$):

$$A=20log{{V_{out}\over V_{in}}}$$

Since power ($P$), measured in watts, is proportional to the square of the
voltage ($V$), a 10X increase in voltage results in a $10^2 = 100$X increase in
power, or 20dB. This converts the equation above into:

$$A=10log{{P_{out}}\over{{P}_{in}}}$$

These all end up being derived from (for $A$ dB):

$${V_{out}\over{V_{in}}} = {10^{(A/20)}} \\[10pt]
{P_{out}\over{P_{in}}} = {10^{(A/10)}}$$