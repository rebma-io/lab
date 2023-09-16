---
tags:
  - measurement
  - metrology
  - standards
---
# Science of Measurement

WARNING: **Super High Level** This document is very high-level, and is
based on my primitive and basic understanding of amazingly advanced and
complicated topics. I've tried to impart a few things that I've learned
that have helped me over the years.

This is probably better termed "how to not suck at measuring things".
There is actually a full science behind measuring things called
metrology. Metrology is a crazy topic full of rabbit holes inside rabbit
holes. Wikipedia [defines
metrology](https://en.wikipedia.org/wiki/Metrology) as:

> Metrology is the scientific study of measurement. It establishes a
> common understanding of units, crucial in linking human activities.
> [...] Metrology is divided into three basic overlapping activities:
>
> * The definition of units of measurement
> * The realization of these units of measurement in practice
> * Traceability—linking measurements made in practice to the reference standards
> 
> These overlapping activities are used in varying degrees by the three
> basic sub-fields of metrology:
> 
> * Scientific or fundamental metrology, concerned with the
>   establishment of units of measurement.
> * Applied, technical or industrial metrology—the application of
>   measurement to manufacturing and other processes in society. 
> * Legal metrology, covering the regulation and statutory requirements
>   for measuring instruments and methods of measurement.

## Quick Note About Systems

There is really only a single system of measure: the metric system. The
reality is that everything else is defined in reference to the metric
system. For example, the inch is defined, [at least since the
1960s](https://en.wikipedia.org/wiki/Inch), as 25.4mm _exactly_.  There
are still places that use the imperial (inch) system for things, such as
US machinists, but by and large the world runs on metric explicitly. For
the rest of this, I'm going to use the metric system because it is less
annoying. 

## Precision and Accuracy

In a college math class, we were asked a question: "What's the
difference between precision and accuracy?" My answer was that accuracy
is how close you are to the "correct" answer, and precision was how many
digits you had in your answer. This is both correct(ish) and also wrong.
Instead, we should define them this way:

_Accuracy_
: The accuracy indicates how well it agrees with the (conventional) true
value.

_Precision_
: The precision of an instrument refers to the dispersion of
measurements.

You can think of precision as the repeatability of your measurements. If
the black line in the center is our _true value_, and the magenta dots
are our measurements:

![Precision versus accuracy on a line](img/precision-accuracy.png)

It is really important to get this into your head quite deeply:

** We can never achieve perfection in measurement. No matter how precise and
accurate a measurement is, it will have some remaining uncertainty.**

NOTE: **Before You Begin** Before you get too concerned with precision
and accuracy, you should make a very deliberate decision about how much
you actually need. If you are working in machining and similar fields,
then "thous" (1/1000 of an inch) are a common thing to worry about, and
many things are measured in "tens" (1/10,000 of an inch). For 3D
printing, we're lucky to hit 1/100th of an inch.

## 3rd Party Resources

* National Physical Laboratory (UK)
    * [Beginner's Guide to Measurement
      (GPG118)](https://www.npl.co.uk/gpgs/beginners-guide-to-measurement) 
    * [Beginner's Guide to Measurement in Mechanical Engineering
      (GPG131)](https://www.npl.co.uk/
      gpgs/measurement-mechanical-engineering-guide)
    * [Dimensional Metrology
    (GPG80)](https://www.npl.co.uk/gpgs/dimensional-metrology-guide)
    * [Design and Interpretation of Engineering Drawings for Measurement
    Processes (GPG79)](https://www.npl.co.uk/gpgs/engineering-drawings-for-measurement-processes)
* [Adam Savage discussing his views of measurement and
  accuracy](https://www.youtube.com/watch?v=qE7dYhpI_bI)