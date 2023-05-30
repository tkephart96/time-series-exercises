"""
Acquire some data for Time Series Exercises
"""

##### IMPORTS #####

import pandas as pd
import requests
import math

##### FUNCTIONS #####

import os

def get_ppl():
    '''Get Star Wars people as a dataframe'''
    # name of cached csv
    filename = 'sw_ppl.csv'
    # if cached data exist
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # wrangle from sw api if not cached
    else:
        ppl_url = 'https://swapi.dev/api/people/'
        response = requests.get(ppl_url)
        people = response.json()['results']
        nxt_ppl = response.json()['next']
        while nxt_ppl is not None:
            # print(nxt_ppl)
            response = requests.get(nxt_ppl)
            if response.status_code == 200:
                people += response.json()['results']
                nxt_ppl = response.json()['next']
                continue
            else:
                print(f'Error Code: {response.status_code}')
                break
        df = pd.DataFrame(people)
        # cache data locally
        df.to_csv(filename, index=False)
    return df

def get_planets():
    '''Get Star Wars planets as a dataframe'''
    # name of cached csv
    filename = 'sw_planets.csv'
    # if cached data exist
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # wrangle from sw api if not cached
    else:
        planets_url = 'https://swapi.dev/api/planets/'
        response = requests.get(planets_url)
        planets = response.json()['results']
        nxt_planet = response.json()['next']
        while nxt_planet is not None:
            # print(nxt_planet)
            response = requests.get(nxt_planet)
            if response.status_code == 200:
                planets += response.json()['results']
                nxt_planet = response.json()['next']
                continue
            else:
                print(f'Error Code: {response.status_code}')
                break
        df = pd.DataFrame(planets)
        # cache data locally
        df.to_csv(filename, index=False)
    return df

def get_starships():
    '''Get Star Wars starships as a dataframe'''
    # name of cached csv
    filename = 'sw_starships.csv'
    # if cached data exist
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # wrangle from sw api if not cached
    else:
        starships_url = 'https://swapi.dev/api/starships/'
        response = requests.get(starships_url)
        starships = response.json()['results']
        nxt_starship = response.json()['next']
        while nxt_starship is not None:
            # print(nxt_starship)
            response = requests.get(nxt_starship)
            if response.status_code == 200:
                starships += response.json()['results']
                nxt_starship = response.json()['next']
                continue
            else:
                print(f'Error Code: {response.status_code}')
                break
        df = pd.DataFrame(starships)
        # cache data locally
        df.to_csv(filename, index=False)
    return df

def get_sw_data():
    '''Get Star Wars people, planets, and starships as one dataframe'''
    ppl = get_ppl()
    planets = get_planets()
    starships = get_starships()
    return pd.concat([ppl,planets,starships])

def get_german_power():
    '''
    Get Open Power Systems Data for Germany as a dataframe
    The data set includes country-wide totals of electricity consumption, 
    wind power production, and solar power production for 2006-2017.
    '''
    # name of cached csv
    filename = 'german_power.csv'
    # if cached data exist
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # wrangle from sw api if not cached
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        # cache data locally
        df.to_csv(filename, index=False)
    return df