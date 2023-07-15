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


In addition, I always create the following three parameters to allow for easily
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