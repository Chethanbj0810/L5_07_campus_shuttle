# Static Code Analysis - Issues Found

## Project
Campus Shuttle System

## Tools Used
- Pylint
- Bandit
- Flake8

## Issues Identified in the Original Code

### 1. Missing Documentation
**Tool:** Pylint  
**Issue:** The module and several functions did not have docstrings.  
**Fix:** Added module and function docstrings to explain the purpose of the code.

### 2. Mutable Default Argument
**Tool:** Pylint  
**Issue:** The add_trip_log() function used an empty list as a default argument. This list could be shared across function calls.  
**Fix:** Changed the default to None and created a new list when needed.

### 3. Unsafe Exception Handling
**Tool:** Pylint  
**Issue:** The underused_routes() function used a bare except statement, which could hide unexpected errors.  
**Fix:** Removed the broad exception handling and handled empty trip lists in average_load().

### 4. Insecure Random Number Generator Warning
**Tool:** Bandit  
**Issue:** Bandit reported B311 because random.choice() uses a pseudorandom generator.  
**Fix:** Replaced random with secrets and used secrets.choice().

### 5. File Handling
**Tool:** Pylint  
**Issue:** The original code opened files without specifying an encoding and did not use context managers.  
**Fix:** Used Path.open() with UTF-8 encoding and with statements.

### 6. Naming Convention
**Tool:** Pylint  
**Issue:** The assignDriver() function did not follow the Python snake_case naming convention.  
**Fix:** Renamed it to assign_driver().

### 7. Formatting Problems
**Tool:** Flake8  
**Issue:** The original source code contained formatting and style violations.  
**Fix:** Reformatted the source code to follow Python style conventions.

### 8. Input Validation and Runtime Errors
**Tool:** Code review  
**Issue:** The original program accepted invalid passenger counts, including negative values and text, and could fail when calculating an average for an empty route or looking up a deleted route.  
**Fix:** Added passenger-count validation, handled empty routes, and checked route IDs before accessing them.

## Final Results

- Pylint score: 10.00/10 (previously reported).
- Bandit: No issues identified (previously reported).
- Flake8: No issues reported (previously reported).