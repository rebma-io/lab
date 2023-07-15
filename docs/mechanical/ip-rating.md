---
tags:
  - enclosures
  - nema
  - ratings
  - standards
  - water
---
# IP and NEMA Ratings

## IP Ratings 

IP rating codes are an international standard defined in IEC 60529. The
code contains the IP prefix followed by two numbers. The first number
describes resistance to ingress of solids such as dust or other small
particles, while the second number expresses protection against liquids.
For example:

* IP**6**7 = Solids Rating (First Number)
* IP6**7** = Liquids Rating (Second Number)

Additionally, there is an optional letter appended to the end (see
below).

IEC has a [nice diagram on their site](https://www.iec.ch/ip-ratings)
explaining all the pieces. 

### Protection Level Definition

| Level | Solids Rating                                                                                                                                          | Liquids Rating                                                                                                                                                       |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0/X   | Not rated for protection against contact or ingress (or no rating supplied).                                                                           | Not rated (or no rating supplied) for protection against ingress of this type.                                                                                       |
| 1     | Protection against solid objects larger than 50 mm (e.g. accidental contact with any large surface of the body, but not deliberate body contact).      | Protection against vertically dripping water. No harmful effects when the item is upright.                                                                           |
| 2     | Protection against solid objects larger than 12 mm (e.g. accidental finger contact).                                                                   | Protection against vertically dripping water. No harmful effects when tilted up to 15° from normal position.                                                         |
| 3     | Protection against solid objects larger than 2.5 mm (e.g. tools).                                                                                      | Protection against water sprayed directly at any angle up to 60° off vertical.                                                                                       |                                                                                                                                                                      
| 4     | Protection against solid objects larger than 1 mm (e.g. small objects such as nails, screws, insects).                                                 | Protection against splashing water from any direction. No harmful effects when tested for at least 10 minutes with an oscillating spray (limited ingress permitted). |
| 5     | Dust protected: partial protection against dust and other particulates (permitted ingress will not compromise the performance of internal components). | Protection against low-pressure jets. No harmful effects when water projected in jets from 6.3 mm nozzle, from any direction.                                        |
| 6     | Dust tight: full protection against dust and other particulates.                                                                                       | Protection against powerful water jets. No harmful effects when water projected in jets from 12.5 mm nozzle, from any direction.                                     |
| 7     | N/A                                                                                                                                                    | Protection against full immersion at up to 1 meter depth for up to 30 minutes. Limited ingress permitted with no harmful effects.                                    |
| 8     | N/A                                                                                                                                                    | Protection against immersion beyond 1 meter. Equipment is suitable for continuous immersion in water. The manufacturer may specify conditions.                       |

Finally, there is a potential suoplementary level to provide extended
protection information:

| Letter | Meaning                      |
| ------ | ---------------------------- |
| F      | Oil resistant                |
| H      | High voltage apparatus       |
| M      | Motion during water test     |
| S      | Stationary during water test |
| W      | Weather conditions           |

You can find more details about the testing methodology [on
Wikipedia](https://en.wikipedia.org/wiki/IP_code), unless you want to
pay for the specification yourself.

NOTE: **Further Levels** I believe there is work on higher ratings
"above" those currently in place, but I don't know anything about them.
If you need something above IP67, good luck! 

### Common Ratings

The most common ratings I've seen are:

* IP54. This means some dust will get in, but it shouldn't be enough to
  damage anything. Also, splashes of water should be "OK".
* IP56. Same as IP54, but it can sustain some high-pressure water
  directed at it.
* IP65. This is dustproof, but still can't deal with high-pressure
  water, or being submerged. 
* IP67. This can be submerged in water for an extended period of time.


## NEMA Ratings

NEMA has ratings for enclosures, in parallel to the IP ratings (and
predating them, I believe, by quite some time). The NEMA definition
interacts with National Fire Protection Code (NFPA) and National
Electrical Code (NEC) and includes references to them.

### NEMA Types

| Type        | Approximate Definition                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1           | General-purpose. Protects against dust, light, and indirect splashing but is not dust-tight; primarily prevents contact with live parts; used indoors and under normal atmospheric conditions.                                                                                                                                                                                                                           |
| 2           | Drip-tight. Similar to Type 1 but with addition of drip shields; used where condensation may be severe (as in cooling and laundry rooms).                                                                                                                                                                                                                                                                                |
| 3* (varied) | Weather-resistant. Protects against falling dirt and windblown dust, against weather hazards such as rain, sleet and snow, and is undamaged by the formation of ice. Used outdoors on ship docks, in construction work, and in tunnels and subways. R suffix but omits protection against windblown dust. S suffix also operable when laden with ice. X suffix means additional corrosion protection against salt water. |
| 4 and 4X    | Watertight. Must exclude at least 65 GPM of water from a 1 in nozzle delivered from a distance not less than 10 ft for 5 min. Used outdoors on ship docks, in dairies, in wastewater treatment plants and breweries. X suffix indicates additional corrosion resistance.                                                                                                                                                 |
| 5           | Dust-tight. Provided with gaskets or equivalent to exclude dust; used in steel mills and cement plants.                                                                                                                                                                                                                                                                                                                  |
| 6 and 6P    | Submersible. Design depends on specified conditions of pressure and time; submersible in water or oil; used in quarries, mines, and manholes.                                                                                                                                                                                                                                                                            |
| 7           | Certified and labelled for use in areas with specific hazardous conditions: for indoor use in Class I, Groups A, B, C, and D environments as defined in NFPA standards such as the NEC.                                                                                                                                                                                                                                  |
| 8           | Certified and labeled for use in areas with specific hazardous conditions: for indoor and outdoor use in locations classified as Class I, Groups A, B, C, and D as defined in NFPA standards such as the NFPA 70.                                                                                                                                                                                                        |
| 9           | Certified and labelled for use in areas with specific hazardous conditions: for indoor and outdoor use in locations classified as Class II, Groups E, F, or G as defined in NFPA standards such as the NEC.                                                                                                                                                                                                              |
| 10          | MSHA. Meets the requirements of the Mine Safety and Health Administration, 30 CFR Part 18 (1978).                                                                                                                                                                                                                                                                                                                        |
| 11          | General-purpose. Protects against the corrosive effects of liquids and gases. Meets drip and corrosion-resistance tests.                                                                                                                                                                                                                                                                                                 |
| 12 and 12K  | General-purpose. Intended for indoor use, provides some protection against dust, falling dirt, and dripping non-corrosive liquids. Meets drip, dust, and rust resistance tests.                                                                                                                                                                                                                                          |
| 13          | General-purpose. Primarily used to provide protection against dust, spraying of water and non-corrosive coolants. Meets oil exclusion and rust resistance design tests.                                                                                                                                                                                                                        
You can find a more in-depth dive into the ratings either
[here](https://engineerfix.com/electrical/electrical-ratings/a-complete-guide-to-nema-ratings/)
or from NEMA directly with [NEMA
250](https://www.nema.org/standards/view/nema-250-enclosure-types),
which is, shockingly for a standard, free.

### Common Ratings

My personal experience is that while NEMA ratings _used_ to be very
common, most people have switched over to IP for most things. Still, if
you're looking for watertight enclosures, the 4 and 4X series are still
referenced a good bit. Otherwise, the main place I've seen NEMA types
referenced is in electrical (as opposed to electronic) enclosures.

## Comparing IP and NEMA

While there are a lot of little details, the approximate comparison
between IP and NEMA is:

| NEMA           | IP code          |
| -------------- | ---------------- |
| 1              | IP20             |
| 2              | IP22             |
| 3, 3X, 3S, 3SX | IP55             |
| 3R, 3RX        | IP24             |
| 4, 4X          | IP44, IP66, IP65 |
| 5              | IP53             |
| 6              | IP67             |
| 6P             | IP68             |
| 12, 12K, 13    | IP54             |