def predict_recovery(amount, days_overdue):
    if amount > 10000 and days_overdue < 30:
        return "High"
    elif days_overdue < 60:
        return "Medium"
    else:
        return "Low"

