import sys
from robust_division_calculator import safe_divide

def main():
    """
    Command-line interface for the robust division calculator.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform safe division
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
