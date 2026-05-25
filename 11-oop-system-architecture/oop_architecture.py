# 🏗️ THE CLASS (The Master Blueprint)
class User:
    def __init__(self, username, email):
        # Enforce Encapsulation: We assign properties directly to the unique instance
        self.username = username
        self.email = email
        self.account_status = "Standard Member"
        
    def display_dashboard_permissions(self):
        """A standard behavior shared by all user objects."""
        print(f"📊 [DASHBOARD] User '{self.username}' holds: {self.account_status} access permissions.")


# 🧬 INHERITANCE (The Specialized Child Blueprint)
# PremiumUser inherits absolutely everything from the generic User class automatically!
class PremiumUser(User):
    def __init__(self, username, email, active_subscription_tier):
        # Call the parent constructor to set up username and email cleanly
        super().__init__(username, email)
        # Add properties unique ONLY to premium accounts
        self.account_status = "VIP Premium Member"
        self.tier = active_subscription_tier
        
    # POLYMORPHISM: We overwrite the exact same method name to make it act differently!
    def display_dashboard_permissions(self):
        print(f"🌟 [PREMIUM DASHBOARD] VIP '{self.username}' unlocked: Unlimited High-Speed Cloud Caching Features ({self.tier} Tier).")


if __name__ == "__main__":
    print("--- 🏗️ Executing Object-Oriented System Architecture Simulation ---")
    
    # 🚗 Stamping out unique OBJECTS from our blueprints
    standard_user_profile = User(username="rahul_dev", email="rahul@example.com")
    premium_user_profile = PremiumUser(username="vinit_99", email="mivi72086@gmail.com", active_subscription_tier="Enterprise 5TB")
    
    print("\n⚡ Triggering Encapsulated Behaviors:")
    # Both profiles look identical from the outside, but they run their own specialized code!
    standard_user_profile.display_dashboard_permissions()
    premium_user_profile.display_dashboard_permissions()