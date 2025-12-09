import os
import sys
import statistics

def parse_scores_from_string(s: str):
    """Parse a string of comma/space separated numbers into a list of floats."""
    parts = [p.strip() for p in s.replace(',', ' ').split()]
    scores = []
    for p in parts:
        if not p:
            continue
        try:
            scores.append(float(p))
        except ValueError:
            print(f"Warning: skipping non-numeric token: {p}")
    return scores

def read_scores():
    """
    Read scores from one of several sources, in priority order:
    1. Command-line arguments
    2. SCORES environment variable
    3. scores.txt file
    4. Interactive prompt
    """
    if len(sys.argv) > 1:
        return parse_scores_from_string(" ".join(sys.argv[1:]))

    env = os.getenv("SCORES")
    if env:
        return parse_scores_from_string(env)

    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r", encoding="utf-8") as f:
            return parse_scores_from_string(f.read())

    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()
    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    total = sum(scores)
    avg = total / len(scores)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {total:.2f}")
    print(f"Average: {avg:.2f}")
    print(f"Min: {min(scores):.2f}")
    print(f"Max: {max(scores):.2f}")
    print(f"Median: {statistics.median(scores):.2f}")

if __name__ == "__main__":
    main()
