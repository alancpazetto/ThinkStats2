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


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    # case_id = 10229
    # indices = preg_map[case_id]

    # print(indices)
    # print( preg.outcome[indices].values )

    # preg.loc[:13, 'prglngth'] = 1
    # preg.loc[14:26, 'prglngth'] = 2
    # preg.loc[26:, 'prglngth'] = 3




    # df['totalwgt_kg'] = 





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
