# Reflection - Static Code Analysis

## 1. What did I learn?
I learned how Pylint, Bandit, and Flake8 help identify code quality,
security, and formatting problems in Python programs.

## 2. Which issues were most important?
The mutable default argument, broad exception handling, invalid passenger
counts, and Bandit B311 warning were important because they could lead to
unexpected behavior or indicate a security concern.

## 3. How did I improve the code?
I added documentation, improved naming conventions, validated passenger
counts and route IDs, handled empty trip lists, improved file handling,
and corrected formatting issues.

## 4. What did I learn about testing and analysis?
I learned that static analysis should be performed before and after making
changes. Comparing reports helps verify whether the changes improved the
code.

## Conclusion
After fixing the identified issues, Pylint reported a score of 10.00/10,
Bandit reported no issues, and Flake8 produced no output.