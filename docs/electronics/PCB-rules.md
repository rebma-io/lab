# PCB Rules

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
