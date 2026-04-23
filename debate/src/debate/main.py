#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from debate.crew import Debate

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Real estate investing',
        'motion': 'Buying a real estate property in India is a good investment',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

