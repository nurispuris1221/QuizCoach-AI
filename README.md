# QuizCoach AI
A small, explainable adaptive Python quiz for the AI Fundamentals final project (Topic 01).

## Run locally (Windows, macOS, Linux)
Requires Python 3.10 or newer. No pip packages, accounts, API keys, or internet access required.

```bash
python app.py
```
On Windows, `py -3 app.py` or double-click `start_windows.bat` also works. Open **http://127.0.0.1:8000** in a browser. If the port is occupied, run `python app.py --port 8001` and use that port. Stop with Ctrl+C.

## Use
Choose an option and submit. The dashboard shows the cumulative Bayesian estimate, last-three-answer Viterbi path, one-step MDP action and calculation details. If Review is recommended, read the explanation and acknowledge it before advancing. Five questions are fixed; the review path is adaptive, not question difficulty. Restart clears the session. The app binds to localhost; it is a classroom prototype, not a public production service.

## Algorithms
- **Bayes:** prior 0.5; correct likelihood 0.85 if knows, 0.30 otherwise; wrong likelihoods 0.15 and 0.70. Each posterior becomes the next prior. Assumes answers are conditionally independent given broad Python fundamentals knowledge.
- **HMM / Viterbi:** Beginner and Ready; equal initial probabilities; transition rows [0.80, 0.20], [0.15, 0.85]; correct emissions 0.30 and 0.85. Dynamic programming and backtracking on latest three responses; one or two responses give provisional paths. Scores are joint path probabilities, not state posterior probabilities.
- **MDP:** uses last Viterbi state as a point estimate; sums transition probability × immediate reward, selects maximum. Beginner: Review 4.40 vs Next 0.40; Ready: Review 2.30 vs Next 4.40. No full value iteration or learned policy.

## Tests and demo
```bash
python -m unittest discover -s tests -v
python demo.py
```
Sample sequence I,I,C,C,C: final score 3/5, Bayes 51.09%, Viterbi Ready → Ready → Ready, MDP Next Question. Reverse-order C,C,C,I,I has the same Bayesian score but a different inferred state and recommendation. See `docs/test_results.txt` and `docs/demo_output.txt` for actual runs. HTTP tests exercise the server; interactive browser test was blocked by the execution environment's browser policy. Verify the UI locally before defense.

## Structure
`app.py` HTTP server; `engine.py` orchestration; `algorithms/` independent implementations; `data/` question bank; `static/` interface; `tests/` test suite; `docs/` project documentation. `demo.py` console fallback.

## Limitations
All probabilities, rewards and transitions are illustrative, not estimated from student data. This is not a validated knowledge assessment. The HMM assumes a fixed transition model and resets its prior in each rolling window. The MDP treats the inferred state as known, ignoring uncertainty. No learning gains have been measured. No LLM is called by the app.

## Publish to GitHub
Create an empty repository in your GitHub account, then run these commands in the extracted project folder (replace YOUR-USERNAME):
```bash
git init
git add .
git commit -m "Initial QuizCoach AI prototype"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/QuizCoach-AI.git
git push -u origin main
```
The archive is repository-ready, but has not been published to an account. Review AI usage and contribution statements before submitting. Source: course handout *FINAL PROJECT. Detailed Guidelines*, Topic 01 and implementation note.
