def calculate_stats(numbers):
    '''
    Calculate basic descriptive statistics for a list of numbers.
 
    Parameters
    ----------
    numbers : list of int or float
 
    Returns
    -------
    dict with keys: count, mean, median, min, max
 
    Example
    -------
    >>> calculate_stats([1, 2, 3, 4, 5])
    {'count': 5, 'mean': 3.0, 'median': 3, 'min': 1, 'max': 5}
    '''
    if not numbers:
        return None
    n   = len(numbers)
    srt = sorted(numbers)
    mid = n // 2
    med = srt[mid] if n % 2 else (srt[mid-1] + srt[mid]) / 2
    return {'count': n, 'mean': sum(numbers)/n,
            'median': med, 'min': min(numbers), 'max': max(numbers)}
 
# Access the docstring
help(calculate_stats)
 
# Test it
print(calculate_stats([85, 92, 78, 95, 88]))
# {'count': 5, 'mean': 87.6, 'median': 88, 'min': 78, 'max': 95}
