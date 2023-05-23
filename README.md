# Calculating astronomical twilight

> Author: Matteo Tomasini
>
> Date: 23 May 2023

The goal of this exercise was to familiarize myself with coding small GUIs using `tkinter`. To this goal, I coded a little calculator to determine when the full night starts (_i.e._ the astronomical twilight ends) at a certain date and position. The main engine behind this code is the great package `ephem`.

## Astronomical twilight

As anyone who looks up at the sky knows, the night does not start with the setting of the Sun. In fact, after the Sun disapperas on the horizon, the sky enters twilight, which is classicaly divided in three: civil twilight lasts from the sunset to when the Sun is 6 degrees below the horizon; nautical twilight lasts from the end of civil twilight to when the Sun is 12 degrees below the horizon; astronomical twilight lasts from the end of nautical twilight to when the Sun is 18 degrees below the horizon. Any time between this moment and the start of astronomical twilight before sunrise is considered full night.

For astronomical observation, it is not necessarily needed for the sun to be below 18 degrees - many observations of some bright objects can be done during nautical and astronomical twilight, provided the objects are above the horizon at that time: however, to spot particularly dim objects (especially dim with respect to the tool one is using), night needs to start in order to have better chances at seeing the hunted object.

With the package `ephem`, the calculation is easy: once the date and the location on Earth are set (see official documentation of the package), one needs to modify the horizon of Earth, _e.g._ in my code at line 23:

```python
earth.horizon = '-18'
```

After which, one calculates the next setting and the next rising as usual.

### Note

Feel free to borrow from my code if you need - I myself have been scavenging the internet to write this. For any questions you can open an issue here on Github.
