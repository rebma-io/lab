# Fundamental Equations

None of this is unique, original, or otherwise only found here, but I thought it
might be useful to collect things that people should probably know about.

## Ohm's Law

This is where it always begins, right? Ohm's law states that the current ($I$)
through aconductor between two points is directly proportional to the voltage
($V$) across the two points. This is represented in the following equation:

$$I = {V\over R}$$

The voltage ($V$) is always measured _across_ a conductor; it simply doesn't
exist without that context. $R$ is the resistance of the conductor. Ohm's law
states that $R$ is a constant, independent of the current. 

The great thing about this is you can, through the magic of mathematics, flip it
all over and around. You can get the voltage with $V=IR$, or the resistance
($R$) through $R={V\over I}$. Or you can organize it into a pretty wheel to
solve for all sorts of things depending on what you have (note $P$ is power in
watts):

![The wheel of Ohm's Law](/img/ohms-law-wheel.png)

For example, if you need to understand the current ($I$), and you only have
power ($P$) and resistance ($R$), you can use $\sqrt{P/R}$.

Know this one simple thing will carry you _very far_ in electronics.

