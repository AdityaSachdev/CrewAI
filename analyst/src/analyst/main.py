#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from analyst.crew import Analyst       

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    input_data = {
        "sector": "India's Defence Industry"
    }
    
    result = Analyst().crew().kickoff(inputs=input_data)
    print(result.raw)

if __name__ == "__main__":
  run()
