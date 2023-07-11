# Simulating Circuits

There are a lot of different tools that can do simulation
([LTSpice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
being perhaps the most famous), but as I was working on drawing all
these schematics for explaining electronics here in Fusion360, I ran
across an amazing tool written by Paul Falstad. I'm not sure he has a
_formal_ name for it, but we'll call it
[circuitjs](http://www.falstad.com/circuit/). This allows for very
accurate simulation of a circuit with observability. There are other
tools, like [CircuitLab](https://www.circuitlab.com/), which are also
quite useful.

NOTE: **Source of Models** Rather than redraw a lot of things, I have
adopted the existing models that are contained in the circuitjs library
wherever possible, sometimes making small adjustments. All credit for
those really belongs with Paul and his associated contributors. 

## Understanding and Interacting

I'm not going to go into all the schematic symbols, as those are covered
elsewhere, but a few things to keep in mind when looking at them:

* _Green_ indicates a positive voltage potential across the section in
  that color.
* _Red_ indicates negative voltage potential across the section.
* _Gray_ indicates ground, earth, or just zero potential.
* _Yellow dots_ indicate the movement of current, in the [conventional direction](non-intuitive-topics.md#conventional-current-flow-v-reality).

Along the bottom are scopes showing the measurement of various
characteristics in the circuit. Hovering over the lines will get you
specific details at that exact point in time. 

You can interact with the circuit! You can press the "RUN/Stop" button
to start and stop the circuit. The "Reset" will return it back to where
it started from all your modifications. Finally, there are sliders on
the right hand side that control not just the speed of simulation and
the speed at which the current is visualized, but often other sliders to
control parts of the circuit.

You can click on a switch to turn it on or off. If you hover over a
component, you'll get some more information on the component and the
current state will be shown in the bottom right corner. You can also
_modify_ components. If you double click (left click on them), you can
edit them and modify their characteristics. 

Once again, amazing thanks to Paul for this amazing tool, along with
[Iain Sharp](http://lushprojects.com/circuitjs/) who made the original
Javascript port. 

## Accuracy of Simulation

WARNING: **Don't Bet Your Money on It** Simulations are just
approximations of reality, not reality. We are depending a lot on the
idea of an ideal component, which is not the reality.

I'm just going to quote [Iain](http://lushprojects.com/circuitjs/) here:

> Physics simulations are not real life, and don't assume that
> simulation and reality are identical! This simulation idealizes many
> components. Wires and component leads have no resistance. Voltage
> sources are ideal - they will try and supply infinite current if you
> let them. Capacitors and inductors are 100% efficient. Logic gate
> inputs draw zero current - not too bad as an approximation for CMOS
> logic, but not typical of 1980s TTL for example. By all means use this
> simulator to help visualize circuits, but always test in reality.
> 
> Sorry to break it to you folks, but the simulator numerically
> approximates models of components that are also approximate. Even
> without allowing for any bugs it is just a rough guide to reality.
> This simulator may be helpful for visualization, but used the wrong
> way any simulator can give a false sense of security. Some people
> don't really grasp this important concept - I've even had one user
> accuse the simulator of "lying" because he (or she) didn't take
> account of the component idealizations and didn't understand the
> actual performance of the components they chose to use. It's a key
> leaning for all electronic engineers that they must always be fully
> aware of real-world component (and system) characteristics and how
> these differ from any particular simulator they use. If you want more
> precise models of real-world components then the SPICE-based
> simulators are much more appropriate tools than this one, but even
> then, you should be aware of deviations from reality. As the great
> analogue circuit designer Bob Pease said "When a computer tries to
> simulate an analog circuit, sometimes it does a good job; but when it
> doesn't, things get very sticky".
> 
> One consequence of the use of ideal components is that the simulator
> doesn't converge on a result for circuits that have no defined
> behaviour - for example an ideal voltage source short-circuited by an
> ideal wire. Another situation that can't be simulated under these
> assumptions is the current distribution between the conductors if two
> perfect conductors are connected in parallel. When using the simulator
> you must account for places where real electronics differs from the
> ideal.