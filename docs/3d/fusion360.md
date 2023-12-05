---
tags:
  - 3d
  - fusion-360
  - licensing
  - parametric-modeling
  - tips
---
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
abstract your project. Think of a component as a part. There are a few other
advantages to using components extensively:

* The joints in the Assembly menu only work with components.
* Drawings can only be created from components. On activation, the
  timeline is filtered. This means it will only show items in the
  timeline that pertain to that component. The timeline on a big project
  can become unwieldy, and this will make the quickly growing timeline
  much easier to work with.
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

Name your things. Most everything can be named in Fusion 360, but you
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
* [Component color
  cycling](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-Toggle-Component-Cycling-Color-in-Fusion-360.html)
  is an amazing way to view your models when you have a bunch of
  components. Rather than just using the
  [appearance](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-D59206EC-875D-4890-8088-AD23E5364951),
  it ensures that every component is distinct from all the ones around
  it.
* All of the analysis capabilities are insanely useful, and you should
  familiarize yourself with them, but I would definitely start with
  [section
  analysis](https://help.autodesk.com/view/fusion360/ENU/?guid=SLD-SECTION-ANALYSIS),
  which allows you to cut through the component and see what is going on
  inside. This will also show how multiple components interact clearly.
  
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
  haven't needed the features (although I may buy just to support the
  author).
* [AnyShortcut](https://apps.autodesk.com/FUSION/en/Detail/Index?id=156700835167123223).
  This allows you to create a keyboard shortcut for things in Fusion 360
  that don't have one. This is especially useful in integrating with an
  El Gato Stream Deck.
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