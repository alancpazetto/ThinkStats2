"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ValidatePregNum(resp):
    
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False
    
    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    # preg = nsfg.ReadFemPreg()
    # preg_map = nsfg.MakePregMap(preg)

    resp = nsfg.ReadFemResp()

    # resp.replace(0, np.nan, inplace=True)
    # resp.loc[ resp.pregnum > 7, 'pregnum' ] = 7
    # https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835

    assert( len(resp) == 7643 )
    assert( resp.pregnum.value_counts()[1] == 1267 )
    assert( ValidatePregNum(resp) )



    # print(resp.pregnum.value_counts().sort_index())

    # case_id = 10229
    # indices = preg_map[case_id]

    # print(indices)
    # print( preg.outcome[indices].values )

    # preg.loc[:13, 'prglngth'] = 1
    # preg.loc[14:26, 'prglngth'] = 2
    # preg.loc[26:, 'prglngth'] = 3




    # ======================================================
    # preg['totalwgt_kg'] = preg['totalwgt_lb'] * 0.45359237
    # print( preg.totalwgt_kg.mean() )
    # ======================================================

    # print( preg[(preg.caseid==5012) & (preg.pregordr==1)].totalwgt_kg )
    
    

    # ======================================================
    # preg.loc[preg.prglngth.astype(int) <= 13, 'prglngth'] = 1
    # preg.loc[ (preg.prglngth.astype(int) > 13) & (preg.prglngth.astype(int) <= 26), 'prglngth'] = 2
    # preg.loc[preg.prglngth.astype(int) > 26, 'prglngth'] = 3

    # preg.loc[preg.prglngth.astype(str) == '1', 'prglngth'] = '0-13'
    # preg.loc[preg.prglngth.astype(str) == '2', 'prglngth'] = '13-26'
    # preg.loc[preg.prglngth.astype(str) == '3', 'prglngth'] = '26-50'

    # print( preg['prglngth'].value_counts().sort_index() )
    # ======================================================

    # print(birthord[0:10])


    # print(preg.outcome.head())
    # print(preg['pregordr'][:10])
    # print( preg.outcome.value_counts(sort=False) )
    # print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
