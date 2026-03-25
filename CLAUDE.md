# LeetCode Repository

Python solutions for the LeetCode 75 study plan.

## Project Structure

```
questions/          # LeetCode solutions (numbered by problem ID)
ml/                 # Basic ML examples (Keras, PyTorch, XGBoost)
ml_v2/              # Improved ML examples + IMDB attention model
interview_questions/ # Interview prep files
question_notes.md   # Running notes on solutions and learnings
```

## Conventions

### File naming
`questions/[PROBLEM_NUMBER]_[problem_slug].py`
Example: `questions/933_number_of_recent_calls.py`

### Solution file template
```python
"""
Start: [TIME]
End: [TIME]

[LeetCode URL]

[Problem description, examples, constraints]

Questions / notes:
 -

Options
 -

Notes for next time:
 -
"""

from unittest import TestCase

class Solution:
    def methodName(self, param: type) -> returnType:
        ...

tc = TestCase()
tc.assertEqual(Solution().methodName(...), expected)
```

## Creating New Solution Files

See AGENTS.md for the full specification. Key points:
- Set `Start:` to current time, `End:` to `TODO`
- Fix exponent notation from LeetCode (write `10^5` not `105`)
- Add method stub only — no implementation
- Include all example test cases (they should fail until solved)
- Leave Questions/notes, Options, and Notes for next time sections empty

## Critiquing Solutions

When asked to critique a solution or options in a `questions/` file:
- Provide critique only (correctness, complexity, style, edge cases)
- Do not edit the file

## Committing and Pushing

See AGENTS.md. Always stage all changes (`git add -A`) unless told otherwise.

## Testing

Tests use Python's built-in `unittest.TestCase`. Run a file directly to execute its tests:
```
python questions/933_number_of_recent_calls.py
```

## ML Subproject

The `ml_v2/imdb_attention/` project is a standalone PyTorch attention model. Run from repo root:
```
python ml_v2/imdb_attention/main.py
```
Dependencies are in `requirements.txt` (PyTorch, scikit-learn, XGBoost, Keras, datasets).
