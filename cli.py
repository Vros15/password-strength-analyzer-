"""
cli.py

Command-line interface for the Password Strength Analyzer.
"""

import argparse
from analyzer.scorer import score_password
from analyzer.crack_time import format_duration


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze password strength using rules and entropy."
    )

    parser.add_argument(
        "--password",
        required=True,
        help="Password to analyze (processed in memory only)."
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format."
    )

    return parser.parse_args()


def print_human_readable(result: dict):
    print(f"Strength: {result['rating']} ({result['score']}/100)")
    print(f"Entropy: {result['entropy_bits']} bits")

    if "crack_time_estimate" in result:
        crack = result["crack_time_estimate"]
        print("\nEstimated Crack Time:")
        print(f"- Offline attack: {format_duration(crack['offline_seconds'])}")
        print(f"- Online attack:  {format_duration(crack['online_seconds'])}")

    if result["issues"]:
        print("\nIssues:")
        for issue in result["issues"]:
            print(f"- {issue}")
    else:
        print("\nNo issues detected.")



def main():
    args = parse_args()
    result = score_password(args.password)

    if args.json:
        import json
        print(json.dumps(result, indent=2))
    else:
        print_human_readable(result)


if __name__ == "__main__":
    main()
