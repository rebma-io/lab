# Joining Parts

When joining parts, there's one question you need to start with: is this
reversible? That will guide you down the path of what technique to use. There
are a couple ways to join parts together, each with their own trade-offs:

* Press fit. Typically non-reversible.
* Snap fit. Reversible.
* Glue. Non-reversible.
* Screws. Reversible.

## Press Fit

If you can get the [mechanical fit](/mechanical/fit.md) setup correct, then you
may be able to use an interference fit and stick things together without any
other mechanism. Unfortunately, you also run the risk of breaking the parts
doing this, so I strongly advise against it.

## Snap Fit

Snap fit is a common way of making injection-molded parts fit together, but it
can also be used in 3D printing. A snap fit set of pars usually consists of a
protrusion and a mating depression, generating an interlocking connection that
often relies on parts that bend. There are many guides on creating them, but I
like [this
one](https://all3dp.com/2/3d-printing-snap-fit-design-simply-explained/) as a start.

## Glue

Using glue is a great option, and there are three primary glues that are
commonly used:

* [Cyanoacrylate](https://en.wikipedia.org/wiki/Cyanoacrylate) ("super glue")
* UV-set epoxy. I like [Bondic](https://bondic-store.com).
* [Hot glue](https://en.wikipedia.org/wiki/Hot-melt_adhesive), which is actually
  a [thermopastic](https://en.wikipedia.org/wiki/Thermoplastic) and not a
  traditional adhesive.

Each of these has trade-offs, but the first two are the most durable and
strongest. The hot glue is useful for more temporary things, or things where
there will not be much stress on the joint.

## Screws

Screws are a great way to join two or more printed parts together in a
semi-permanent fashion. There are a few possibilities in how you can screw them
together that I'm going to cover here. Stefan over at CNC Kitchen has done a
[good
comparison](https://www.cnckitchen.com/blog/helicoils-threaded-insets-and-embedded-nuts-in-3d-prints-strength-amp-strength-assessment)
of various techniques from a strength perspective.

### Just Screw It In

Honestly, you can just screw a lot of screws in, and certainly a [self-tapping
screws](https://en.wikipedia.org/wiki/Self-tapping_screw) should work.
Unfortunately, this is not a super repeatable process, and 

### Tapping Holes

The next option is to use a [tap and die
set](https://en.wikipedia.org/wiki/Tap_and_die) to pre-cut the theads into the
printed part. This will reduce the tension in the part, and ensure a much
cleaner join as the taps are _very sharp_. For the best results, you'll want to
tap the hole twice. The first time using either a plug or taper tap, and the
second time using a bottoming tap. The first will make sure 90% of the threads
are cut, and the bottoming tap will ensure the last few at the bottom are cut
properly. If you try to use a bottoming tap by itself, you'll find that it will
struggle to get the initial bite into the material and to stay straight.

To help explain it, I made a small video:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RjGXpc7K3p0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Threaded Inserts

My favorite is to use brass threaded inserts. These are inserts that are heat
set into the printed part and provide a durable and repeatable joint. The ones I
like are from Stefan at [CNC Kitchen](https://cnckitchen.store), and look like
this: 

[![M3 threaded insert from CNC
Kitchen](/img/cnc-kitchen-threaded-insert.jpg)](https://cnckitchen.store)

You can also get quality examples from
[McMaster-Carr](https://www.mcmaster.com/products/threaded-inserts/for-use-in~plastic/)
who stocks an even wider variety in even more materials. There are other brands,
but I've found these to be of the best quality and have never failed me. You'll
also really want to get the [soldering
tips](https://cnckitchen.store/products/einschmelzhilfen-soldering-tips-m2-m2-5-m3-m4-m5-m6-1-4-m8-100-lead-and-cadmium-free)
that will make it much easier to use (assuming your soldering iron supports
either T18 or 900M tips). You'll definitely want to print the [storage
case](https://www.printables.com/model/167924-case-for-cnc-kitchen-threaded-inserts-soldering-ti)
and if you happen to have a [Dremel 220-01
workstation](https://www.dremel.com/us/en/p/220-01-26150220aa), you can print an
[adapter](https://www.thingiverse.com/thing:5480597) that will let you use it to
depress your soldering iron and ensure a clean insert at the correct angle.

Hackaday has [a great
article](https://hackaday.com/2019/02/28/threading-3d-printed-parts-how-to-use-heat-set-inserts/)
detailing how to design parts for threaded inserts and how to properly install
them. I find using a temperature about 5C above the filament print temperature
works well.