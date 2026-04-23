#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from coder.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
problem = "Write a Python code to calculate the first 10,000 terms of the series , multipliying the total by 4: 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ..."

def run():

    inputs = {"problem": problem}
    try:
        result = Coder().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()