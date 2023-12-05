---
tags:
  - 3d
  - conventions
  - modeling
  - parametric-modeling
  - tips
---
# Parameters in Parametric Models

## Naming Scheme

Something I've learned the hard way is that you need to have a naming scheme
when you start to do a lot of parameters in your models. Otherwise, you end up
finding it difficult to identify which parameter you're looking for. Parameters
in Fusion360 can have alphanumeric characters and the following special
characters:

* `_` Underscore
* `"` Double Quote
* `$` Dollar symbol
* `°` Degree symbol
* `µ` Micro symbol

They cannot have a space, so I typically use
[PascalCase](https://en.wikipedia.org/wiki/Camel_case). This is the scheme I
use:

| Name         | Use                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------- |
| `*ID`        | Inside Diameter of a circle-like thing.                                                           |
| `*OD`        | Outside Diameter of a circle-like thing.                                                          |
| `*Depth`     | The depth of a hole                                                                               |
| `*Clearance` | Any specific clearance that you need to think about. Note this is different than fit (see below). |
| `*Count`     | Number of something (e.g., holes) in a surface or body.                                           |


In addition, I always create the following three parameters to allow for
modeling of various [types of fit](../mechanical/fit.md) if something is
going to be 3D printed.

| Name            | Use                                |
| --------------- | ---------------------------------- |
| ClearanceFit    | Allowance for a clearance fit.     |
| TransitionFit   | Allowance for a transition fit.    |
| InterferenceFit | Allowance for an interference fit. |


## Calculations

Starting with the May 2023 release of Fusion360, you can now use conditional
operations in your parameters. This is covered [in the
reference](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-76272551-3275-46C4-AE4D-10D58B408C20).
This opens up a huge new arena for exploration. For example, you could do
something (simplified) like this for the number of holes in a hub:

HoleCount = `if(HubOD >= 100mm; 7; 5)`

This would set the `HoleCount` to `7` if the `HubOD` (hub outer diameter) is
greater than or equal to 100mm. You can also chain them together:

HoleCount = `if(HubOD >= 100mm; if(HubOD >= 200mm; 9; 7); 5)`

TIP: **Future Enhancement** In the future, I'll probably combine the parameters
for various types of fit with the new `if` function, and add a `PrintQuality`
that will allow setting the `PrintQuality` variable to then calculate the actual
fits.

## Default User Parameters

NOTE: **Global Parameters** Currently, Fusion360 doesn't have a concept
of global parameters that you can set for everything. This would be
awesome to have in this case, but not yet. [There are ways to fake
it](https://productdesignonline.com/how-to-create-and-use-global-parameters-in-fusion-360/),
but I find them overly complicated, and the CSV file with Parameters I/O
is a much simpler solution.  

One of the most powerful things with a parametric modeling tool is being
able to create standard parameters that drive the model. Often, a lot of
these are references to external parts that you need to interact with,
like a screw. To simplify _my life_, I have put together a CSV that
contains:

* [Fits for my printer](../mechanical/fit.md): interference,
  transitional, and clearance. 
* Standard metric screws for M2 - M12 in all the default standard
  threads. This is for _socket head screws_, which are my go-to. The
  insert and tap information will work for _any_ metric screw of that
  size and thread pitch (yay metric!). These are all just "standard"
  thread pitches. 
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
* `<size><fit>ClearanceHoleID` for the clearance holes as specified in
  Machinery's Handbook in their normal, close, and loose fits.

I've provided references to where the data came from originally (for
example, the [McMaster-Carr](https://www.mcmaster.com/) screw part
numbers). There's a few things you might need to do:

1. You should update the fits for _your printer_. This is just for my
   Prusa MINI+, and won't necessarily match yours. It's a good start if
   you don't want to fuss about it, although many cheap 3D printers have
   much bigger tolerances.
2. When you want to use `M3HeadOD` (for example), you'll want to allow
   for tolerance. I typically use `TransitionFit030`, which will get a
   snug fit that doesn't drag when you put the screw in. To do that,
   when you create the circle, just set the size to `M3HeadOD +
   TransitionFit030`. I didn't include the fit in the main size because
   different people want different fits in different situations.