def configure_profile(*, username, theme, notifications_on):
    print(f"User: {username} | Theme: {theme} | Alerts: {notifications_on}")

# Order 1: Exactly as defined
configure_profile(username="Bruno", theme="dark", notifications_on=True)

# Order 2: Completely scrambled, but works perfectly fine!
configure_profile(notifications_on=True, theme="dark", username="Bruno")