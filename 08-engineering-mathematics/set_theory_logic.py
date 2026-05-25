# 📊 Defining our two distinct mathematical sets of user IDs
ordered_food_this_week = {"vinit_99", "amit_coder", "rohit_max", "sneha_dev"}
premium_subscribers = {"vinit_99", "sneha_dev", "rahul_ops", "pooja_tech"}

if __name__ == "__main__":
    print("--- 📐 Running SQL Set Theory Simulator ---")
    print(f"Set A (Ordered Food):       {ordered_food_this_week}")
    print(f"Set B (Premium Members):     {premium_subscribers}")
    print("-" * 50)
    
    # 1. INTERSECTION (∩) -> The Overlap (Database INNER JOIN)
    # Target: Users who are BOTH premium AND ordered food.
    premium_orders = ordered_food_this_week.intersection(premium_subscribers)
    print(f"🎯 Intersection (A ∩ B) | Target Marketing Pool:")
    print(f"   ↳ {premium_orders}  <-- Only the overlapping matches!")
    
    # 2. UNION (∪) -> Combined Unique Space (Database UNION)
    # Target: Every single unique active customer across both lists.
    total_unique_customers = ordered_food_this_week.union(premium_subscribers)
    print(f"\n📢 Union (A ∪ B) | All Unique Active Customers:")
    print(f"   ↳ {total_unique_customers}  <-- Duplicates are mathematically filtered out.")
    
    # 3. DIFFERENCE (-) -> Left-Side Exclusivity (Database LEFT JOIN / EXCEPT)
    # Target: Standard users who ordered food but do NOT have premium yet (Perfect for upselling!)
    standard_users_to_target = ordered_food_this_week.difference(premium_subscribers)
    print(f"\n💎 Difference (A - B) | Food Orderers who are NOT Premium:")
    print(f"   ↳ {standard_users_to_target}  <-- Perfect group for a premium trial pitch!")