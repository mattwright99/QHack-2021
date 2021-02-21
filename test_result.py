def test_result(pred, ans, tol):
    diff = abs(pred - ans) / ans
    if diff < tol:
        print('Success!!')
    else:
        print(f'Failure, off by {diff}.')
