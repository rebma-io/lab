---
tags:
  - 3d
  - design
  - methodology
---
# Design Methodology

There are three major approaches to how you go about building out an
entire product/design. Start at the top, start at the bottom, or start
in the middle. Let's try and quickly define them:

While Fusion 360 supports all of these, it _wants_ to use either
top-down or middle-out. No approach is pure, though, and this is just a
way to think about the process rather than some strict rule.

## Top-Down

For top-down designs, the parts' shapes, sizes, and locations are
designed in the larger assembly. For example:

> You can model a bracket so it is always the correct size to hold
> a motor, even if you move the motor. The system will automatically
> resizes the motor bracket. This is helpful for parts like brackets,
> fixtures, and housings, whose purpose is largely to hold other parts
> in their correct positions. You can also use top-down design on
> certain features (such as locating pins) of otherwise bottom-up parts.
    
The advantage of top-down design is that much less rework is needed when
design changes occur. The parts know how to update themselves based on
the way you created them.

You can use top-down design techniques on certain features of a part,
complete parts, or entire assemblies. In practice, designers typically
use top-down techniques to lay out their assemblies and to capture key
aspects of custom parts specific to their assemblies.

## Bottom-Up

Bottom-up design is the traditional "part first" method. You first
design and model parts, then insert them into an assembly and use mates
to position the parts. To change the parts, you must edit them
individually. These changes are then promoted to the assembly.

Bottom-up design is the preferred technique for off-the-shelf parts, or
standard components like hardware, pulleys, motors, etc. These parts do
not change their shape and size based on your design unless you choose a
different component.

## Middle-Out

The answer, as always, is often somewhere in the middle. Typically, you
begin with some existing components and design other parts as required
around them. For example, after looking at the design in your head, or
on paper, you might insert or create the grounded (base/immovable)
component . As you develop the assembly, place existing components or
create new ones in place, as required.