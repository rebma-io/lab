# PCB Design

## Calculators

There are a lot of things where you need to calculate the optimal dimension for
something. Here are a few calculators that can be super helpful:

### Trace Width and Current Capacity

[Sierra Circuits calculator](https://designertools.app.protoexpress.com/).
  
This will let you figure out just how wide your traces need to be for carrying
the power you're moving on the PCB you're having built. For example, if we need
to carry 1A on a PCB manufactured with 1oz copper (the norm/default) with a
ambient temperature of 25C and an allowed temperature rise of 15C (40C total
operating temperature), we can enter it and then click calculate next to the
conductor width, which is what you're solving for 99% of the time:

![Sierra Circuit's trace width
calculator](/img/sierra-circuits-trace-width-calculator.png)

This results in needing to use 7.6729 mils (thousands of an inch) for trace
width. We should use a safety margin of 50% or more (100% is preferrable), which
means we need traces around 11.5 mil wide.

## Checklist for Designs

I use the following checklist for every single design. It is definitely overkill
for any things, but I find consistency to be a helpful thing.

### Things Printed on the Design

- [ ] Name of the thing
- [ ] [Part number](../organization/part-numbers.md) w/version
- [ ] Serial/QC markings
- [ ] Reference designators (see [why you might not want to]())
- [ ] Values for all passives
- [ ] All ports labeled with human-readable markings
- [ ] All ports labeled with pinouts
- [ ] Component outlines
- [ ] Pin 1 indicated on all ICs using small dot
- [ ] Polarity indication for: power and ground, polarized capacitors, and all
  diodes.
- [ ] Probe points
- [ ] Switch settings (if it can fit)

The font size and line width of the silkscreen text depend on the type of
silkscreen method used for its application. For standard silkscreen printing,
you should use as large of font size and line width as possible without going
smaller than a 50 mil font size and a 7 mil line. Liquid Photo Imaging (LPI) can
go down to 4 mil line widths, while direct legend printing (DLT) using an inkjet
can go down to 3 mil. Make sure you understand what your vendor is using for your
case. 

## Design for Manufacturing (DFM)

TODO: Discuss Sierra Circuit's [DFM
tool](https://www.protoexpress.com/tools/pcb-dfm-tool/).


