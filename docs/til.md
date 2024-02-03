# Today I Learned

NOTE: A lot of times, I find little bits of information that aren't
really enough to write an entire thing about, but I'd like to share them
with people. That's what this little section is for. The idea was
[inspired by Simon Willison](https://til.simonwillison.net/).

* _2024-02-02_. As of 7.0.5 (I think) of KiCad on macOS, they have
  disabled support for the Space Mouse due to some perceived flakiness.
  I'm unclear what this is given I've never experienced anything but
  rock solid support in things like Fusion and Solidworks. It is
  possible to get it back by following the instructions in [this
  ticket](https://gitlab.com/kicad/code/kicad/-/issues/14847), which is
  completely not obvious.
* _2023-11-23_. Learning to use [telescoping bore
  gauges](https://www.mcmaster.com/products/hole-gauges/economy-telescoping-bore-gauge-sets/)
  can be super challenging. It requires developing a _feel_ for when
  it's properly situated. Someone mentioned getting some known good and
  precise bores to work with. Some examples were bronze bearings, which
  are both inexpensive and very precisely made.
* _2023-11-11_. I've been digging into Ada recently, and had a problem
  getting [Alire](https://alire.ada.dev/) and Visual Studio Code to play
  nicely with one another. Thanks to [Rob](https://tech.lgbt/@robdaemon)
  for the tip that you need to start VSC with `alr exec -- code .` in
  the directory with the Ada Project