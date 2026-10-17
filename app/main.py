from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
        for trade in trades:
            for key in trade:
                if trade[key] is not None:
                    trade[key] = Decimal(trade[key])

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trades:
        for key in trade:
            if trade[key] is not None:
                if key == "bought":
                    profit["earned_money"] -= (
                        (trade[key] * trade["matecoin_price"])
                    )
                    profit["matecoin_account"] += trade[key]
                elif key == "sold":
                    profit["earned_money"] += (
                        (trade[key] * trade["matecoin_price"])
                    )
                    profit["matecoin_account"] -= trade[key]

    profit_str = {}
    for key in profit:
        profit_str[key] = str(profit[key])

    with open("profit.json", "w") as file:
        json.dump(profit_str, file, indent=2)
