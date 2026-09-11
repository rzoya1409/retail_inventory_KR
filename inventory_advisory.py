import json


class RetailInventorySystem:
    def __init__(self, knowledge_file):
        with open(knowledge_file, "r", encoding="utf-8") as file:
            self.knowledge_base = json.load(file)

    def compare_values(self, actual_value, operator, expected_value):
        """
        Performs comparison according to the operator in the rule.
        """
        if operator == "<=":
            return actual_value <= expected_value

        if operator == ">=":
            return actual_value >= expected_value

        if operator == "<":
            return actual_value < expected_value

        if operator == ">":
            return actual_value > expected_value

        if operator == "==":
            return actual_value == expected_value

        return False

    def rule_matches(self, rule, facts):
        """
        Checks whether all conditions of a rule are satisfied.
        """
        for condition in rule["conditions"]:
            field = condition["field"]
            operator = condition["operator"]
            actual_value = facts[field]

            if "value_field" in condition:
                expected_value = facts[condition["value_field"]]
            else:
                expected_value = condition["value"]

            if not self.compare_values(actual_value, operator, expected_value):
                return False

        return True

    def resolve_knowledge(self, rule_category, facts):
        """
        Uses forward chaining to identify rules that match the facts.
        """
        fired_rules = []

        for rule in self.knowledge_base[rule_category]:
            if self.rule_matches(rule, facts):
                fired_rules.append(rule)

        return fired_rules

    def display_results(self, heading, results):
        print("\n" + "=" * 72)
        print(heading)
        print("=" * 72)

        if not results:
            print("No rule was fired for this category.")
            return

        for result in results:
            print("\nRule Fired :", result["rule_name"])
            print("Decision   :", result["decision"])
            print("Reason     :", result["reason"])


def main():
    print("=" * 72)
    print("      RETAIL INVENTORY AND REORDER MANAGEMENT SYSTEM")
    print("=" * 72)

    system = RetailInventorySystem("knowledge_base.json")

    # Instantiated facts entered by the store manager
    facts = {
        "product_name": input("\nEnter product name: ").strip(),
        "current_stock": int(input("Enter current stock quantity: ")),
        "reorder_level": int(input("Enter reorder level: ")),
        "daily_sales_rate": int(input("Enter average daily sales quantity: ")),
        "days_until_expiry": int(input("Enter days until expiry: ")),
        "days_since_last_sale": int(input("Enter days since last sale: "))
    }

    print("\nProduct Name:", facts["product_name"])

    inventory_results = system.resolve_knowledge("inventory_rules", facts)
    expiry_results = system.resolve_knowledge("expiry_rules", facts)
    sales_results = system.resolve_knowledge("sales_rules", facts)

    system.display_results("INVENTORY AND REORDER DECISION", inventory_results)
    system.display_results("EXPIRY MANAGEMENT DECISION", expiry_results)
    system.display_results("SALES AND PROMOTION DECISION", sales_results)

    print("\n" + "=" * 72)
    print("This is an educational knowledge-based business-system prototype.")
    print("Actual inventory decisions should also consider supplier lead time,")
    print("demand forecasting, storage capacity, seasonal demand, and finance.")
    print("=" * 72)


if __name__ == "__main__":
    main()