# lab 1: Grade Evaluator & Archiver

## Project Overview

This project calculates a student's final academic standing from a CSV file of
course grades, and provides a shell script that archives the grade file and
resets the workspace for the next batch.

## What the project does
The project has two programs `grade-evaluator.py` and `organizer.sh`.

The first, `grade-evaluator.py`, reads the grades and works out the final grade,
the GPA, whether the student passed, and which formative assignments (if any)
they can resubmit. The second, `organizer.sh`, is a shell script that files away
the current `grades.csv` into an archive folder with the date and time stamped
onto its name, then leaves a fresh empty `grades.csv` behind so you're ready for
the next set of grades.

## Files in this repository

- `grade-evaluator.py` - the Python script that does the grade calculations.
- `organizer.sh` - the Bash script that archives and logs.
- `Readme.md` - walkthrough of the project
- `grades.csv` - contains the grades from which the python script runs

## The grades file

`grades.csv` needs a header row and these four columns:

```
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

`group` has to be either `Formative` or `Summative`, `score` is a percentage
from 0 to 100, and the weights have to add up to 100 — 60 across the formatives
and 40 across the summatives.

## Requirements

- Python 3
- A Bash shell

## How to Run the Python Application

From the project directory, run:

```bash
python3 grade-evaluator.py
```

The program will prompt for a filename. Enter `grades.csv` (or the name of any
correctly formatted CSV in the same directory):

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### What it does

1. **Grade validation** — checks that every score is between 0 and 100.
2. **Weight validation** — confirms the weights sum to 100, with a 60/40
   Formative/Summative split.
3. **GPA calculation** — computes the final grade from the weighted scores and
   the GPA using `GPA = (Total Grade / 100) * 5.0`.
4. **Pass/Fail decision** — a student passes only if they score at least 50% in
   **both** the Formative and Summative categories (not just 50% overall).
5. **Resubmission** — lists any failed formative assignment (score below 50)
   that carries the highest weight. If several failed formatives share that
   highest weight, all of them are listed.

## How to Run the Shell Script

The script may need to be made executable first:

```bash
chmod +x organizer.sh
./organizer.sh
```

### What it does

1. Creates an `archive/` directory if one does not already exist.
2. Generates a timestamp (format `YYYYMMDD_HHMMSS`).
3. Moves `grades.csv` into `archive/` with a timestamped name, e.g.
   `archive/grades_20251105_170000.csv`.
4. Creates a new, empty `grades.csv` in the current directory.
5. Appends a record of the operation to `organizer.log` (the log accumulates
   one entry per run).

## Error Handling

The Python program handles the following cases gracefully, with a clear message
and no crash:

- The CSV file does not exist.
- The CSV file is empty (for example, the fresh file created by
  `organizer.sh`).
- A score is outside the 0–100 range.
- The weights do not sum to 100, or the 60/40 split is not respected.
- A group value is neither `Formative` nor `Summative`.