def optimize_production(
    extruder_rate=10000,         # meters per hour
    twinner_rate=5000,           # meters of twisted pair per hour
    spool_capacity=20000,        # spool max capacity in meters
    color_change_time=10,        # minutes
    color_change_waste=1000,     # grams of PVC waste per color change
    max_waste_percent=10,        # maximum allowed PVC waste percentage
    pvc_per_meter=3              # grams of PVC per meter
):
    best_result = None

    # Brute-force: check possible production times from 0.1h to 10h
    for white_hours in [i * 0.1 for i in range(1, 100)]:
        for black_hours in [i * 0.1 for i in range(1, 100)]:
            total_hours = white_hours + black_hours
            white_length = white_hours * extruder_rate
            black_length = black_hours * extruder_rate

            usable_length = min(white_length, black_length)
            twinner_needed_hours = usable_length / twinner_rate

            color_changes = 1 if white_hours == 0 or black_hours == 0 else 2
            total_waste = color_changes * color_change_waste

            total_length = white_length + black_length
            total_pvc = total_length * pvc_per_meter
            waste_percent = (total_waste / total_pvc) * 100

            if waste_percent <= max_waste_percent:
                waiting_time = total_hours - twinner_needed_hours
                result = {
                    'white_minutes': int(white_hours * 60),
                    'black_minutes': int(black_hours * 60),
                    'twinner_minutes': int(twinner_needed_hours * 60),
                    'waiting_minutes': int(waiting_time * 60),
                    'waste_percent': round(waste_percent, 2)
                }

                if best_result is None or waiting_time < best_result['waiting_minutes'] / 60:
                    best_result = result

    return best_result


# Example run
result = optimize_production()
print("Optimal production plan:")
print(f"White production time: {result['white_minutes']} minutes")
print(f"Black production time: {result['black_minutes']} minutes")
print(f"Effective twinner running time: {result['twinner_minutes']} minutes")
print(f"Twinner idle time: {result['waiting_minutes']} minutes")
print(f"PVC waste percentage: {result['waste_percent']}%")
