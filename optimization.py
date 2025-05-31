import pandas as pd

def production_scenario_table(
    extruder_rate=10000,
    twinner_rate=5000,
    spool_capacity=20000,
    color_change_time=10,
    color_change_waste=1000,
    max_waste_percent=10,
    pvc_per_meter=3
):
    records = []

    # Iterate from 10h down to 0.1h in 0.1h steps
    for white_hours in [i * 0.1 for i in range(100, 0, -1)]:
        for black_hours in [i * 0.1 for i in range(100, 0, -1)]:
            white_minutes = int(white_hours * 60)
            black_minutes = int(black_hours * 60)
            total_extruder_minutes = white_minutes + color_change_time + black_minutes

            white_length = white_hours * extruder_rate
            black_length = black_hours * extruder_rate
            usable_length = min(white_length, black_length)
            twinner_minutes = int((usable_length / twinner_rate) * 60)

            color_changes = 1 if white_hours == 0 or black_hours == 0 else 2
            total_waste = color_changes * color_change_waste
            total_pvc = (white_length + black_length) * pvc_per_meter + total_waste
            waste_percent = (total_waste / total_pvc) * 100

            # Calculate twinner waiting time accurately
            twinner_start = white_minutes + color_change_time + black_minutes
            extruder_end = total_extruder_minutes
            waiting_time = max(0, twinner_start - extruder_end)

            records.append({
                'White (min)': white_minutes,
                'Black (min)': black_minutes,
                'Twinner (min)': twinner_minutes,
                'Twinner Idle (min)': waiting_time,
                'PVC Waste (%)': round(waste_percent, 2)
            })

    df = pd.DataFrame(records)
    return df

# Usage example
df = production_scenario_table()
print(df.head())
df.to_excel('production_scenarios.xlsx', index=False)

