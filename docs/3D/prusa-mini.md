# Prusa MINI+

Currently, I have a [Prusa
MINI+](https://www.prusa3d.com/category/original-prusa-mini/). 

## Maker's Muse high-speed settings

I use the following settings taken from [Maker's
Muse](https://www.makersmuse.com)'s recommendations. These are all for
[PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/). I find that they
generate a pretty reasonable draft product _much_ faster than the default Prusa
settings, which are quite conservative for obvious reasons. All speeds are in
mm/s.

| Setting                    | Normal | High-Speed     |
| -------------------------- | ------ | -------------- |
| Layers/Bottom solid layers | 4      | 3              |
| Layers/Top solid layers    | 6      | 3              |
| Layers/Layer height        | 0.20   | 0.30           |
| Speed/Bridges              | 25     | 60             |
| Speed/External perimeters  | 40     | 70             |
| Speed/Gap fill             | 40     | 80             |
| Speed/Infill               | 140    | 250            |
| Speed/Perimeters           | 50     | 100            |
| Speed/Small Perimeters     | 25     | 50             |
| Speed/Solid Infill         | 140    | 250            |
| Speed/Support Material     | 40     | 100            |
| Speed/Top Solid Infill     | 40     | 100            |
| Infill/Fill Density        | 20%    | 10%            |
| Infill/Fill Pattern        | Grid   | Adaptive Cubic |

## Engineering Fit

Using some test prints, I was able to determine the following types of fits that
work for me, at least with Jessie PLA. Fit is a specific mechanical relationship
between (typically) a shaft and a hole. See [my discussion of
fit](../mechanical/fit.md) elsewhere for more details.

| Print Profile     | Interference | Transition | Clearance |
| ----------------- | ------------ | ---------- | --------- |
| 0.15 Quality      | 0.133 mm     | 0.135      | 0.175     |
| 0.30 Maker's Muse | 0.135 mm     | 0.155      | 0.175     |

I use these in Fusion360 to help parameterize the models.
