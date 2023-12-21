---
tags:
  - pcb
  - solder
---

# Layers & Stackup

NOTE: **Scope** This discussion is primarily focused on what a hobbyist is
likely to run into. There is a _vast spectrum_ of PCB-related technology that
is leveraged by specialized applications. Perhaps in the future I will discuss
those.

While there are other ways to connect various electronic components, the
printed circuit board (PCB) is the backbone of the industry. It allows for
very complex designs with repeatable and predictable outcomes. In this
section, I'm going to discuss the 4 key layers in a PCB. Each of these layers
can appear more than once, and we will discuss "stackup", or the organization
of those layers, at the end.

## Layers

There are 5 major types of layers in a PCB: the substrate, copper/conductive,
surface finish, solder mask, and finally the silkscreen. We will take each of
these in turn.

### Substrate and Dialectric

The substrate is the mechanical foundation that the entire PCB uses. It
provides structural integrity, mechanical strength, electrical performance (
specifically the dialectric constant), and thermal management for the rest of
the layers. It's the "skeleton" of the PCB.

| Material   | Description                                                                                                                                                       | Properties                                                                                                  | Application                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| FR-4       | The most common form, and one composed of layers of woven fiberglass impregnated with an epoxy resin.                                                             | Good trade off of mechanical strength, high electrical insulation, and price.                               | General purpose, and what you'll find in 95% of situations.                                          |                                          
| Rogers     | A specific brand of material (typically PTFE-based) that is designed for high-frequency (RF) applications, and which can be had in multiple dialectric constants. | RF-focused with low-loss and controlled impedence                                                           | RF, microwave, antennas, telecommunications                                                          |
| Metal core | Aluminum or copper is the core layer, but it is coated with a dialectric to provide insulating properties.                                                        | Excellent thermal conductivity, which allows for good heat dissipation.                                     | High-power applications, and especially seen recently in LED lighting as the heat-sink to the module |
| Ceramic    | Typically made from alumina (Al~2~O~3~) and sometimes aluminum nitride (AiN).                                                                                     | Exceptional thermal conductivity and insulation properties. Dimensionally stable at very high temperatures. | High-power and high-frequency applications, often with extreme operating conditions.                 |
| Polyimide  | A flexible material that's typically used for flexible PCBs. This is the same material that is marketed as Kapton tape.                                           | Good flexibility and thermal stability.                                                                     | Anywhere flexibility is critical, and commonly used as a form of interconnect.                       |

#### FR-4

Since FR-4 is by far the most common one, especially in hobbyist work, it's
worth diving into the FR world and specifically one characteristic of
FR-4 that varies and can often help improve the quality of your result: glass
transition temperature (T~G~ or just TG). FR-4 isn't a specific meterial, but
instead is a standard defined by NEMA under LI-1-1998 which covers a set of
properties that it must generate, epsecially around fire retardance. [Glass
transition](https://en.wikipedia.org/wiki/Glass_transition) is the
_reversible_ process that basically softens hard amorphous materials, like
fiberglass. Basically, the higher the T~G~, the more resilient the material is
to heat, either during production (think wave soldering for example) and
during operation. FR-4 comes in a few ranges:

* Low: 130-140C (default)
* Medium: 150-160C
* High: 170-180C

For example, if a PCB rated to TG130 is heated beyond 130C, it will lose its
solid form. This not only impacts the mechanical strength of the board, but it
also deteriorates the electrical properties.

As a hobbyist, typically the regular FR-4 is completely acceptable, but it's
worth having in the back of your pocket if you need something better.

#### Rogers

You're 100% OK using FR-4, until you're not. The biggest contributor to
needing to move to Rogers is the frequency of the signals you're working with.
Once you get above a few hundred megahertz, and definitely above 1GHz, you'll
need to be thinking about whether FR-4 can support the operating and
dialectric needs of your design.

#### Dielectric What?

While the term "dielectric constant" is still in heavy use in the electronics
world, the "official" term is actually _relative permittivity_. But still,
what does that mean?

A dielectric is an insulating material and the dielectric constant measures
the storage of electrical energy within an electrical field in the material.
It is a fundamental concept to capacitance in either capacitors or just
general circuit design. High relative permittivity will reduce the magnitude
of a field within the material. Conversely, low relative permittivity will
increase the field, all other things being equal.

The dielectric constant (D~k~) profoundly impacts frequency performance,
miniaturization capability, and achievable impedance values. Materials with a
lower D~k~ permit higher operating frequencies, greater impedance control, and
more minor features. This comes at the expense of requiring larger trace
widths. A higher Dk materials allow increased density and smaller components
but with limitations in frequency range and impedance control.

### Conductive (Copper)

### Surface Finish
Combination finishes, typically involving mixing "hard gold" with something else.

#### Hot Air Solder Level (HASL)
#### Organic Solderability Preservatives (OSP)

#### Hard Gold
#### Electroless Nickel Immersion Gold (ENIG)
#### Electroless Nickel Electroless Palladioum Immersion Gold (ENEPIG)
#### Immersion Tin
#### Immersion Silver

### Solder Mask

Also called a solder resist, the solder mask is a thin layer of polymers on a
PCB. It serves numerous purposes throughout the lifecycle of the PCB:

* Insulation from soldering process. Solder will not, typically, stick to
  solder mask. This means that when you're in the process of assembling a PCB,
  whether by hand or automation, the solder mask will ensure that the solder
  stays within the "lines" of the PCB, and doesn't spread out where it's not
  wanted. It's also critical to techniques like drag soldering.
* Strengthens pads. The additional polymer material reinforces the pads on the
  board's surface, and this helps reduce the likelihood of separation.
* Protect from corrosion and oxidation. Copper is a great conductor, but it
  also reacts quite strongly to both moister and oxygen, causing it to lose
  electrons and change properties. Solder mask provides a defense against both
  these things.
* Improve break-down voltage of dielectric material. Breakdown voltage is the
  _maximum_ voltage that a PCB can withstand before bad things happen. Because
  the polymer a resist is made from is also a dialectric material, using it
  increases the breakdown voltage.

Solder mask is applied using one of three methods:

1. Liquid photoimageable solder masks. In this case a two-part epoxy is mixed
   at the last second and either sprayed or coated using a curtain[^1], then a
   mask is created, and UV is used to expose and harden the epoxy.
2. Dry film photoimageable solder masks. This is used when the board has been
   laminated in a vacuum. It uses a film technique similar to the overall PCB
   etching process, and can provide a very fine resolution. For this reason,
   it's often seen in high-density interconnect (HDI) boards.
3. Liquid epoxy solder masks. This is by far the most cost-effective way to
   apply at production scale. it uses a standard silkscreen technique to apply
   the polymer, wich is then termally cured.

Solder mask is available in a wide range of colors, and can even be provided in custom colors if you're a large enough customer. While green is by far the most common historically, you can find it in:

* Red
* Yellow
* White
* Black
* Purple
* Blue
* Clear

Manufacturers may charge extra for anything except green.

### Silkscreen


Markings: Reference designators, part outlines/smybols, polarity marking, probe/test points, pin numbers, switch settings, board information (name, number, revision), manufacturer information, legal information including certifications.
Colors: White, black, yellow.

## Stackup

[^1]: A curtain is basically a waterfall of the liquid that a board passes
under. Often there is a second flow underneath the board to provide bottom
coating if being done in a single step.