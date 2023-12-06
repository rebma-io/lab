---
tags:
  - comparison
  - jlcpcb
  - pcb
  - pcbway
  - pricing
---
# Comparison of Chinese PCB Manufacturers by Size/Layers/Finish

NOTE: **Where's the Domestic Manufacturers?** That's a great question.
Unfortunately, they're simply not even in the same price ballpark as the
Chinese manufacturers. This likely comes down to two characteristics: 1)
volume; 2) most domestic companies don't do anything that isn't high
end, as that's where the margin really is.

There's a project I'm working on that I'm trying to figure out the right
PCB size for. To do that, I figured I'd take a look at various
parameters and how they impact the pricing with the two biggest Chinese
PCB makers: PCBWay and JLCPCB. The parameters I'm comparing are:

1. Dimensions
2. Layer count (2 and 4 layers)
3. Surface finish (HASL v ENIG)

This is a pretty big spreadsheet, and you can find it here: 
[[ link_for_download("pcb-manufacturer-pricing-comparison.xlsx",
license="CC-BY 4.0") ]], but here's the top-level results:

![Spreadsheet comparing pricing for PCBWay and
JLCPCB](img/pcb-pricing-comparison-20231205.png)

A few observations that stand out for me:

1. JLCPCB is never more expensive than PCBWay, and often less than 1/2
   the price. Given a recent [comparison](supplier-comparison.md), it's
   hard to see why PCBWay is so much more.
2. The delta between HASL finish and ENIG for JLCPCB is much less,
   making it far more attractive. In fact, JLCPCB w/ENIG is almost
   always cheaper than PCBWay with HASL. :exploding_head:
3. There's a definite cost hit the minute you go over 100mm in any
   dimension. This likely has something to do with their overall size
   and how they put various orders together. The cost then drops per
   cm^2^ after that.

A few things that weren't really considered:

* Difference in shipping. Both offer a lot, and they seemed to be about
  the same pricing.
* Solder mask color. Both offer more than green, and sometimes they're
  free and other times the combination costs money. White on green is a
  good baseline.
