# Fundamentals

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

> NOTE: **Knowing Things** We talk about knowing things a lot, but what exactly
> do we mean by "know". Knowledge can come from two potential sources:
>
> * Extrinsically controlled (or fixed). If we have a voltage source which
>   always outputs 7.3 Volts, then the voltage is known because it is being
>   controlled and set to a specific value.
> * Measured. We can measure a voltage of 7.3 Volts across the output of a
>   regulator. This is known because it is measured, rather than fixed by some process.

The great thing about this is you can, through the magic of mathematics, flip it
all over and around depending on what you know. You can get the voltage with
$V=IR$, or the resistance ($R$) through $R={V\over I}$. Or you can organize it
into a pretty wheel to solve for all sorts of things depending on what you have
(note $P$ is power in watts):

![The wheel of Ohm's Law](/img/ohms-law-wheel.png)

For example, if you need to understand the current ($I$), and you only have
power ($P$) and resistance ($R$), you can use $\sqrt{P/R}$.

This one simple thing will carry you _very far_ in electronics.



### Resistivity in Ohmic Materials

Resistance is a property of the materials being used, as well as their physical
dimensions. You can calculate the resistance as:

$$R = \rho{L\over A}$$

where $A$ is the cross-sectional area (in meters), and $L$ is the length (also
in meters). $\rho$ is the intrinsic  resistive property of the material,
although it does change with temperature. 

For example, here's a [few different
materials](https://www.thoughtco.com/table-of-electrical-resistivity-conductivity-608499)
and their $\rho$ values:

| Material  | $\rho$ at 20C        |
| --------- | -------------------- |
| Copper    | $1.68\times 10^{-8}$ |
| Aluminum  | $2.82\times 10^{-8}$ |
| Iron      | $1.0\times 10^{-7}$  |
| Sea water | $2.0\times 10^{-1}$  |
| Air       | $2.3\times 10^{16}$ (approximately) |

### Limits of Linearity

While Ohm’s Law states that resistance is a linear function, this rule is not
universal and is in fact empirical. It is actually a linearized model of
trillions or more of atomic (and quantum) scale interactions within a material,
and it turns out that on average, the aggregated behavior looks roughly linear.
This is a recurring theme, but you can also completely ignore this nearly all
the time.