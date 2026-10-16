"""Demo: strangler fig - traffic gradually shifts from legacy to new system."""
from framework.gateway import StranglerGateway


def main():
    gw = StranglerGateway(new_traffic_ratio=0.0)

    print("--- Stage 1: 100% legacy ---")
    counts = {"legacy": 0, "new": 0}
    for i in range(100):
        r = gw.route(f"req-{i}")
        counts[r["backend"]] += 1
    print(f"  traffic split: legacy={counts['legacy']}, new={counts['new']}")

    print("\n--- Stage 2: 20% new (canary) ---")
    gw.set_ratio(0.2)
    counts = {"legacy": 0, "new": 0}
    for i in range(100):
        r = gw.route(f"req-{i}")
        counts[r["backend"]] += 1
    print(f"  traffic split: legacy={counts['legacy']}, new={counts['new']}")

    print("\n--- Stage 3: 50/50 ---")
    gw.set_ratio(0.5)
    counts = {"legacy": 0, "new": 0}
    for i in range(100):
        r = gw.route(f"req-{i}")
        counts[r["backend"]] += 1
    print(f"  traffic split: legacy={counts['legacy']}, new={counts['new']}")

    print("\n--- Stage 4: 100% new, legacy strangled ---")
    gw.set_ratio(1.0)
    counts = {"legacy": 0, "new": 0}
    for i in range(100):
        r = gw.route(f"req-{i}")
        counts[r["backend"]] += 1
    print(f"  traffic split: legacy={counts['legacy']}, new={counts['new']}")

    print("\n== all stages done ==")


if __name__ == "__main__":
    main()
