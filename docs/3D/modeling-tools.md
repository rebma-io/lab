# Modeling Tools

Before discussing 3D modeling tools, I wanted to put out some of the things that
I was looking for in a tool:

1. Parametric. The tool absolutely must be built on the idea of parametric
   design, and allow for ongoing evolution by adjusting the parameters and then
   re-solving the design. 
2. Integrated MCAD/ECAD. When building something that combines something like 3D
   printing and electronics, it's supper helpful to be able to round-trip between
   the mechanicals and the PCB layout. This can help ensure your shapes all fit
   the way you expect, including holes and mounting features.
3. Simulation capabilities. This means both things like
   [LTSpice](https://en.wikipedia.org/wiki/LTspice) for electronics, but also
   various forms of FEM like static-stress. This is helpful in figuring out how
   something you're designing that has to bear some amount of load (static at
   least) will react.
4. Rendering. It'd be nice to have some decent rendering capabilities.
5. Documentation capabilities. 3D models are great, but when the
   rubber-meets-the-road, most organizations are driven by 2D drawings. Being
   able to create these and have them dynamically updates will be infinitely
   better than my manual drafting in highschool.

For my purposes, I settled on using
[Fusion360](https://www.autodesk.com/products/fusion-360/overview?term=1-YEAR&tab=subscription)
and pay for a regular subscription annually. See my discussion
[elsewhere](fusion360.md) as to the license tradeoffs.

## Alternatives to Fusion360

Note that these are all parametric modelers. Parametric modelers use a 3D
modelling technique based on computational methodology to manipulate the
geometry. It happens using parameters which are (adjustable) geometric
properties of a design model. 

### 3DEXPERIENCE SOLIDWORKS

[$99 USD for Makers,
[website](https://www.solidworks.com/solution/3dexperience-solidworks-makers)]
Based on the recommendations of a friend, this is the application I started
with. It is insanely powerful, and definitely "industrial grade" tooling. The
Maker edition does have some limits (such as watermarking things), but likely is
fine for most people's use. The main reason I stopped using it is that it
crashed more than I would like, and the website is absolutely _impenetrable_.
Seriously, it may be the worst website I've ever interacted with, and it's often
necessary to get things done. There's a [comparison of Fusion360 and
SOLIDWORKS](https://all3dp.com/2/fusion-360-vs-solidworks-cad-software-compared-side-by-side/)
you can read.

SOLIDWORKS doesn't work on macOS, although there is a web interface for some of
the tools.

### FreeCAD

[Open Source, [website](https://www.freecad.org/)] The closest thing to
SOLIDWORKS or Fusion360. And while I know a lot of people have a lot of love for
the tool, I've not had the best of luck with it from a stability perspective. I
also find it more difficult to use than either Fusion360 or SOLIDWORKS (which
share a huge amount in common).


### OpenSCAD

[Open Source, [website](https://openscad.org/)] Another parametric modeller, but
this one uses a scripting language to drive it's modeling, rather than inferring
the model from the interactive use of the system. This might be easier for some
people to think about, and it definitely encourages you to use parameters much
more. For a starter system, though, I think it's not supper intuitive for most
people. You can [read the
tutorial](https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/Chapter_1) to see how
you feel about it.


### Onshape

[Free - $2,500 USD, [website](https://www.onshape.com/en/)] In spite of being a web-only application, Onshape is an serious tool. Where it
excels is in collaboration (obviously), even supporting simultaneous multi-user
editing. The "free" (as in beer) version has a couple of limitations that made
it potentially uninteresting. First, you can't use it for commercial projects.
Second, all your work will be public. Lastly, you're missing both the PCB
functionality and the rendering. 

## Accessories to Make Your Life Better

### SpaceMouse

If you do any amount of 3D modeling, and can spare a few extra dollars, I cannot
recommend the [3DConnexion SpaceMouse
Compact](https://3dconnexion.com/uk/product/spacemouse-compact/). It brings you
6 degrees-of-freedom in movement and allows you to interact with a model as
though you are holding it. While it takes a day or two to get comfortable with,
it's now second nature and a wildly more productive way to manipulate things.

![SpaceMouse Compact](/img/spacemouse-compact.jpg)

Note that it doesn't replace your mouse/trackball, but instead augments it.


### El Gato StreamDeck

Harking back to the old button boxes on CAD workstation, the
[StreamDeck](https://www.elgato.com/us/en/s/welcome-to-stream-deck) may be built
for streamers, but it works great as a button box for 3D modeling. I have mine
installed along with the SpaceMouse in a 3D printed
[enclosure](https://www.printables.com/model/42505-spacemouse-streamdeck-mount).