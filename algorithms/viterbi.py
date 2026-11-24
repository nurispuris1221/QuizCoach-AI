"""Two-state HMM: dynamic programming and backtracking."""
STATES = ('Beginner', 'Ready')
INITIAL = {'Beginner': 0.5, 'Ready': 0.5}
TRANSITION = {'Beginner': {'Beginner': 0.8, 'Ready': 0.2},
              'Ready': {'Beginner': 0.15, 'Ready': 0.85}}
EMISSION = {'Beginner': {True: 0.3, False: 0.7},
            'Ready': {True: 0.85, False: 0.15}}


def infer(observations):
    if any(type(o) is not bool for o in observations):
        raise ValueError('Observations must be booleans')
    if not observations:
        return {'path': [], 'scores': [], 'probability': None}
    scores = [{s: INITIAL[s] * EMISSION[s][observations[0]] for s in STATES}]
    back = []
    for obs in observations[1:]:
        row, pointers = {}, {}
        for s in STATES:
            prev = max(STATES, key=lambda p: scores[-1][p] * TRANSITION[p][s])
            pointers[s] = prev
            row[s] = scores[-1][prev] * TRANSITION[prev][s] * EMISSION[s][obs]
        scores.append(row)
        back.append(pointers)
    last = max(STATES, key=lambda s: scores[-1][s])
    path = [last]
    for pointers in reversed(back):
        path.append(pointers[path[-1]])
    return {'path': list(reversed(path)), 'scores': scores, 'probability': scores[-1][last]}
