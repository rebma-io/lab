# Voltage Dividers

CONSTRUCTION: This is just under construction and is nowhere near ready
for review, but it's in the repo so I can keep track of it.

INFO: **Limits of Voltage Dividers** Voltage dividers are amazing
things, and you definitely will want to use a lot of them. They do have
their limitations though. Typically, a voltage divider is only useful
up to a small number of milliamps (mA). Above that, you absolutely need
a different solution, like a voltage regulator.

A voltage divider is an circuit using resistors (usually). It's main use
is generating a proportional drop in voltage as output depending on the
value of the resistors used. You get this voltage output by tapping
across one of the resistors to get the desired voltage drops.

## Arrangement of Resistors

There are a bunch of different arrangements of resistors that you might
see in a schematic to create a voltage divider:

![Voltage divider
arrangements](../img/schematic-voltage-divider-arrangements.png)

(A) is the "classic" example, and the one you'll see here and in
textbooks. (B) is a slightly re-oriented version. (C) is the one you're
most likely to see "in the wild". The reason fr that is that that 2.727V
output is likely fed into an IC or other circuit that also has a
connection to ground, so the 2.727V is referenced to the same ground.
All of these do _exactly the same thing_. 

## 3+ Resistors in a Divider Network

## Choosing Resistor Decades

NOTE: **Standing on Shoulders** This was something I didn't understand
very well, until about 4 years ago when I read [this
comment](https://electronics.stackexchange.com/a/28903) on Stack Exchange.
It also has links to interactive exploration of the circuits. I've used
similar circuits here, but would rather link to the original for the
detail. 

![Voltage divider with a pair of 100&ohm;
resistors](../img/schematic-voltage-divider-100ohm.png){: align=right }

_Current is king_. As is always the case. The resistors chosen have a
huge impact on not just the voltage, but also the current. So let's look
at a few circuits and run the numbers on them. If we look at the
voltage divider equation, we can figure out the voltage at TP1:

$$\begin{aligned}
V_{out} &= V_S{R_2\over{R_1 + R_2}}\\[5pt]
&=5{100\over{100 + 100}}\\[5pt]
&=5\cdot{1\over2}\\[5pt]
&=2.5\mathrm{V}
\end{aligned}$$

So we know this will create 5V of output, but what's the current? Well,
back to Ohm's Law. Let's look at the current at ground.

$$\begin{aligned}
I &= {V\over R}\\[5pt]
&= {5\over{200}}\\[5pt]
&= 0.025\mathrm{A} = 25\mathrm{mA}
\end{aligned}$$

![Voltage divider with a pair of 10k&ohm;
resistors](../img/schematic-voltage-divider-10kohm.png){: align=right }

So, we have 25mA of current at the ground node. What if we have
something with even bigger resistors? 

$$\begin{aligned}
I &= {5\over{20000}}\\[5pt]
&= 0.00025 = 250\mathrm{\mu A}
\end{aligned}$$

So great, bigger resistors equal less current. We can think of this as
the "wasted" current by the divider.

### Circuit Loading

![Voltage divider with a pair of 100&ohm; resistors and a 1k&ohm;
load](../img/schematic-voltage-divider-100ohm-loaded.png){: align=left }  But what if we
put it
under load, and what's the point if there's nothing hanging off the
voltage divider?  Let's say we have a 1k&ohm; load equivalent to the
circuit. Now, we have 2 parallel resistors in series with another. Don't
see it? Take a look at it this way.

![Voltage divider with a pair of 100&ohm; resistors and a 1k&phm; load,
reoriented](../img/schematic-voltage-divider-100ohm-loaded-parallel.png){: align=right }

Uh oh! 

So what does this end up looking like? Well, first, we have a parallel
resistor network, and we can use [the simplified
equation](fundamentals.md#series-and-parallel-circuits) of ${100 \times
1000}\over{100 + 1000}$ or $100000\over1100$ or $90.\overline{90}$&ohm;.
So what does that do to our divider?

$$\begin{aligned}
V_{out} &= V_S{R_2\over{R_1 + R_2}}\\[5pt]
&= 5{90.91\over{190.91}}\\[5pt]
&= 2.38\mathrm{V}
\end{aligned}$$

Woops! There went our 2.5V voltage reference! And basically everything
has a resistance as a load. 

===

![Generic voltage
divider](../img/schematic-voltage-divider-generic.png){: align=right }

So where does that leave us. Well, presuming we know what the load on
the voltage divider is going to be, we can just twist Ohm's Law around
to get what we need. I'm going to try and show my work here. Let's use
the generic voltage divider arrangement to the right.

$$\begin{aligned}
R_{2,3} &= {{R2\cdot R3}\over{R2 + R3}}\\[5pt]
V_{TP1} &= {R_{2,3}\over{R1 + R_{2,3}}}\\[5pt]
\end{aligned}$$

TIP: **Where to Start** For &micro;A loads, I'd start with things in the
100k&ohm; range. For mA loads, I'd start with 1-10k&ohm;. If you need
more than a few mA, then you really need a voltage regulator, not
a voltage divider.