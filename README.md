
# Python_API v0.1
A basic command-line interface (CLI) that consumes a public API (open-notify) and returns the
date and time (EAT) when the International Space Station will next pass over a given set of
coordinates.

## Instructions for use:
1. Download setup.py and issdata.py to an empty directory
2. Set up a virtual environment. WARNING: This app uses the following third-party libraries
    'Click'
    'tzlocal'
    'requests'
3. Run `> pip install --editable` to test the app
4. Run the app with `> issdata <latitude> <longitude>`
5. Options available:
    --help : Display information about the app, arguments required and options available
    --city : Use preregistered city coordinates. Currently only 'nairobi' is registered.

Example:
`issdata 0 0` Latitude for the Equator and Longitude for Greenwich Meridian
`issdata -1.292 36.846` Latitude and Longitude for Nairobi
`issdata --city nairobi` Use option preregistered coordinates for nairobi