---
tags:
  - logic-levels
  - voltage
  - signals
---
# Logic Levels and Families

There are a bunch of different voltages that are used in designing
circuits. The most common a hobbyist would run into are 5V and 3.3V.
But, they're not really 5V and 3.3V, but instead a combination of
thresholds that make up the family. For the purposes of this, we're
going to talk about the families that are common in the 74xx series of
logic circuits. 

## What is a Logic Low? A High?

![Hierarchy of logic levels for various
transitions](img/logic-levels.svg){: align=right width=150 }

We have to start by defining the various levels. There's a few, but they
should all make sense, taken from lowest voltage to highest:

* **GND**. The ground reference potential. Typically this is zero volts.
  This could also be referred to as V~EE~ or V~SS~.
* **V~OL~**. The target output level for the transmitter to send a logic
  low. The level must be between GND and V~OL~.
* **V~IL~**. The target input level for the receiver to interpret a
  logic low. Anything between GND and V~IL~ will be interpreted as logic
  low.
* **V~t~**. The transition voltage, which is the hard line between logic
  high and low. This is the minimum potential to cause current to flow
  within the device's internal transistors.
* **V~IH~** The target input level for a receiver to interpret a logic
  high. Anything between V~IH~ and V~CC~ should be considered a high.
* **V~OH~**. The target output level for a transmitter to send a logic
  high. Anything between V~OH~ and V~CC~ is acceptable.
* **V~CC~**. The main positive voltage for the design. This can also be
  called V~DD~.

## Families of Logic

All of the logic out there typically falls into one of a couple of
families (mostly defined by JEDEC):

* 5V TTL
* 5V CMOS
* 3.3V CMOS or TTL (typically identical)
* 2.5V CMOS
* 1.8V CMOS

For each of those, they have the following levels in volts:

| Level | 5V TTL  | 5V CMOS | 3.3V CMOS | 2.5V CMOS | 1.8V CMOS |
| ----- | ------- | ------- | --------- | --------- | --------- |
| V~CC~ | 4.5-5.5 | 4.5-5.5 | 2.7-3.6   | 2.3-2.7   | 1.65-1.95 |
| V~OH~ | 2.4     | 4.44    | 2.4       | 2.0       | 1.2       |
| V~IH~ | 2.0     | 3.5     | 2.0       | 1.7       | 1.17      |
| V~t~  | 1.5     | 2.5     | 1.5       | 1.2       | 0.9       |
| V~IL~ | 0.8     | 1.5     | 0.8       | 0.7       | 0.68      |
| V~OL~ | 0.4     | 0.5     | 0.4       | 0.2       | 0.45      |
| GND   | 0       | V       | 0         | 0         | 0         |

> NOTE: **Voltage Tolerance and Compliance** A device that is voltage
> tolerant can withstand a voltage greater than its V~CC~ on its I/O pins.
> For example, if a device has a V~CC~ of 2.5 V and can accept inputs equal
> to 3.3V and can withstand 3.3V on its outputs, the 2.5V device is
> called 3.3V tolerant. A device which is voltage compliant can receive
> signals from and transmit signals to a device which is operated at a
> voltage greater than its own V~CC~. For example, if a device has a
> 2.5V V~CC~ and can transmit and receive signals to and from a 3.3V
> device, the 2.5V device is said to be 3.3V compliant. 

## 74-Series Logic Families

WARNING: **Large Topic** I should probably write an entire thing on
74-series logic, as it's really the foundation of so many things
historically, and even still in the most advanced systems, you'll find a
smattering of "glue logic" implemented in 74-series logic. For now, I'm
just going to wave my hand at it, and discuss the families. 

If we convert this to 74-series logic, we can see how they various logic
families (those crazy letters in the middle of part numbers) fit
together. For example, for TI, this is just some of the families, and
really you have to pull apart what exactly you need:

| Logic Voltage | Families                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| 5V            | ABT, AC/ACT, AHC, AHCT, ALS, AS, BCT, F, LV, LV1T, LV-A, LS, S, TTL, FCT2 |
| 3.3V          | AC, AHC, ALB, ALVC, ALVT, AUP, AVC, LV, LV-A, LVC, LVT, LV1T, AUP1T       |
| 2.5V          | ALVC, ALVT, AUC, AUP, AVC, LV, LV1T, LV-A, LVC                            |
| 1.8V          | ALVC, AUC, AUP, AVC, LVC, LV1T                                            |

Note that the CD4000 family typically fits under the 5V heading. In
addition, there are families with even lower voltage levels available,
but they're unlikely to show up anywhere near a hobbyist.

For me, I typically will use LVC or AHC for 3.3V and ACT for 5V. 