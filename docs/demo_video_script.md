# Demo video narration

Console-based demonstration; synthetic English narration. Run `python demo.py` to reproduce. For a browser recording, use the live-demo sequence in `defense_guide.md`.

## Scene 1: Why QuizCoach AI?
QuizCoach AI is a small adaptive Python quiz for the AI Fundamentals final project. Instead of showing only a score, it estimates knowledge, infers recent hidden states, and recommends the next learning action. This video uses the actual Python console engine.


## Scene 2: Question 1 of 5
The first answer is incorrect. Bayesian inference updates the initial fifty percent belief to seventeen point six five percent. Viterbi provisionally infers Beginner. The expected reward for Review is four point four, greater than Next, so the engine recommends review.


## Scene 3: Question 2 of 5
The second answer is also incorrect. The knowledge estimate falls to four point three nine percent. The recent state sequence is Beginner, Beginner. The recommendation remains review. The application shows the correct answer and a short explanation.


## Scene 4: Question 3 of 5
The third answer is correct. Knowledge increases to eleven point five one percent. Viterbi uses three observations now, and the best path is still three Beginner states. One correct answer does not necessarily imply readiness, so review is still recommended.


## Scene 5: Question 4 of 5
The fourth answer is correct. The estimate rises to twenty six point nine three percent. In the latest window, Viterbi infers Beginner, Ready, Ready. The MDP now prefers Next Question, because the expected reward is four point four rather than two point three.


## Scene 6: Question 5 of 5
The fifth answer is correct. The final score is three out of five, and the knowledge estimate reaches fifty one point zero nine percent. The most likely recent path is Ready, Ready, Ready, so the recommendation is to move on to future practice.


## Scene 7: Same score, different recommendation
The improving and declining scenarios have the same quiz score and Bayesian posterior, but their recent state sequences differ. This demonstrates the value of modeling answer order. Eighteen automated algorithm and HTTP tests passed. Browser interaction still needs to be verified locally.


## Scene 8: What the prototype demonstrates
The three AI topics work together in an explainable small prototype. All probabilities and rewards are illustrative assumptions permitted by the course guidelines. The next step is to calibrate them using appropriate learning data. Thank you.
