'''
A very silly toy model for how LSST might observe, using random numbers.

Was started in this project:
https://github.com/jradavenport/MW-Flare
'''

import numpy as np
import matplotlib.pyplot as plt


def generate_visits(Nvisits=900, tspan=10, revisit=1.0,
                    stat=False, seasonscale=365./5., t0=0.):
    '''
    Use some very crude approximations for how visits will be spaced out:
    - Survey starts at midnight, time = 0.0
    - Can only observe at night, time > 0.75 | time < 0.25
    - Exposures are clustered around a season w/ a gaussian shape each year
    - Field is observable for first half of year, 0 < date < 182
    - On average, each field should be hit every 3 days during observable season


    Parameters
    ----------
    Nvisits : int, optional
        Number of visits to generate. Default is 900
    tspan : float, optional
        Total time span of data to simulate (in years). Default is 10
    revisit : float, optional
        The typical re-visit time within a night (in hours). Default is 1.0
    seasonscale : float, optional
        How wide to make the Gaussian season? Default is 365./5.
    stat : bool, optional
        Print some stats and make a plot? Default is False
        
    Returns
    -------
    The timestamps of the Nvisits (in days)

    '''

    # Generate random times for visit, between [0.75 and 0.25]
    # Make 2 arrays, since when field is visited it gets visited twice in 1 night
    time_of_day1 = np.random.random(Nvisits/2.) / 2. - 0.25
    time_of_day2 = time_of_day1 + np.random.normal(loc=revisit/24., scale=revisit/24./10., size=Nvisits/2.)
    
    time_of_day = np.concatenate((time_of_day1, time_of_day2))
    
    date_of_year = np.repeat(np.floor(np.random.normal(loc=365./4., scale=seasonscale, size=Nvisits/2.)), 2)

    year_of_obs = np.repeat(np.floor(np.random.random(Nvisits/2.) * tspan) * 365., 2)

    date_obs = time_of_day + date_of_year + year_of_obs + t0

    date_obs.sort()

    if stat is True:
        print('revisit time:')
        print(revisit/24.)
              
        print('mean time between visits:')
        print(np.mean(date_obs[1:] - date_obs[:-1]))

        print('median time between visits:')
        print(np.median(date_obs[1:] - date_obs[:-1]))

        plt.figure()
        _ = plt.hist(date_obs, bins=np.arange(date_obs.min(), date_obs.max(),7),
                     histtype='stepfilled', color='k')
        plt.xlabel('Time (days)')
        plt.ylabel('# Visits per Week')
        plt.show()

    return date_obs


def photerror(mag, nfloor=0.005, m5=24.89, gamma=0.038):
    '''
    http://arxiv.org/pdf/0805.2366v4.pdf
    use values from Ivezic 2008, assuming g-band
    '''

    x = 10.0**(0.4*(mag - m5))
    sigrand2 = (0.04 - gamma) * x + gamma * (x**2.0)

    err = (nfloor**2. + sigrand2)**0.5
    return err


if __name__ == "__main__":
    generate_visits(stat=True)
