"""A request for when
the International Space Station
will next pass over Nairobi.
Uses open-notify.
"""

import json

from datetime import datetime

# third party libraries
import tzlocal
import requests
import click

def gettime(lat, lon):
    """Return in local date and time
    when the ISS will pass over the
    latitude and longitude passed as
    arguments.
    """
    parameters = {"lat": lat, "lon": lon, "n": 1}

    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

    data = response.json()

    risetime = float(data['response'][0]['risetime'])

    local_timezone = tzlocal.get_localzone()

    local_time = datetime.fromtimestamp(risetime, local_timezone)

    return local_time

@click.command()
@click.option('--city', default='none', help='Time ISS will pass over a city. Try nairobi')
@click.argument('lat', required=False)
@click.argument('lon', required=False)
def get_time(city, lat=400.5, lon=400.5):
    """Arguments - Latitude, Longitude
    """
    if city == 'none':
        if lat != 400.5 and lon != 400.5:
            isstime = gettime(lat, lon)
            click.echo(isstime)
        else:
            click.echo('Missing arguments: <Latitude> and <Longitude>')

    if city == 'nairobi':
        click.echo(gettime(-1.292, 36.846))
