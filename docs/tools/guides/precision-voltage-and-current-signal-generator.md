---
tags:
  - curernt
  - voltage
  - source
---
# Precision Current and Voltage Signal Generator

![Precision voltage reference. A box with a blue front, 1 knob, and 1
button](img/zyx-hod-2ao-vi.jpg){: width=200 align=right }

A while back, I picked up [this voltage and current
reference](https://www.aliexpress.us/item/3256805285277753.html) from
AliExpress. It has a product number, I think of ZYX-HOD-2AO-VI, but who
knows? I can't remember which person had mentioned it to me, but
they thought it had *excellent* characteristics, and behavior far in
excess of what you might expect for a sub 
[[ usd(15.0, as_of="21 August 2023") ]] 
device. It's also quite compact at 3.9" (100mm) by 2.36" (60mm) by 1"
(25mm). 

One thing it didn't have, though, was a good manual, so I've pulled this
together from both it's kinda "manual", some digging, probing, and
general beating my head against the wall.

Let's start with the specs:

| Attribute     | Range   | Tolerance |
| ------------- | ------- | --------- |
| Voltage range | 0-10VDC | 0.01V     |
| Current rage  | 0.22mA  | 0.01mA    |

The one I bought has a built-in 3.6V LiIon battery that can be charged
over a micro-USB connector. The screw terminal lock is also removable,
something they don't typically mention. This means you can potentially
swap them quickly for various setups. 

## Inside the Box

![Complicated PCB](img/precision-internal-pcb.jpg)

As I mentioned above, this device is far more complicated than anything
at this price point has a right to be. If you pop the front cover off
after removing the rotary knob, you peer inside, and find this.

That's a _lot_ for what this does. Unfortunately, they've scrubbed all
the ICs of any marks. There's one inside that has the faint residual
marking of "ZYX", but that's useless.  There's a few seemingly
high-quality polyester caps as well (marked 334J100 on top). Still,
impressive for the price, and explains the rather outstanding
performance.

We truly live in a bizarre, and in many ways golden, era of electronics.

## Power Options

There are three ways to power the one I have:

1. External 15-30VDC power supply, which it will never draw more than 1W
   operating, and 5W charging.
2. External micro-USB at 5V and 0.2A operating and 1A charging.
3. Internal 3.7V battery.

Obviously, you can only use one of these at a time.

## Output Modes

There are two output modes, current and voltage, which you can think of
a constant-current and constant-voltage sources. You can switch between
them using the MODE button. 

## Terminal Block

On the top of the device, there is a (removable) screw terminal bock. It
has 6 connections, which are numbered left to right 1-6:

| Terminal | Label | Use                                                                                               |
| -------- | ----- | ------------------------------------------------------------------------------------------------- |
| 1        | GND   | Ground for either signal output or external 24VDC power supply                                    |
| 2        | 24V   | 24VDC positive connection for external power supply                                               |
| 3        | AI+   | Not sure of this one, it discusses a two-wire acquisition device, but this isn't a 4-wire device. |
| 4        | AIo   | Constant current output                                                                           |
| 5        | AVo   | Constant voltage output                                                                           |
| 6        | GND   | Ground for either signal output or external 24VDC power supply                                    |

## Changing Parameters

Getting to the parameters setting is a bit weird. First, there are
settings for each mode (voltage v current), so you will need to make
sure you're in the right mode before starting. To get access:

1. Press and hold down the control knob for 2 seconds. This will display
   `F001`, which is a reference to parameter 001.
2. Rotate the knob clockwise to select `F002`. The first time you do
   this, you will get a display consisting of 4 underlines: `_ _ _ _`.
   This means that the device wants a passcode.
3. To enter the password you rotate the knob clockwise for a `|-`
   symbol or counterclockwise for a `-`. To get to parameters F002-F009,
   you use the passcode `|-  -  -  |-`. That's clockwise,
   counter-clockwise, counter-clockwise, clockwise. Then press down on
   the rotary control. To get to F100-F109, you will use a different
   passcode, which is `|-  -  |-  -`, or clockwise, counter-clockwise,
   clockwise, and counter-clockwise. Again, press down on the rotary
   control. 
4. Rotate the the parameter you want to change, then press down on the knob.

After you've set a parameter, or once you've not interacted with it for
10 seconds, it will return to "normal" operation.

| Parameter | Use (I)                 | Use (V)                | Notes                                                     | Default |
| --------- | ----------------------- | ---------------------- | --------------------------------------------------------- | ------- |
| F001      | Coarse/Fine             | Same                   | 0 = coarse, 1 = fine, 2 = quick output (F100 set above 0) | 0       |
| F002      | Display Range           | Display Range          | 0 = 20mA/10V, 1 = 20mA/5V, 2 = 22mA/3.3V                  | 0       |
| F003      | Actual v Percentage     | Actual v Percentage    | 0 = Actual I/V, 1 = Percentage of range                   | 0       |
| F004      | Coarse Trimming         | Coarse Trimming        |                                                           | 1       |
| F005      | Fine Trimming           | Fine Trimming          |                                                           | 1       |
| F006      | Unused                  | Unused                 |                                                           |         |
| F007      | 0.2mA Calibration Value | 0.1V Calibration Value |                                                           |         |
| F008      | 20mA Calibration Value  | 10V Calibration Value  |                                                           |         |
| F009      | Screen Brightness       | Screen Brightness      | 0 = normal, 1 = bright, 2 = super bright                  |         |
| F100      |                         |                        |                                                           |         |
| F101      |                         |                        |                                                           |         |
| F102      |                         |                        |                                                           |         |
| F103      |                         |                        |                                                           |         |
| F104      |                         |                        |                                                           |         |
| F105      |                         |                        |                                                           |         |
| F106      |                         |                        |                                                           |         |
| F107      |                         |                        |                                                           |         |
| F108      |                         |                        |                                                           |         |
| F109      |                         |                        |                                                           |         |

## Saving Values

If you want to set a "default" value for it to start up in, you can
short-press the rotary wheel (about 1s). When you do that, it will
display `. . . .` on the screen, which means it saved the value. Now,
when you turn the box back on, it will use that as the starting point.

## Wiring Configurations

### External Power Supply

You can feed the device with an external power supply, between 15-30VDC,
even though the label says 24VDC. It will regulate it, just as it does
the internal battery. The hook-up is pretty bog standard:

![Diagram showing connections between device and power
supply](img/precision-external-power-supply.png)

### Constant Current

### Constant Voltage