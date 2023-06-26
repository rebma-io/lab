# Units of Measure

There are a lot of units of measure that you end up working with. In
this section, I want to talk about a few that have always tripped me up,
and hopefully, by explaining them to others, I can better understand
them myself.

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