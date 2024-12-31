import csv
import pandas as pd
import matplotlib.pyplot as plt

class FinanceApp:
    def __init__(self):
        self.transactions = []

    def load_csv(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.transactions = [row for row in reader]
                for transaction in self.transactions:
                    transaction['amount'] = float(transaction['amount'])  # Convert amount to float
            print(f"Data loaded successfully from {filename}")
        except Exception as e:
            print(f"Error loading file: {e}")

    def add_income(self, amount, category, description):
        self.transactions.append({
            'type': 'Income',
            'amount': amount,
            'category': category,
            'description': description
        })

    def add_expense(self, amount, category, description):
        self.transactions.append({
            'type': 'Expense',
            'amount': amount,
            'category': category,
            'description': description
        })

    def view_summary(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        balance = total_income - total_expenses

        print("\n--- Financial Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}\n")

    def export_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['type', 'amount', 'category', 'description'])
            writer.writeheader()
            writer.writerows(self.transactions)

        print(f"Data exported to {filename}")

    def generate_tips(self, total_income, total_expenses, largest_income, largest_expense):
        print("\n--- Financial Tips ---")
        if total_income < total_expenses:
            print("1. Your expenses exceed your income. Consider reducing discretionary spending or finding additional income sources.")
        else:
            print("1. Great job keeping expenses below income! Try to allocate some savings for emergencies or investments.")

        if largest_expense['amount'] > 0.3 * total_income:
            print("2. Your largest expense is significant. Look for ways to minimize costs in this category.")
        else:
            print("2. Your largest expense is within a reasonable range. Keep monitoring to ensure it stays manageable.")

        if total_income - total_expenses < 0.2 * total_income:
            print("3. Your savings margin is low. Consider creating a stricter budget to increase your savings.")

        print("4. Always track your finances regularly to spot trends and adjust your spending habits as needed.")

    def analyze_transactions(self):
        df = pd.DataFrame(self.transactions)

        if df.empty:
            print("\nNo transactions to analyze.")
            return

        # Separate income and expenses
        income = df[df['type'] == 'Income']
        expenses = df[df['type'] == 'Expense']

        # Income Analysis
        if not income.empty:
            total_income = income['amount'].sum()
            income_category_totals = income.groupby('category')['amount'].sum()
            largest_income = income.loc[income['amount'].idxmax()]

            print("\n--- Income Analysis ---")
            print("Income by Category:")
            print(income_category_totals)

            # Plot income data as a pie chart
            income_category_totals.plot(kind='pie', title='Income by Category', autopct='%1.1f%%', ylabel='', startangle=90, colors=plt.cm.Paired.colors)
            plt.axis('equal')  # Ensure pie chart is a circle
            plt.tight_layout()
            plt.show()

            print("\nLargest Single Income:")
            print(f"Amount: ${largest_income['amount']:.2f}")
            print(f"Category: {largest_income['category']}")
            print(f"Description: {largest_income['description']}")
        else:
            total_income = 0
            largest_income = {'amount': 0}

        # Expense Analysis
        if not expenses.empty:
            total_expenses = expenses['amount'].sum()
            expense_category_totals = expenses.groupby('category')['amount'].sum()
            largest_expense = expenses.loc[expenses['amount'].idxmax()]

            print("\n--- Expense Analysis ---")
            print("Expenses by Category:")
            print(expense_category_totals)

            # Plot expense data as a pie chart
            expense_category_totals.plot(kind='pie', title='Expenses by Category', autopct='%1.1f%%', ylabel='', startangle=90, colors=plt.cm.Paired.colors)
            plt.axis('equal')  # Ensure pie chart is a circle
            plt.tight_layout()
            plt.show()

            print("\nLargest Single Expense:")
            print(f"Amount: ${largest_expense['amount']:.2f}")
            print(f"Category: {largest_expense['category']}")
            print(f"Description: {largest_expense['description']}")
        else:
            total_expenses = 0
            largest_expense = {'amount': 0}

        # Generate tips based on analysis
        self.generate_tips(total_income, total_expenses, largest_income, largest_expense)

    def run(self):
        while True:
            print("\n--- Finance App ---")
            print("1. Load CSV")
            print("2. Add Income")
            print("3. Add Expense")
            print("4. View Summary")
            print("5. Export to CSV")
            print("6. Analyze Transactions")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                filename = input("Enter CSV filename to load: ")
                self.load_csv(filename)

            elif choice == '2':
                amount = float(input("Enter income amount: "))
                category = input("Enter income category: ")
                description = input("Enter description: ")
                self.add_income(amount, category, description)

            elif choice == '3':
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)

            elif choice == '4':
                self.view_summary()

            elif choice == '5':
                filename = input("Enter filename to export (e.g., data.csv): ")
                self.export_to_csv(filename)

            elif choice == '6':
                self.analyze_transactions()

            elif choice == '7':
                print("Exiting the app. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FinanceApp()
    app.run()
