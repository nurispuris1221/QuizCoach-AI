"""Reproducible console demonstration using the exact same engine as the web app."""
from engine import grade
if __name__ == '__main__':
    choices = [0, 0, 2, 3, 0]
    for i in range(1, len(choices)+1):
        r = grade(choices[:i]); b=r['bayes']; h=r['hmm']; m=r['mdp']
        print(f"Q{i}: {'Correct' if r['feedback']['correct'] else 'Incorrect'} | {r['feedback']['topic']}")
        print(f"  Bayes: {b['prior']:.4f} * {b['likelihood_knows']:.4f} / {b['evidence']:.4f} = {b['posterior']:.4f}")
        print(f"  Viterbi: {', '.join('C' if x else 'I' for x in r['observations'])} -> {' / '.join(h['path'])}")
        print(f"  MDP: Review={m['values']['Review Topic']:.2f}; Next={m['values']['Next Question']:.2f} -> {m['action']}")
        print(f"  Feedback: {r['feedback']['explanation']}\n")
    print(f"Final score: {r['correct_count']} / 5 | Knowledge: {r['knowledge']:.2%}")
