
import numpy as np
import scipy as sp
from scipy import linalg
from scipy import stats
import scipy.ndimage as ndimage
from datetime import date


def detect(t, temp, pctile=90, minDuration=2):
    '''
    
    Simplification of code produced for Hobday et al. (2016)'s paper on marine heat waves.
    
    
    
    Inputs:
      t       Time vector, in datetime format (e.g., date(1982,1,1).toordinal())
              [1D numpy array of length T]
      temp    Temperature vector [1D numpy array of length T]
    
    
    Outputs:
    
      mhw     Detected heatwaves. Each key (following list) is a
              list of length N where N is the number of detected heatwaves:
 

        'date_start'           Start date of MHW [datetime format]
        'date_end'             End date of MHW [datetime format]
        'duration'             Duration of MHW [days]


    Options:

      pctile                 Threshold percentile (%) for detection of extreme values
                             (DEFAULT = 90)
      minDuration            Minimum duration for acceptance detected MHWs
                             (DEFAULT = 2 [days])

    Notes:
    Original code/documentation written by Eric Oliver, Institue for Marine and Antarctic Studies, University of Tasmania, Feb 2015
    
    Original repo: https://github.com/ecjoliver/marineHeatWaves
    
    
    '''

    # Initialize heatwave output variable
    mhw = {}

    mhw['date_start'] = [] # datetime format
    mhw['date_end'] = [] # datetime format
    mhw['duration'] = [] # [days]
    mhw['time_start'] = [] # [days]
    mhw['time_end'] = [] # [days]



    # Time series of "True" when threshold is exceeded, "False" otherwise    
    exceed_bool = temp - np.percentile(temp, pctile)
    exceed_bool[exceed_bool<=0] = False
    exceed_bool[exceed_bool>0] = True
    
    # Fix issue where missing temp vaues (nan) are counted as True
    exceed_bool[np.isnan(exceed_bool)] = False
    
    # Find contiguous regions of exceed_bool = True
    events, n_events = ndimage.label(exceed_bool)

    # Find all MHW events of duration >= minDuration
    for ev in range(1,n_events+1):
        event_duration = (events == ev).sum()
        if event_duration < minDuration:
            continue
        mhw['time_start'].append(t[np.where(events == ev)[0][0]])
        mhw['time_end'].append(t[np.where(events == ev)[0][-1]])


    # Calculate marine heat wave properties
    mhw['n_events'] = len(mhw['time_start'])
    for ev in range(mhw['n_events']):
        mhw['date_start'].append(date.fromordinal(mhw['time_start'][ev]))
        mhw['date_end'].append(date.fromordinal(mhw['time_end'][ev]))



    return mhw

