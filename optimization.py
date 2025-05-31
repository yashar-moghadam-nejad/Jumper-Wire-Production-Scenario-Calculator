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
    for white_spool_count in [i  for i in range(5, 0, -1)]:
        for black_spool_count in [i  for i in range(1, 0, -1)]:
            white_minutes = int(((white_spool_count * spool_capacity)/extruder_rate)*60)
            black_minutes = int(((black_spool_count * spool_capacity)/extruder_rate)*60)
            total_extruder_minutes = white_minutes + color_change_time + black_minutes

            white_length = (white_minutes/60) * extruder_rate
            black_length = (black_minutes/60) * extruder_rate
            usable_length = min(white_length, black_length)
            twinner_time = int(usable_length / twinner_rate)

            total_pvc = ((white_length + black_length) * pvc_per_meter) + color_change_waste
            waste_percent = (color_change_waste / total_pvc) * 100

            # Calculate twinner waiting time accurately 
            waiting_time = round((white_minutes + color_change_time + black_minutes)/60,2)

            records.append({
                'White spool count': white_spool_count,
                'Black spool count': black_spool_count,
                'Twinner working time ': twinner_time,
                'Twinner Idle (min)': waiting_time,
                'PVC Waste (%)': round(waste_percent, 2)
            })

    df = pd.DataFrame(records)
    return df

# Usage example
df = production_scenario_table()
print(df.head())
df.to_excel('production_scenarios.xlsx', index=False)

