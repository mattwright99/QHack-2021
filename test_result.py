'''
This script defines the helper function `test_result` which evaluates my quantum circuits' performace using 
a given true value and relative tolerance.
'''

import numpy as np
import warnings
warnings.filterwarnings("ignore")


def test_result(pred, ans, tol):
    diff = abs(pred - ans) / ans
    
    if type(pred) == float:
        if diff < tol:
            print('Success!!')
        else:
            print(f'Failure, off by {diff}.')
    
    else:
        # If the true result is 0.0 then check that the prediction is less than the tolerance
        
        inf_indices = ans == 0
        diff[inf_indices] = pred[inf_indices]
        
        if all(diff < tol):
            print('Success!!')
        else:
            print(f'Failure :(')
