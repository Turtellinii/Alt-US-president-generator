#!/usr/bin/env python3
"""
Batch simulator that runs the alternate history generator multiple times
and reprints simulations that meet specific criteria.
"""

import sys
import io
from alternate_president_generator import AlternateHistoryGenerator


def capture_simulation():
    """Run a single simulation and capture its output along with statistics"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    try:
        # Run simulation
        generator = AlternateHistoryGenerator()
        generator.run_simulation()

        # Get statistics
        assassinations = sum(1 for p in generator.presidents
                           if p.dies_in_office and p.death_cause == "Assassination")
        num_regimes = len(generator.authoritarian_regimes)

        # Get captured output
        output = captured_output.getvalue()

        return output, assassinations, num_regimes

    finally:
        # Restore stdout
        sys.stdout = old_stdout


def main():
    """Run 100 simulations and reprint those matching criteria"""
    print("="*80)
    print("BATCH SIMULATION - Running 100 alternate histories...")
    print("="*80)
    print("\nCriteria: At least 1 authoritarian regime AND at least 5 assassinations")
    print()

    qualifying_simulations = []

    for i in range(1, 101):
        print(f"Running simulation {i}/100...", end=" ", flush=True)

        output, assassinations, num_regimes = capture_simulation()

        print(f"(Regimes: {num_regimes}, Assassinations: {assassinations})", flush=True)

        # Check if this simulation meets criteria
        if num_regimes >= 1 and assassinations >= 5:
            qualifying_simulations.append({
                'number': i,
                'output': output,
                'assassinations': assassinations,
                'num_regimes': num_regimes
            })

    # Print results
    print("\n" + "="*80)
    print("BATCH SIMULATION COMPLETE")
    print("="*80)
    print(f"\nTotal simulations run: 100")
    print(f"Simulations meeting criteria: {len(qualifying_simulations)}")

    if qualifying_simulations:
        print("\n" + "="*80)
        print("QUALIFYING SIMULATIONS")
        print("="*80)

        for sim in qualifying_simulations:
            print("\n" + "#"*80)
            print(f"# SIMULATION #{sim['number']}")
            print(f"# Authoritarian Regimes: {sim['num_regimes']}")
            print(f"# Assassinations: {sim['assassinations']}")
            print("#"*80)
            print()
            print(sim['output'])
            print()
    else:
        print("\nNo simulations met the criteria (1+ regime AND 5+ assassinations)")


if __name__ == "__main__":
    main()
