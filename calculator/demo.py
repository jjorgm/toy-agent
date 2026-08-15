#!/usr/bin/env python3

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output

def demo():
    calculator = Calculator()
    
    # Test expressions
    test_expressions = [
        "3 + 5",
        "10 - 4",
        "6 * 7",
        "20 / 4",
        "2 ^ 3",  # This will cause an error as ^ is not supported
        "15 + 2 * 3",  # This will test operator precedence
    ]
    
    print("Calculator Demo")
    print("=" * 40)
    
    for expr in test_expressions:
        print(f"\nExpression: {expr}")
        try:
            result = calculator.evaluate(expr)
            if result is not None:
                formatted_output = format_json_output(expr, result)
                print("Result:")
                print(formatted_output)
            else:
                print("Error: Invalid expression")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    demo()