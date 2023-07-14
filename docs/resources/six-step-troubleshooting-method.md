# Six Step Troubleshooting Method

Years ago, at a start-up, I worked with several people who had come up
through the US Navy, and adhered to a troubleshooting method that I
thought was so radically different than anything I had been taught that
I quickly adopted it. This is it. I've tried to remember what all they
told me, since, no matter how hard I tried, I couldn't find any
official Navy document for this. It just seems to be part of the
internal training.

> NOTE: **What's the Point of Troubleshooting?** Troubleshooting, is, at
> its heart, a process of problem solving. The problem you're trying to
> solve is very simple: a fault in a system. Your goal is to fix it.
> But, what does it mean to "fix a fault"? Yes, we want to fix the
> fault, but we also want to do it efficiently and with the least amount
> of frustration. We also want to do this in a repeatable way that is
> explainable to others as much as is feasible.
>
> This process applies to almost everything, really. It is great for
> identifying problems in a circuit, but it's also great when debugging
> software, or solving a recipe conundrum in the kitchen.

## Step 1: Symptom Recognition

Everything begins with the recognition that "something isn't right".
This might come from a device not turning on, or it might be something
more interesting, like the [magic
smoke](https://en.wikipedia.org/wiki/Magic_smoke) coming out of a
component. Something isn't right; something isn't working; something
isn't behaving the way you expect. This is where it all begins: paying
attention to the behavior of things and whether it is what you expect
(note, your expectations may not always be correct, but that's just a
different kind of fault.)

## Step 2: Symptom Elaboration

So, something is wrong. But, what exactly is it that is wrong? This is
where you start asking questions of yourself, or if it involves someone
else, the person who reported the problem. Some questions you might ask:

1. What is not working?
2. How is it not working?
3. Is it just this circuit/you? 
4. Has this happened elsewhere/to others?
5. Has it ever worked?
6. Has anything changed recently? 
7. Have I changed anything recently?

Numbers 1 and 2 above are something that's difficult to explain, but
it's basically the idea that often, people just say things like "it's
not working" or "it's broke", but that's not a very helpful when we are
trying to diagnose and troubleshoot a problem. Instead, we should be
asking questions around how is it not working? Is a light not coming on
that should? Is voltage not somewhere it should be? Is voltage somewhere
it _definitely_ shouldn't be? Poking at this early on will help avoid
some [wild good
chases](https://www.merriam-webster.com/dictionary/wild-goose%20chasehttps://www.merriam-webster.com/dictionary/wild-goose%20chase). 

While doing this, use all the senses you have. Does something _smell_
weird? A lot of dielectric compounds make very acrid smells when they
fail. Did I hear a pop? That's probably not great. Look around and see
what else might have changed.

## Step 3: List probable Faulty Functions

> "When you have eliminated all which is impossible, then whatever
> remains, however improbable, must be the truth." <br>― Arthur Conan
> Doyle, The Case-Book of Sherlock Holmes 

Now that you've figured out how this fault exhibits itself, it's time to
think about what could possibly be causing it. A function is a macro
component of something. For an electronics project, this might be some
subsection of the circuit, or a module. For software, a module or class,
or even function. This is where we have to be creative and brainstorm. 

We are not trying, _at this point_ to figure out exactly what went
wrong. Instead, we just want to figure out approximately where that
problem is likely to be. Part of this is also identifying what is not
part, or at least unlikely to be part, of the problem. Sometimes,
elimination is actually the more expeditious strategy. Reframe the fault
as what it can't be: it can't be the power system, because I measure the
proper voltages as the proper places.

## Step 4: Localize the Faulty Function

One way to localize the faulty function, is to take an approach of
bisecting the problem area. Take something in the middle of the circuit
(approximately), or in the middle of your software, and figure out if
the problem is before or after that point. Before? Great, cut the part
before that in half and repeat. Keep repeating until you've reached a
small enough section that it's easy to reason about what could possibly
go wrong.

We now know the approximate location of the fault, and more importantly,
we know where it's unlikely to be. 

To do this localization, we can pull out the multimeter and oscilloscope
and see what's behaving how. Are capacitors exhibiting the right
capacitance and ESR? Do discreet transistors and diodes exhibit the
right directional flow of current? It can often be helpful to pull out
something to measure temperature (an IR camera is amazing for this) to
see if something is especially hot; high resistance or a short-induced
high current flow, can show up as a _lot_ of heat.

When dealing with software, tracing and logging can be super helpful to
just figure out where things "stop". Where did it end? What was the last
thing that worked? It's also super helpful to dig out a debugger if you
can. This is a bit harder with embedded systems, but worth learning none
the less. 

## Step 5: Localize the Faulty Component

Let's say we now know that the problem is with a specific chip in the
circuit. Now what? Well, now we need to figure out what is causing this
fault. Some things to dig into closely in figuring this out are:

1. Is ground correct? Make sure. Twice.
2. Is power being delivered to the right pins in the right voltages?
3. Are there any solder joint issues? Looking closely with either a
   loupe or microscope will help you identify a bad solder joint, or
   even a short between two pins.
4. Is the chip operating outside its normal operating temperature? Even
   just using your finger to feel if it's hot is a start, though more
   accurate means are helpful.

If those don't get you anywhere, you might want to start looking into
the actual signals going into the chip. For that, something [like a logic
analyzer](http://www.qdkingst.com/en/products) can be super helpful.
[Tiny mini/micro-grabbers are
great](https://www.pomonaelectronics.com/products/test-clips/grabber-test-clips)
for this, or needle points to attach to either a DMM or oscilloscope. 

## Step 6: Failure Analysis

Now that we've figured out what's actually causing the fault, we need to
fix it. But fixing it isn't the last step! Oh no... we have two more
steps. First, we need to _verify_ that our fix actually worked. Then, we
need to _document the fault_ in some fashion so that we (or someone
else) can find it if something similar happens in the future. We want
this to answer a few core questions:

1. What was at fault?
2. How was that fault exhibiting symptoms?
3. What caused the fault?
4. How can we prevent this or similar faults in the future?

This is closely linked to the idea of "the five why's", which is also
commonly used. This is where you recursively explore why something
happened, and do it 5 times. The example from
[Wikipedia](https://en.wikipedia.org/wiki/Five_whys) is illustrative:

> The car is not running
>
> 1. _Why?_ The battery is dead.
> 2. _Why?_ The alternator is not functioning.
> 3. _Why?_ The alternator belt has broken.
> 4. _Why?_ The alternator belt was well beyond its useful service life
>    and had not been replaced.
> 5. _Why?_ The vehicle was not maintained according to the recommended
>    service schedule. 

While this is all related to [root cause
analysis](https://en.wikipedia.org/wiki/Root_cause_analysis), I am of
the opinion that there is rarely _a_ root cause. Instead there are
multiple contributory causes, and it's important not to focus on _the_
cause, but what contributed to the failure.

This information should be part of your
[note-taking](../organization/note-taking.md) process. If your project
hosted somewhere like Github, it's not a bad idea to open an issue for
it and document the findings there, even if it's just you involved in
the issue.