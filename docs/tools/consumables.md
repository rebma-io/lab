---
tags:
  - consumables
  - ipa
  - safety
---
# Consumables

One of the things that I don't think we talk enough about is all the
consumables that we use in a hobby project. While I've talked about
[solder](../electronics/soldering.md) elsewhere, there's a bunch of
others that you typically need to keep around. These are the ones I
continuously keep in stock, and my thoughts about why I chose what I
chose. I would also consider wire a consumable, but don't discuss it
here.


## Spoil Boards

There are many times when you need to cut, chop, or otherwise mangle
something and you don't want to be doing that on something expensive
like an ESD mat.  While there are dedicated cutting mats available, I've
found the best strategy is one stolen from the machining world: [spoil
boards](https://www.shopsabre.com/mdf-vs-ldf-which-spoilboard-is-better-for-cnc/).
These are sacrificial surfaces, so they're inexpensive. In my case, I
just have some 11x14" 1/4" MDF boards that I picked up in a pack of a
dozen for cheap. They are also sometimes called "chip boards". I'm still
on my first. Whenever I need to cut something, out it comes. It's often
the thing under other things... just in case.

## Distilled (or deionized) Water (H~2~O)

WARNING: **Safe Handling** While, yes, distilled (or deionized) water is
water, it is actually somewhat dangerous compared to regular tap water.
Because distillation removes all minerals from water, and water is one
of the most ideal solvents, there are some studies showing that drinking
distilled water can actually pull minerals and electrolytes out of your
body, which could be unhealthy. Just drink regular tap water if you're
in most parts of the world.

I'm going to treat these two as interchangeable, even though they are
produced through vastly different techniques and have slightly different
properties. For the hobbyist, this doesn't matter. The primary uses for
distilled water are:

* Cleaning things. Because water is an excellent solvent, it is a good
  starting point to clean components. 
* Wetting a solder sponge. Your soldering iron may have a sponge with it
  for cleaning the tip. Rather than using tap water, it's best to use
  distilled water as it is much less likely to add additional
  contaminants to the surface.

WARNING: **Not Everything is Watertight** Not every component is
watertight. In addition to things like sensors that may be open to
outside elements intentionally, there may be a small amount of ability
for water to [find a way](https://www.youtube.com/watch?v=ZScGEeNPTsQ)
into devices. 

## Isopropyl Alcohol (IPA)

> WARNING: **Safe Handling** Isopropyl alcohol (IPA) is a _reasonably_
> safe material to handle, but I would strongly recommend a few
> precautions. First, you should, if possible, obtain the MSDS for the
> product you purchase, but if not, you can use one [such as this from
> Sigma-Aldrich](https://www.sigmaaldrich.com/US/en/sds/ALDRICH/W292907).
> Reading this will give you a good understanding of what some of the
> risks and safe handling procedures are. 
>
> The general advice I would give is:
>
> 1. If you are going to directly handle IPA, meaning it will touch your
>    skin, wear [gloves](#gloves). I know this is a hassle, but it is
>    better safe than regretful in an ER in the future. You can use your
>    own judgement when this is triggered, but _for me_ I will wear
>    gloves if I'm not using a swab, or at least a wipe between me and
>    the IPA.
> 2. Never, ever, ever get IPA above its boiling point (typ. 82C, 180F)
>    unless you absolutely know what you're doing. IPA vapors can cause
>    severe respiratory distress and long-term damage. They also can
>    introduce the IPA into the bloodstream, which can lead to it
>    metabolizing into your body as acetone. You don't want that.
> 3. Store in a well-sealed container, and keep any you're not actively
>    using in a dark cool place for ensure long-term stability.

Also called isopropanol, and often just referred to as IPA, isopropyl
alcohol is a very inexpensive solvent that is used heavily in both
hobbyist and commercial electronics and mechanical works. While
typically available in a 60-90% concentration, you can easily obtain
99-99.9% concentration, which is what I recommend for use in this case.
Reducing the amount of water also reduces the possibility of
water-induced corrosion. Definitely, I wouldn't use anything below 90%
for electronics work.

For general use, I will admit to just buying the [Amazon Basics
99%](https://www.amazon.com/dp/B07NFSFBXQ/), which is "good enough".

So what do you use IPA for? A lot of things, but the main uses are:

* Cleaning solder flux off of PCB.
* Cleaning contacts.
* Removing adhesives.
* Removing Sharpie markings.
* Removing fingerprints from many surfaces (but not all).

One of the great things is that it evaporates quickly.

## Acetone

> WARNING: **Safe Handling** Like, IPA, acetone is [generally recognized
> as safe](https://en.wikipedia.org/wiki/Generally_recognized_as_safe)
> in very low quantities, but that means that, like IPA, you need to
> take similar steps to handle it. Acetone is a _highly flammable_ and
> volatile substance that can _ignite at room temperature_, so never use
> it near fire or anything that can create a spark. Also, ensure that
> acetone is stored in cool, well-ventilated areas away from direct
> sunlight and heat sources.
> 
> Always wear (latex!) gloves, and never let it get above its boiling
> point (typ. 56C, 133F) where it can be dangerous. But note, if you're
> going to have anything more than _very brief_ contact with acetone,
> you will need to invest in latex or butyl rubber gloves, as nitrile
> (my preference) will allow permeation after a few minutes.

Acetone is a solvent like IPA (it's also a precursor to producing
acrylic materials), and as such, it is useful for cleaning things. For
example, in chemical lab settings, it is often use as part of the
process of cleaning glassware to ensure it has minimal residue before
the final wash (note, it is _not_ the final wash).

In hobby use, there's a few places where it can be helpful:

* Acetone vapors can be used as part of a process to [smooth ABS and
  ASA](https://all3dp.com/2/abs-acetone-smoothing-3d-print-vapor-smoothing/)
  3D printed parts. This works with some other plastics as well, and you
  can use a small cotton swap to buff off a scratch by _literally_
  dissolving a bit of the plastic.
* Unstick acrylate glues, such as superglue. 
* 

DANGER: **Acetone and PCB** Never, ever, under any circumstance use
acetone on a PCB. It will strip the top coatings off; specifically, the
solder mask and silkscreen.

NOTE: **Fingernail Polish Remover** Fingernail polish remover typically
contains acetone, but also has many other components such as [dimethyl
glutarate](https://pubchem.ncbi.nlm.nih.gov/compound/Dimethyl-glutarate),
[dimethyl
adipate](https://pubchem.ncbi.nlm.nih.gov/compound/Dimethyl-adipate),
[dimethyl succinate](https://pubchem.ncbi.nlm.nih.gov/compound/7820),
and [propylene
carbonate](https://pubchem.ncbi.nlm.nih.gov/compound/7924). This makes
them not interchangeable with pure acetone. 

## Anti-static Cleaning Spray

One thing to be aware of, though, is when you're cleaning an
electrostatic workbench mat, is that IPA can reduce the efficacy of the
mat at dealing with ESD. To avoid degrading something that's not
particularly cheap, I use a specific cleaner for anything where "static
control" is an issue (this includes my wooden workbench top as well,
although it's unclear if that does anything useful other than waste more
expensive consumables): [ACL Staticide Mat & Table Top
Cleaner](https://www.aclstaticide.com/products/mat-table-top-cleaner). 

To use it, you spray the surface with the Staticide, and then _allow it
to sit 2-3 minutes_, and then wipe off (with a [lint-free
wipe](#lint-free-wipes) preferably). Doing this will ensure you maintain
the ESD protection of the mat over time.

## Paper Towels

I do keep a roll of paper towls (specifically [Viva "signature
cloth"](https://www2.v1.vivatowels.com/en-us/products/viva-signature-cloth-paper-towels))
around for general cleaning purposes, wiping down a bench, etc. It's
worth keeping them close at hand, and so I have them mounted under the
desk to the drawer module.

TIP: **Possible Reusable Replacement** Adam Savage is a [big
fan](https://www.youtube.com/watch?v=roXwRxFTfCI) of [these huck
(surgical)
towels](https://mimaatex.com/collections/huck-towels/products/huck-towels-blue-commercial-50-piece-pack-16x-24-new-100-cotton-super-absorbent-lint-free-free-shipping)
in his shop. I've ordered some and will update once I've had a chance to
use them for a while. 

## Lint-Free Wipes

You'll need to wipe things _a lot_ when working with electronics and 3D
printing, so it's good to keep a heavy stock of lint-free wipes. You
want [non-woven](https://en.wikipedia.org/wiki/Nonwoven_fabric) wipes in
a blend of polyester and cellulose. Personally, I keep a stock of [4x4"
AAWipes](https://www.aawipes.com/products/aawipes-bag-of-600-pcs-4-x-4-cleanroom-wipes-delicate-task-wipers),
which are common in cleanroom applications. You can buy smaller volumes
on their [Amazon store](https://www.amazon.com/gp/product/B07YF88GJH/).
Sadly, they are typically single-use, although I have been known to
reuse one if I've just used it to wipe a reasonably clean surface with
IPA and need to do it again.

WARNING: **Disinfecting Wipes** Don't confuse these for disinfecting
wipes like what you would use in the kitchen.  Those have chemicals in
them that can damage sensitive electronics and often will leave a
residue behind.

## Low Lint Swabs

Often, you'll need to get into the crevices of something, or between
leads on an IC, to clean them, and to do that using a [low lint cotton
swab](https://www.mcmaster.com/products/low-lint-swabs/). The relative
of the random cotton swab at your local pharmacy, they're a tiny bit
more expensive, but have wooden handles, and cotton woven in a way that
leaves a minimal amount of lint behind.

They're also available in an ESD-safe version, but it's about 10-15x
more expensive, and while I _know_ I should probably use them, I'm
simply too cheap to buy them. The ESD-safe ones use a plastic handle and
a polyurethane foam tip. If you're wanting to splurge, please do.

## Gloves

WARNING: **Not All Gloves Are the Same** Not all gloves are good for
every use case. While I discuss primarily nitrile gloves here, they are
_not appropriate_ for a few use cases. Please review [this guide to the
chemical resistance of
gloves](https://amo-csd.lbl.gov/downloads/Chemical%20Resistance%20of%20Gloves.pdf)
for concrete scientific recommendations.

Gloves are disposable, much to the surprise of many people. They are
also relatively inexpensive.  While there are a few materials on the
market, I am a big fan of
[nitrile](https://en.wikipedia.org/wiki/Nitrile) gloves as they
(typically) will not trigger latex allergies, which are more present
than you'd imagine, and no reason to tempt fate. In addition, I would
use something that is _at least_ 5 mils (0.005") thick (typically
measured at the palm). Personally, I like them in purple, but they come
in a bunch of different colors. 

The gloves I use are from
[Kimberly-Clark](https://www.kcprofessional.com/en-us/products/scientific-and-research/lab-environment/hand-protection-and-gloves/kimberly-clark-nitrile-gloves/55090)

If you're just touching things with your fingertips, you can also
consider using [finger cots](https://en.wikipedia.org/wiki/Finger_cot),
which cover just the last joint of your fingers in most cases. They also
come in nitrile, and are pretty common in the electronics industry.
Personally, they drive me crazy, and I'd rather go through the time of
putting on one or two gloves.

## Third-Party Resources

* [More about isopropyl
  acohol](https://www.ifixit.com/News/36877/ask-ifixit-everything-you-wanted-to-know-about-isopropyl-alcohol) 