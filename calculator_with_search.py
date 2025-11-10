# calculator_with_search.py
# Smart Calculator with Equation Solver
# Uses search concepts from Chapter 3
import operator
import math
class SmartCalculator:
    """
    A calculator that can solve simple equations using search
    """
    def __init__(self):
        # Let Copilot help: Write a comment describing what you want
        # Example: "# Create a dictionary of basic math operations"
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

    def basic_calculate(self, num1, op, num2):
        """
        Perform basic calculation
        Let Copilot complete this function
        """
        # Type this comment and see what Copilot suggests:
        # Check if operation is valid and perform calculation
        if op in self.operations:
            return self.operations[op](num1, num2)
        raise ValueError(f"Invalid operation: {op}")

    def solve_for_x(self, target, operation, known_value, x_position='left'):
        """
        Solve simple equations like: x + 5 = 10 or 3 * x = 15
        Uses a simple search approach to find x
        """
        # This demonstrates a brute-force search
        # We'll try different values of x until we find the answer
        # Search range
        min_x = -100
        max_x = 100
        step = 0.1
        # Let Copilot help complete the search logic
        # Type: "# Search for x value that satisfies the equation"
        current_x = min_x
        best_x = None
        best_difference = float('inf')
        
        while current_x <= max_x:
            # Calculate result with current x
            if x_position == 'left':
                result = self.operations[operation](current_x, known_value)
            else:
                result = self.operations[operation](known_value, current_x)
            
            # Check if we found exact answer
            difference = abs(result - target)
            if difference < 0.0001:  # Close enough!
                return current_x
                
            # Track best answer so far
            if difference < best_difference:
                best_difference = difference
                best_x = current_x
            current_x += step
            
        return best_x

    def equation_solver_menu(self):
        """
        Interactive menu for equation solving
        """
        print("\n" + "="*50)
        print("EQUATION SOLVER (using search)")
        print("="*50)
        print("I can solve equations like:")
        print(" x + 5 = 10")
        print(" x * 3 = 15")
        print(" 10 - x = 7")
        print(" 20 / x = 4")
        
        while True:
            print("\nEnter equation (or 'quit' to exit):")
            equation = input().strip()
            
            if equation.lower() == 'quit':
                break
                
            # Parse equation parts (assuming format: "a op b = c")
            try:
                left, right = equation.split('=')
                left = left.strip()
                right = right.strip()
                target = float(right)
                
                # Find x position and operation
                if 'x' in left:
                    parts = left.split()
                    if parts[0] == 'x':
                        x_position = 'left'
                        operation = parts[1]
                        known_value = float(parts[2])
                    else:
                        x_position = 'right'
                        operation = parts[1]
                        known_value = float(parts[0])
                        
                    x = self.solve_for_x(target, operation, known_value, x_position)
                    print(f"\nSolution: x = {x}")
                    
                    # Verify the solution
                    if x_position == 'left':
                        result = self.operations[operation](x, known_value)
                    else:
                        result = self.operations[operation](known_value, x)
                    print(f"Verification: {result} ≈ {target}")
                    
            except Exception as e:
                print(f"Error: {str(e)}")
                print("Please use format like 'x + 5 = 10' or '3 * x = 15'")

    def visualize_search(self, target, operation, known_value, x_position='left'):
        """
        Show the search process step by step
        This helps understand how search algorithms explore possibilities
        """
        print("\n🔍 SEARCHING FOR SOLUTION...")
        print(f"Goal: Find x where ", end="")
        if x_position == 'left':
            print(f"x {operation} {known_value} = {target}")
        else:
            print(f"{known_value} {operation} x = {target}")
            
        # Show first few search steps
        test_values = [-10, -5, 0, 5, 10, 15, 20]
        print("\nTesting values:")
        print("-" * 40)
        for x in test_values:
            if x_position == 'left':
                result = self.operations[operation](x, known_value)
            else:
                result = self.operations[operation](known_value, x)
            distance = abs(result - target)
            print(f"x = {x:4}: {result:6.2f} | Distance from target: {distance:6.2f}")
def main():
    """
    Main program loop
    """
    calc = SmartCalculator()
    while True:
        print("\n" + "="*50)
        print("🤖 SMART CALCULATOR WITH AI ASSISTANCE")
        print("="*50)
        print("1. Basic Calculation")
        print("2. Solve Equation (using search)")
        print("3. See Search Visualization")
        print("4. About Search Algorithms")
        print("5. Exit")
        
        choice = input("\nChoose option (1-5): ")
        
        if choice == '1':
            # Basic calculation
            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operation (+, -, *, /, ^): ")
                num2 = float(input("Enter second number: "))
                result = calc.basic_calculate(num1, op, num2)
                print(f"\nResult: {num1} {op} {num2} = {result}")
            except Exception as e:
                print(f"Error: {str(e)}")
        
        elif choice == '2':
            # Equation solver
            calc.equation_solver_menu()
        
        elif choice == '3':
            # Visualization demo
            print("\nLet's solve: x + 5 = 12")
            result = calc.visualize_search(12, '+', 5, 'left')
            print(f"\nSolution: x = {result}")
        
        elif choice == '4':
            print("\n📚 ABOUT SEARCH ALGORITHMS")
            print("-" * 40)
            print("This calculator uses a simple linear search:")
            print("• It tries different values of x")
            print("• Checks if each value solves the equation")
            print("• Keeps track of the best answer")
            print("• This is similar to 'brute force' search")
            print("\nReal search algorithms (Chapter 3) are smarter:")
            print("• BFS: Explores all possibilities level by level")
            print("• DFS: Explores one path deeply before trying others")
            print("• A*: Uses heuristics to search more efficiently")
        
        elif choice == '5':
            print("\nThanks for using Smart Calculator! 👋")
            break
            
if __name__ == "__main__":
    main()