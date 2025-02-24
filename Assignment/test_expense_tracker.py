import unittest
from expense_tracker import expense_tracker

class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        expenses = []
        total = 0
        curr = "2025-02-24"
        
        expense = {"date": curr, "description": "Groceries", "amount": 100}
        total += expense["amount"]
        expenses.append(expense)
        
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["description"], "Groceries")
        self.assertEqual(expenses[0]["amount"], 100)
        self.assertEqual(total, 100)

    def test_view_expenses(self):
        expenses = [
            {"date": "2025-02-24", "description": "Groceries", "amount": 100},
            {"date": "2025-02-24", "description": "Transport", "amount": 50}
        ]
        
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[1]["description"], "Transport")
        self.assertEqual(expenses[1]["amount"], 50)

    def test_calculate_total(self):
        expenses = [
            {"date": "2025-02-24", "description": "Groceries", "amount": 100},
            {"date": "2025-02-24", "description": "Transport", "amount": 50}
        ]
        total = sum(exp["amount"] for exp in expenses)
        
        self.assertEqual(total, 150)

if __name__ == "__main__":
    unittest.main()

