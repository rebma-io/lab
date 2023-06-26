# Fusion360


## Add-Ons and Extensibility

One thing I really like about Fusion360 is that there's an extensive [ecosystem
of apps](https://apps.autodesk.com/FUSION/en/Home/Index) or add-ons that allow
you to extend the tool in fun and pretty amazing ways. Similar to AutoCAD,
nearly everything inside Fusion360 is [exposed programmatically](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-C1545D80-D804-4CF3-886D-9B5C54B2D7A2). You can write
extensions in either Python or C++ (although the electronics design still uses
the EAGLE [user language
programming](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-C1545D80-D804-4CF3-886D-9B5C54B2D7A2)).

I use a few plugins somewhat regularly:

* [3D Print
  Plus](https://apps.autodesk.com/FUSION/en/Detail/Index?id=2942207745179825936&appLang=en&os=Win64).
  This provides a much more advanced way to send STL to a slicer if you don't
  want to use the FFF slicing capabilities inside Fusion360 itself. The only
  "problem" is that it can only send a single body at a time, which, if you want
  to print a bunch of bodies, can be painful. There is a pro version, but I
  haven't needed the features (although I may buy just to support the author).
* [Additive
  Assistant](https://apps.autodesk.com/FUSION/en/Detail/Index?id=9068625559069345798&appLang=en&os=Win64).
  Provides a bunch of additional analysis tools for FFF manufacturing around
  things like overhang, warp, poor bed adhesion, etc. This runs in the Design
  workspace.
* [DirectName](https://apps.autodesk.com/FUSION/en/Detail/Index?id=7497198800232664541&appLang=en&os=Win64).
  Rule #1: thou shalt always use components. Rule #2: name your stuff. This
  prompts you to name everything (bodies, features, sketches, etc) immediately,
  rather than creating them and then requiring you to go back and rename them.
  While it is, initially, annoying, it sure does help keep things clean and
  understandable in the timeline.
* [GFGearGenerator](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1236778940008086660&appLang=en&os=Win64).
  Lets you design gears in 3D very simply. Won't go into anything super-exotic,
  but it solves problems quickly.
* [No Component
  Warn](https://apps.autodesk.com/FUSION/en/Detail/Index?id=5188175718375703395&appLang=en&os=Win64).
  Nanny plugin to make sure you always put things in a component (rude #1). It
  also catches mistakes where you're using the wrong component and adding
  something to it.
* [ParametricText](https://apps.autodesk.com/FUSION/en/Detail/Index?id=2114937992453312456&appLang=en&os=Mac).
  Provides parameters for text. Weirdly, this is something you can't do with the
  regular parameters. It also has access to variables that you can use which are
  covered in the [excellent
  documentation](https://parametrictext.readthedocs.io/en/stable/). Use it. Use
  it all the time.
* [SnapEDA](https://apps.autodesk.com/FUSION/en/Detail/Index?id=5446990520022318629&appLang=en&os=Win64).
  Provides access (Windows only) to [SnapEDA](https://www.snapeda.com/)'s
  extensive library of components. 
* [Voronoi](https://apps.autodesk.com/FUSION/en/Detail/Index?id=1006119760063675415&appLang=en&os=Mac).
  Helps you generate [Voronoi
  diagrams](https://en.wikipedia.org/wiki/Voronoi_diagram). The plugin isn't
  particularly great, and it has a tendency to put the generated diagrams in
  entirely the wrong plane, but it's free and generates decent quality results
  that you can move where you need them.

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
$495 USD (2023-6) that it will cost.

## Random Bits of Information

* For text, you have to use a TrueType font (ttf), not an OpenType (otf)
  font, at least in Windows. If you use OTF, you will get errors like
  "could not retrieve the profiles of the selected text".
* [How to use global parameters across many different
  files](https://productdesignonline.com/how-to-create-and-use-global-parameters-in-fusion-360/),
  although it's a pain in the ass.