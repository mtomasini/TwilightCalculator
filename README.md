# Calculating astronomical twilight

> Author: Matteo Tomasini
>
> Date: 23 May 2023

The goal of this exercise was to familiarize myself with coding small GUIs using `tkinter`. To this goal, I coded a little calculator to determine when different twilights end, for a certain date and position. The main engine behind this code is the great package `ephem`.

## Types of twilight

As anyone who looks up at the sky knows, the night does not start with the setting of the Sun. In fact, after the Sun disapperas below the horizon, the sky enters twilight, which is classicaly divided in three periods: civil twilight lasts from the sunset to when the Sun is 6 degrees below the horizon; nautical twilight lasts from the end of civil twilight to when the Sun is 12 degrees below the horizon; astronomical twilight lasts from the end of nautical twilight to when the Sun is 18 degrees below the horizon. Any time between this moment and the start of astronomical twilight before sunrise is considered full night.

For astronomical observation, it is not necessarily needed for the sun to be below 18 degrees - many observations of some bright objects can be done during nautical and astronomical twilight, provided the objects are above the horizon at that time: however, to spot particularly dim objects (especially dim with respect to the tool one is using), the full night needs to start in order to have better chances of seeing the hunted object.

With the package `ephem`, the calculation is easy. Once the date and the location on Earth are set (see official documentation of the package), one needs to modify the horizon of Earth, _e.g._ in my code at lines 22--29:

```python
earth.horizon = '0' # or '-6', '-12', '-18', depending on the input value 
```

After which, one calculates the next setting and the next rising as usual using the package.

## Usage and notes

To use the tool, the best is to have a python environment set up with `pandas`, `ephem` and `tkinter` installed (all three can be installed using `pip`), then simply download the `.py`script and run locally:

```bash
python twilight_calculator.py
```

The GUI will pop up on the screen and you'll be able to enter the date (in format `YYYY-MM-DD`) and the location at which you wanna calculate the end of twilight (in format `lon/lat` - note the slash `/`, _e.g._ you need to enter `56.511/7.102` - decimal precision is arbitrary). I did not put any effort into parsing the input, but if you stick to the described format you will have no problem. Then, select which twilight you want to calculate -- the calculation will give you the time of the end of that twilight (or the time of sunset, which is the default in the dropdown menu). Click on the `Calculate!` button, and _voilà_!

Feel free to borrow from my code if you need - I myself have been scavenging the internet to write this. For any questions you can open an issue here on Github.
