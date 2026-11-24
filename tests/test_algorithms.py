import unittest
from itertools import product
from algorithms.bayesian import update
from algorithms.viterbi import infer, INITIAL, TRANSITION, EMISSION, STATES
from algorithms.mdp import decide, MODEL
from engine import analyze, grade

class Algorithms(unittest.TestCase):
    def test_bayes_correct(self): self.assertAlmostEqual(update(.5, True)['posterior'], .85/1.15)
    def test_bayes_wrong(self): self.assertAlmostEqual(update(.5, False)['posterior'], .15/.85)
    def test_bayes_bounds(self):
        for p in (0, .5, 1):
            for c in (True, False): self.assertTrue(0 <= update(p,c)['posterior'] <= 1)
    def test_viterbi_exhaustive(self):
        for obs in product((False,True), repeat=3):
            def prob(path):
                p=INITIAL[path[0]]*EMISSION[path[0]][obs[0]]
                for i in range(1,3): p*=TRANSITION[path[i-1]][path[i]]*EMISSION[path[i]][obs[i]]
                return p
            result=infer(obs)
            self.assertAlmostEqual(prob(result['path']),max(map(prob,product(STATES,repeat=3))))
            self.assertAlmostEqual(result['probability'],prob(result['path']))
    def test_mdp_beginner(self):
        r=decide('Beginner'); self.assertAlmostEqual(r['values']['Review Topic'],4.4); self.assertAlmostEqual(r['values']['Next Question'],.4); self.assertEqual(r['action'],'Review Topic')
    def test_mdp_ready(self):
        r=decide('Ready'); self.assertAlmostEqual(r['values']['Review Topic'],2.3); self.assertAlmostEqual(r['values']['Next Question'],4.4); self.assertEqual(r['action'],'Next Question')
    def test_normalized_transitions(self):
        for actions in MODEL.values():
            for outcomes in actions.values(): self.assertAlmostEqual(sum(p for _,p,_ in outcomes),1)
    def test_empty(self): self.assertIsNone(analyze([])['mdp'])
    def test_strong(self): self.assertEqual(analyze([True]*5)['mdp']['action'],'Next Question')
    def test_weak(self): self.assertEqual(analyze([False]*5)['mdp']['action'],'Review Topic')
    def test_improving(self): self.assertEqual(analyze([False,False,True,True,True])['mdp']['action'],'Next Question')
    def test_declining(self): self.assertEqual(analyze([True,True,True,False,False])['mdp']['action'],'Review Topic')
    def test_grade(self): self.assertEqual(grade([1,2,2,3,0])['correct_count'],5)
    def test_invalid_choice(self):
        for c in ([4], [True], [0]*6, None):
            with self.assertRaises(ValueError): grade(c)

if __name__=='__main__': unittest.main()
