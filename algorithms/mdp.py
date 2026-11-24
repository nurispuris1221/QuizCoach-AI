"""One-step MDP action comparison; no learned parameters."""
STATES = ('Beginner', 'Ready')
ACTIONS = ('Review Topic', 'Next Question')
# Each tuple is (next state, transition probability, immediate reward).
MODEL = {
    'Beginner': {'Review Topic': [('Beginner', .4, 2), ('Ready', .6, 6)],
                 'Next Question': [('Beginner', .9, 0), ('Ready', .1, 4)]},
    'Ready': {'Review Topic': [('Beginner', .1, -4), ('Ready', .9, 3)],
              'Next Question': [('Beginner', .2, 2), ('Ready', .8, 5)]}}


def decide(state):
    if state not in MODEL:
        raise ValueError('Unknown state')
    terms = {a: [{'next_state': s, 'probability': p, 'reward': r, 'product': p*r}
                 for s, p, r in MODEL[state][a]] for a in ACTIONS}
    values = {a: sum(t['product'] for t in terms[a]) for a in ACTIONS}
    return {'state': state, 'values': values, 'terms': terms,
            'action': max(ACTIONS, key=values.get)}
