from model import predict_recovery

cases = [
    {"id": 101, "amount": 15000, "days": 20},
    {"id": 102, "amount": 4000, "days": 70}
]

for case in cases:
    priority = predict_recovery(case["amount"], case["days"])
    print(f"Case {case['id']} → Priority: {priority}")

