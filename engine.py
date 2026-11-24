"""Shared orchestration for the local application and tests."""
import json
from pathlib import Path
from algorithms.bayesian import update
from algorithms.viterbi import infer
from algorithms.mdp import decide

QUESTIONS = json.loads((Path(__file__).parent / 'data/questions.json').read_text(encoding='utf-8'))


def analyze(history):
    prior = .5
    timeline = [prior]
    details = None
    for correct in history:
        details = update(prior, correct)
        prior = details['posterior']
        timeline.append(prior)
    hmm = infer(history[-3:])
    decision = decide(hmm['path'][-1]) if hmm['path'] else None
    return {'knowledge': prior, 'timeline': timeline, 'bayes': details,
            'hmm': hmm, 'observations': history[-3:], 'mdp': decision,
            'correct_count': sum(history), 'answered': len(history)}


def grade(choices):
    if not isinstance(choices, list) or len(choices) > len(QUESTIONS):
        raise ValueError('Invalid answer history')
    if any(type(c) is not int or not 0 <= c < len(QUESTIONS[i]['options']) for i,c in enumerate(choices)):
        raise ValueError('Invalid answer choice')
    result = analyze([c == QUESTIONS[i]['answer'] for i,c in enumerate(choices)])
    if choices:
        q = QUESTIONS[len(choices)-1]
        result['feedback'] = {'correct': choices[-1] == q['answer'], 'answer': q['options'][q['answer']],
                              'explanation': q['explanation'], 'topic': q['topic']}
    return result
