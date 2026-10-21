# python_basics

A small collection of Python exercises and fundamentals — notes and solutions
kept while learning to reason in code. Everything here is written by hand and
kept deliberately simple: the point is to show the thinking behind each step,
not to hide it behind frameworks or tooling.

## What's inside

| File | Description |
| --- | --- |
| `sum application/exercises/1helloworld.py` | First script: prints a greeting. |
| `sum application/exercises/2extrmelybasic.py` | Reads two numbers from stdin and prints their sum. |
| `sum application/server/sum_brincation.py` | Grades a student score (pass, another chance or fail) and validates the input. |
| `sum application/server/main.py` | Entry point of the sum application; reuses `check_errors` and `pass_or_fail` from `sum_brincation.py`. |
| `sum application/next_steps.md` | Short list of ideas that are still to be implemented. |
| `exercises/climbing_stains.py` | Climbing stairs problem solved with dynamic programming. |

## How to run

Requires Python 3. The `sum application` folder name contains a space, so
quote the paths.

```bash
python "sum application/exercises/1helloworld.py"
python "sum application/exercises/2extrmelybasic.py"
python "sum application/server/sum_brincation.py"
python "sum application/server/main.py"
```

The two server scripts ask for a comma-separated sequence of numbers, so you
can pipe the input in:

```bash
echo "10,5" | python "sum application/server/sum_brincation.py"
echo "10,5" | python "sum application/server/main.py"
```

The climbing stairs exercise is a class, so it can be imported and called
directly:

```bash
python -c "from exercises.climbing_stains import Solution; print(Solution().climbStairs(5))"
```

## Notes

These are learning exercises kept as-is for reference, not production code.

## License

MIT — see [LICENSE](LICENSE).
