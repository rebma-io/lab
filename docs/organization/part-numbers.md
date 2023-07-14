---
tags:
  - organization
  - part-number
  - pbs
---
# Part Numbers

## Why Part Numbers Matter

Parts are the thing that you want to keep track of. Inventory is your stock of
those parts. This matters when you get past just puttering around because
otherwise the entire process of knowing how much something costs to make, and
therefore what you need to charge, as well as whether you even have it, is
nearly impossible.

## Part Numbers are Not Inventory

TODO:

## My Numbering Scheme

I've landed on using the following part numbering scheme:

`$project.$component.$version`

This can be broken down thusly:

`$project` (regex: `\d{3}`) 
: The project represents some logical grouping of a set of parts. For example,
the microphone is a project. To collect lots of common parts, parts which can be
part of lots of different, the projects `000`-`099` are used to potentially hold
lots of common parts.

`$component` (regex: `\d{4}`)
: This can be either an assembly or a part. An assembly is composed of multiple
other parts or assemblies. The first digit tells you whether the thing is an
assembly or not. All assemblies start with a zero, where `1`-`9` is used for
individual parts.  

`$version` (regex: `\d{3}`)
: A sequential identifier of the version. This is only incremented when a
version is "approved" and used for a specific project in some way. Something
that hasn't even been designed yet can be designated `000`. 

This means the length of the part number is 3+1+4+1+3 = 12 characters. So, for
example, this is a part number: 

`103.0033.01`

It refers to revision `1` of assembly `33` on project `103`.

Note that this system does not account for different vendors. Realistically, if
the parts are interchangeable, then it shouldn't matter, and if they aren't,
then they aren't the same part anyway. 


## Background/Reference Information

Based on [this article on
Hackaday](https://hackaday.com/2020/12/02/a-case-for-project-part-numbers/),
here's some basic information:

* Shout-out to Donald Norman's The Design of Everyday Things. Need to re-read
  this book. Knowledge-in-hand (i.e. available at the moment of need) versus
  knowledge-in-the-world (i.e. things we just "know" from experience or
  expertise).
* Two major approaches:
  * Just a sequence of numbers (012324)
  * Something structured (07-BED-04-MKS-MRW)
* What meaningful information is worth encoding into the part number for others?
  * Version of the part
* Possible format:
  * Full: [_subassembly_]-[_part_id + params_]-[_revision_]-[_fab_process + material_]-[_who_made_it_]
  * Shortened: [part_id + params]-[revision]
  * Only need the shortened one on the part itself in most cases.
  * `041-CRS-02-M61-MRW` - Is the aluminum crossbar (CRS) from the alternate
    crossbar subassembly (41) in the design’s second revision (02) and machined
    (M) from 6061 aluminum, and manufactured by Mandala Rose Works (MRW). 
* [Here's what the author did with more
  details](https://jubilee3d.com/index.php?title=Part_Numbers).
* Print the part number on the side of the part as it's much more legible. 
* Every time I modify a part between GitHub Releases, I’ll update the part
  number. If I’m editing a part between a release, I just tick the number and
  re-export the STL in the preferred print orientation. The part number is
  stored as metadata in the model file, but if I get confused about what number
  I’m counting from, I can just lookup the STL from the last release. What that
  means is that STL files keep their names, but their contents change. This
  saves us from extra bookkeeping since part hyperlinks in places like the wiki
  don’t need to change every time the part number changes. This is also in-line
  with software practices. Every time we change a file, we don’t give it a new
  name. Version control software tracks the file’s history for us. And the same
  is true for design files that represent hardware if you track them with a tool
  like Git. Fun fact! GitHub will actually render a diff of two STL files from
  your commits if you dig for them.

Best practices ([Duro
Labs](https://www.durolabs.co/blog/part-numbering-systems-best-practices/)):

* Employ a semi-intelligent (structured) customer part number (CPN) scheme.
  Something like the first three elements of the full one above.
* Use numeric item identifiers. Less confusion.
* Keep part number length consistent. 
* Ensure item identifier numbers are unique and permanent.
* Avoid using special characters and leading zeros. Lots of software will strip
  leading numbers.
* Utilize category-based part numbering. This is basically the subassembly part.
* Use PLM for part numbering, not CAD.

Some more thoughts ([Grahamm
Foster](https://www.grahammfoster.com/the-best-part-numbering-scheme/)):

* `989/RQ/80370/001 rev A`
* BU/Group code. This is the "business unit" that is involved in this part.
* Data Type code
* Function code
* Variant code
* Version/Revision
