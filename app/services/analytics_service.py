from collections import defaultdict
import statistics

def calculate_portfolio_value(assets):
    return sum(asset.price * asset.quantity for asset in assets)

def sector_breakdown(assets):
    breakdown = defaultdict(float)

    for asset in assets:
        breakdown[asset.sector] += asset.price * asset.quantity

    return breakdown

def top_assets(assets):
    sorted_assets = sorted(
        assets,
        key=lambda a: a.price * a.quantity,
        reverse=True
    )
    return sorted_assets[:5]

def portfolio_summary(assets):
    values = [asset.price * asset.quantity for asset in assets]

    total_value = sum(values)

    if len(values) > 1:
        risk = statistics.stdev(values)
    else:
        risk = 0

    return {
        "total_value": total_value,
        "num_assets": len(assets),
        "risk_std_dev": risk
    }
