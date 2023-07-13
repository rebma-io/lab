# Fusion 360

Currently, I use [Fusion
360](https://www.autodesk.com/products/fusion-360/overview) for all of
my 3D and ECAD work. I'm trying to collect together things I've learned,
and recommendations here.

## Rules for Success

There are two critical rules that the community has developed over the
years, and I highly recommend following them:

1. Everything goes into a component.
2. Everything has a name.

Let's take the two separately.

### Rule #1: Components

Components are a container for sketches, geometry, joint origins, bodies, etc.
This helps organize things. This makes it much easier to think about and
abstract your project. Think of a component as a part. There's a few other
advantages to using components extensively:

* The joints in the Assembly menu only work with components.
* Drawings can only be created from components
* On activation the timeline is filtered. This means it will only show
  items in the timeline that pertain to that component. The timeline on
  a big project can become unwieldy, and this will make the quickly
  growing timeline much easier to work with.
* When you export a component with "save as" Fusion 360 will also export
  the complete parametric design history.
* Only components show on the BOM.
* Only components can be added to [selection
  sets](https://help.autodesk.com/view/fusion360/ENU/?guid=SLD-CREATE-SELECTION-SETS).
  Selection sets are a way to "name" a specific group of items that you
  can refer to again and again consistently.
* Only components can be isolated. This allows you to make everything
  but one component "disappear" from the design, and ensure you don't
  accidentally affect them.
* You can make copies of a component, but keep linked changes (or not if
  you want). This can be super helpful in larger assemblies. 

There's also a [write
up](https://www.autodesk.com/products/fusion-360/blog/5-things-you-should-know-about-components-and-bodies/)
on the difference between components and bodies. This is super important
to understand. Also, some [strategies for using
components](https://www.autodesk.com/products/fusion-360/blog/5-time-saving-strategies-assembly-design/).

Note that this is a soft rule, not a hard rule. Following it blindly,
like so many rules, [can result in
failure](https://www.autodesk.com/products/fusion-360/blog/quick-tip-rule-1-oversight/). 


### Rule #2: Names

Name your things. Most everyting can be named in Fusion 360, but you
_definitely_ want to name these things:

* Sketches
* Bodies
* Construction planes
* Section analysis
* Views
* Components

You can also name extrusions, chamfers, and a lot of other things.
Whether you name this or not is up to you, but if you do name them, then
in the design history timeline, you'll see more information, which may
make it easier to navigate larger timelines.

Finally, name them clearly, and I tend to use somewhat long-winded names, often
going from coarse to fine granularity. If this is something
"structured", I might even include [part
numbers](../organization/part-numbers.md).

## Tips and Tricks

* [Learn to use the S-key
  functionality](https://www.autodesk.com/products/fusion-360/blog/quick-tip-the-s-key/).
  This is a quick way to search for commands and execute them, or
  activate a tool. You can also pin commonly used commands to the menu.
  One thing to be aware of is that, for _some reason_, Fusion 360 will
  show you 3D commands when you're in 2D sketches, and so you need to be
  cognizant of the difference and the different icon.

## Add-Ons and Extensibility

One thing I really like about Fusion360 is that there's an extensive [ecosystem
of apps](https://apps.autodesk.com/FUSION/en/Home/Index) or add-ons that allow
you to extend the tool in fun and pretty amazing ways. Similar to AutoCAD,
nearly everything inside Fusion360 is [exposed programmatically](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-C1545D80-D804-4CF3-886D-9B5C54B2D7A2). You can write
extensions in either Python or C++ (although the electronics design still uses
the EAGLE [user language
programming](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-C1545D80-D804-4CF3-886D-9B5C54B2D7A2)).

I use a few plugins regularly:

* [3D Print
  Plus](https://apps.autodesk.com/FUSION/en/Detail/Index?id=2942207745179825936).
  This provides a much more advanced way to send STL to a slicer if you don't
  want to use the FFF slicing capabilities inside Fusion360 itself. The only
  "problem" is that it can only send a single body at a time, which, if you want
  to print a bunch of bodies, can be painful. There is a pro version, but I
  haven't needed the features (although I may buy just to support the author).
* [Additive
  Assistant](https://apps.autodesk.com/FUSION/en/Detail/Index?id=9068625559069345798).
  Provides a bunch of additional analysis tools for FFF manufacturing around
  things like overhang, warp, poor bed adhesion, etc. This runs in the Design
  workspace.
* [DirectName](https://apps.autodesk.com/FUSION/en/Detail/Index?id=7497198800232664541).
  Rule #1: thou shalt always use components. Rule #2: name your stuff. This
  prompts you to name everything (bodies, features, sketches, etc) immediately,
  rather than creating them and then requiring you to go back and rename them.
  While it is, initially, annoying, it sure does help keep things clean and
  understandable in the timeline.
* [Duplicate
  Components](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1864820821708132049).
  Automates the steps for creating instances or creating duplicate
  components in a design. This is great when you want to include things
  like screws in your designs.
* [GFGearGenerator](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1236778940008086660).
  Lets you design gears in 3D very simply. Won't go into anything super-exotic,
  but it solves problems quickly.
* [Install from
  Github](https://apps.autodesk.com/FUSION/en/Detail/Index?id=789800822168335025).
  Not everything is on the Autodesk "store". There's a bunch of things
  you can find on Github. This takes the project URL and installs it all
  for you automatically. It doesn't, unfortunately, automatically update
  the plugin, but instead just installs a zip of the current state.
* [No Component
  Warn](https://apps.autodesk.com/FUSION/en/Detail/Index?id=5188175718375703395).
  Nanny plugin to make sure you always put things in a component (rude #1). It
  also catches mistakes where you're using the wrong component and adding
  something to it.
* [Parameters
  I/O](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1801418194626000805).
  Allows you to import/export user parameters as a CSV. This is great
  way to get a bunch of "default" parameters. [See below for
  mine](#default-user-parameters).
* [ParametricText](https://apps.autodesk.com/FUSION/en/Detail/Index?id=2114937992453312456).
  Provides parameters for text. Weirdly, this is something you can't do with the
  regular parameters. It also has access to variables that you can use which are
  covered in the [excellent
  documentation](https://parametrictext.readthedocs.io/en/stable/). Use it. Use
  it all the time.
* [SnapEDA](https://apps.autodesk.com/FUSION/en/Detail/Index?id=5446990520022318629).
  Provides access (Windows only) to [SnapEDA](https://www.snapeda.com/)'s
  extensive library of components. 
* [Voronoi](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1006119760063675415).
  Helps you generate [Voronoi
  diagrams](https://en.wikipedia.org/wiki/Voronoi_diagram). The plugin isn't
  particularly great, and it has a tendency to put the generated diagrams in
  entirely the wrong plane, but it's free and generates decent quality results
  that you can move where you need them.

<!-- 
TODO: Evaluate Dogbone add-on https://apps.autodesk.com/FUSION/en/Detail/Index?id=3534533763590670806
TODO: Evaluate NetApp add-on
TODO: Evaluate Any Shortcuts add-on https://apps.autodesk.com/FUSION/en/Detail/Index?id=156700835167123223
TODO: Evaluate Gridfinity Generator https://apps.autodesk.com/FUSION/en/Detail/Index?id=7197558650811789
-->

## Default User Parameters

NOTE: **Global Parameters** Currently, Fusion360 doesn't have a concept
of global parameters that you can set for everything. This would be
awesome to have in this case, but not yet. [There are ways to fake
it](https://productdesignonline.com/how-to-create-and-use-global-parameters-in-fusion-360/),
but I find them overly complicated, and the CSV file with Parameters I/O
to be a much simpler solution. 

One of the most powerful things with a parametric modeling tool is being
able to create standard parameters that drive the model. Often, a lot of
these are references to external parts that you need to interact with,
like a screw. To simplify _my life_, I have put together a CSV that
contains:

* [Fits for my printer](../mechanical/fit.md): interference,
  transitional, clearance.
* Standard metric screws for M2 - M12 in all the default standard
  threads. This is for _socket head screws_, which are my go to. The
  insert and tap information will work for _any_ metric screw of that
  size and thread pitch (yay metric!). These are all just "standard"
  thread pitch.
* Sizes for [threaded inserts](joining-parts.md#threaded-inserts).

You can download the CSV from here: 
[[ link_for_download("f360_default_parameters.csv", license="CC-BY 4.0")
]]

You can import them quickly with the [Parameters
I/O](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1801418194626000805)
add-on that Autodesk provides (you'll need to install for some weird
reason). Once imported, if you look at user parameters, you'll see
something like this:

![Fusion360 user parameters dialog box showing a large number of
parameters](../img/f360-user-parameters-imported.png)

The naming is based on this pattern:

* `<type of fit>Fit<layer height without decimal>` for the various fits.
* `<size>Head<OD/Depth>` for the outside diameter (OD) and depth
  (height) of the screw.
* `<size>InsertHoleID` for the inside diameter (ID) of the hole
 you'll need to insert the insert.
* `<size>InsertDepth` for the depth of the insert when you do an extrude
  cut. Note there are also some `InsertShortDepth` for the CNC Kitchen
  short inserts.
* `<size>TapeHoleID` for the ID of the hole you'll need if you plan on
  [tapping the holes](joining-parts.md#tapping-holes).

I've provided references to where the data came from originally (for
example, the [McMaster-Carr](https://www.mcmaster.com/) screw part
numbers). There's a few things you might need to do:

1. You should update the fits for _your printer_. This is just for my
   Prusa MINI+, and won't necessarily match yours. It's a good start if
   you don't want to fuss about, although many cheap 3D printers have
   much bigger tolerances.
2. When you want to use `M3HeadOD` (for example), you'll want to allow
   for tolerance. I typically use `TransitionFit030`, which will get a
   snug fit that doesn't drag when you put the screw in. To do that,
   when you create the circle, just set the size to `M3HeadOD +
   TransitionFit030`. I didn't include the fit in the main size because
   different people want different fits in different situations.

## Personal License v Subscription

Autodesk has a "free" (as in beer) license available for "personal use". While
they have a [rudimentary
comparison](https://www.autodesk.com/products/fusion-360/personal), there are a
few things that absolutely drove me to spend the larger sum for a normal
subscription: 

* Max of 10 documents in read-write and everything else read-only. And you have
  to manually manage it.
* Super-limited electronics. 2 schematics and 2 layers. Nothing more.
* Drawings can only have a single sheet.
* No simulation capabilities.
* No access to cloud services (which aren't cheap, but are super powerful).

For getting started, though, it's 100% worth starting with the personal license
and figuring out if this is something you're serious enough about to drop the
[[usd("495.00", as_of="2023-06")]] that it will cost.

## Random Bits of Information

* For text, you have to use a TrueType font (ttf), not an OpenType (otf)
  font, at least in Windows. If you use OTF, you will get errors like
  "could not retrieve the profiles of the selected text".
* [How to use global parameters across many different
  files](https://productdesignonline.com/how-to-create-and-use-global-parameters-in-fusion-360/),
  although it's a pain in the ass.

## Learning Resources

Autodesk has a pretty great collection of courses up on Coursera for
free. The ones I've looked at are:

* [Introduction to Digital Manufacturing with Autodesk Fusion
  360](https://www.coursera.org/learn/introduction-digital-manufacturing-fusion-360)
* [Autodesk Fusion 360 Integrated CAD/CAM/CAE](https://www.coursera.org/learn/fusion-360-integrated-cad-cam-cae)
* [3D Model Creation with Autodesk Fusion 360](https://www.coursera.org/learn/3d-model-creation-fusion-360)
* [Engineering Design Process with Autodesk Fusion 360](https://www.coursera.org/learn/engineering-design-process-fusion-360)
* [Manufacturing Process with Autodesk Fusion 360](https://www.coursera.org/learn/manufacturing-process-fusion-360)

They have a huge number of [choices for
courses](https://www.coursera.org/autodesk) in a lot of topics,
depending on your interest area.

## 3rd Party Resources

* [Autodesk's Fusion 360 API](http://autodeskfusion360.github.io/)
* [Autodesk Community Gallery](https://www.autodesk.com/community/gallery)
* [Understanding bodies and components](https://productdesignonline.com/tips-and-tricks/understanding-bodies-and-components-fusion-360-rule-1/)