'''
This script defines the helper function `test_result` which evaluates my quantum circuits' performace using 
a given true value and tolerance.
'''

def test_result(pred, ans, tol):
    diff = abs(pred - ans) / ans
    if diff < tol:
        print('Success!!')
    else:
        print(f'Failure, off by {diff}.')
