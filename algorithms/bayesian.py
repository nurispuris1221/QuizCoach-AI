"""Bayesian knowledge update for a binary answer."""
P_CORRECT_KNOWS = 0.85
P_CORRECT_NOT = 0.30


def update(prior, correct):
    if not 0 <= prior <= 1 or type(correct) is not bool:
        raise ValueError('Expected probability and boolean answer')
    lk = P_CORRECT_KNOWS if correct else 1 - P_CORRECT_KNOWS
    ln = P_CORRECT_NOT if correct else 1 - P_CORRECT_NOT
    evidence = lk * prior + ln * (1 - prior)
    return {'prior': prior, 'likelihood_knows': lk, 'likelihood_not': ln,
            'evidence': evidence, 'posterior': lk * prior / evidence}
