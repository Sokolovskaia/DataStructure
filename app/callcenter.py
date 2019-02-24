def worker_bonus(week_scores):
    """
    >>> worker_bonus([[4, 3, 2]])
    0

    >>> worker_bonus([[4, 3, 4]])
    1
    >>> worker_bonus([[5], [5], [4, 2]])
    0
    >>> worker_bonus([[4, 4], [5], [5]])
    3


    """
    total = 0
    bonus_bound = 3
    for day_scores in week_scores:
        min_score = min(day_scores)
        if min_score < bonus_bound:
            return 0
        total += 1

    return total


