#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import pandas as pd
from datetime import date

from .utils import cik_mapping

class Client:
    def __init__(self) :
        self._base_url = 'https://data.sec.gov/api/xbrl/companyconcept/CIK'
        
        self._header = {
            'User-Agent' : 'Personal Access'
        }
        
    def get_eps(self, tickers:list[str]) -> pd.DataFrame:
        _eps_url = '/us-gaap/EarningsPerShareDiluted.json'
        eps = []
        for tic in tickers :
            cik = cik_mapping[tic]
            url = self._base_url + cik + _eps_url
            s = requests.get(url, headers = self._header)
            try :
                hist = pd.DataFrame(json.loads(s.text)['units']['USD/shares'])
                hist = hist.loc[hist['frame'].map(lambda x : 'Q' in x if type(x) == str else False)][['val', 'frame']]
                hist.loc[:, 'frame'] = hist.loc[:, 'frame'].map(lambda x : x[4:])
                hist.columns = [tic, 'period']
                hist.set_index('period', inplace = True)
                
                #Weird adjustment on the history
                hist = hist.loc[EPS.index != '08Q4I']
                
                #Transforming the index into dates
                hist.index = hist.index.map(lambda x : date(int('20'+x[:2]), int(x[-1])*3, 1))
                
                eps.append(hist)
            except : 
                print(f'{tic} history not found')
                            
        return eps[0].join(eps[1:], how='outer')
        
    def number_of_shares(self, tickers:list[str]) -> pd.DataFrame:
        _post_url = '/us-gaap/WeightedAverageNumberOfDilutedSharesOutstanding.json'
        data = []
        for tic in tickers :
            cik = cik_mapping[tic]
            url = self._base_url + cik + _post_url
            s = requests.get(url, headers = self._header)
            try :
                hist = pd.DataFrame(json.loads(s.text)['units']['USD/shares'])
                hist = hist.loc[hist['frame'].map(lambda x : 'Q' in x if type(x) == str else False)][['val', 'frame']]
                hist.loc[:, 'frame'] = hist.loc[:, 'frame'].map(lambda x : x[4:])
                hist.columns = [tic, 'period']
                hist.set_index('period', inplace = True)
                
                #Weird adjustment on the history
                hist = hist.loc[EPS.index != '08Q4I']
                
                #Transforming the index into dates
                hist.index = hist.index.map(lambda x : date(int('20'+x[:2]), int(x[-1])*3, 1))
                
                data.append(hist)
            except : 
                print(f'{tic} history not found')
                
        return data[0].join(data[1:], how='outer')
    
    def book_value(self, tickers:list[str]) -> pd.DataFrame:
        pass
        
        
           
    
    