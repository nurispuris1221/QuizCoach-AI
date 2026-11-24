# Defense guide (English)
## 0:00–2:00 — Problem and objectives
Traditional quizzes provide a score, but the same score can hide different recent learning patterns. QuizCoach AI demonstrates how evidence, hidden states and decisions can be combined. The scope is five Python questions, two hidden states, two actions and a three-answer HMM window. Our objective is an explainable classroom prototype, not a validated tutor.
## 2:00–6:00 — Live demo
Open localhost, submit two wrong answers (A, A), read the suggested review; then submit C, D, A correctly. Show the dashboard and the actual calculation panel after each answer. After the fifth answer, the score is 3/5, Bayesian estimate 51.09%, HMM path Ready/Ready/Ready, MDP recommends Next Question. Restart to show reset. Run `python demo.py` if the browser is unavailable. Show `python -m unittest discover -s tests -v` and actual results.
## 6:00–8:00 — Three algorithms
Bayes: posterior = likelihood × prior / evidence. First correct answer gives 73.91%, first wrong gives 17.65%. Viterbi: the highest joint probability ending in each hidden state is computed with a max over predecessor states; backtracking gives the best path. MDP: expected immediate reward is the sum of probability times reward; choose the maximum. Beginner review: 0.4×2 + 0.6×6 = 4.4 versus 0.4. Ready next: 4.4 versus 2.3. All model parameters are illustrative.
## Q&A practice
- Why Bayes and HMM? Bayes accumulates evidence without order; HMM models the order of recent observations. They are separate estimates, so they can disagree.
- Why Viterbi rather than simply counting answers? It uses initial, transition and emission probabilities and finds an entire most likely hidden state sequence.
- Are Viterbi scores state probabilities? No, they are joint path scores; a forward algorithm would marginalize over paths.
- Why MDP? Actions can change the next state and yield different rewards. Our one-step model uses given transitions, not reinforcement learning or value iteration.
- What is adaptive? Review versus move on; questions remain fixed.
- Are the numbers real? No. The course guidelines allow predefined toy values. No learning improvement is claimed.
- What is tested? Known Bayes outputs, exhaustive eight HMM observation sequences against brute force, MDP scores, invalid inputs, five-answer HTTP session and static endpoints. Browser test was blocked in the generation environment; rerun locally.
- Why is MDP approximate? Hidden states are estimated; treating one most likely state as fully observed discards uncertainty. A belief-state policy is a future improvement.
