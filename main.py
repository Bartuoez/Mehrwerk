import pandas as pd
from collections import defaultdict

"""
    The Function calculates basic process mining KPIs from an event log file.

    Parameters:
        filename (str): The path to the event log.

    The KPIs include:
    - Number of events (# Events)
    - Number of cases (# Cases)
    - Number of unique activities (# Activities)
    - Number of process variants (# Variants)
    """


def process_mining_kpis(filename):
    # Load the event log CSV file
    event_log_df = pd.read_csv(filename, sep=';')

    # Calculation of the Number of Events (rows in the file)
    num_events = len(event_log_df)

    # Calculation of the number of unique cases based on the 'Case' column
    num_cases = event_log_df['Case'].nunique()

    # Calculation the number of unique activities based on the 'Activity' column
    num_activities = event_log_df['Activity'].nunique()

    # Find out the process variants and count occurrences of each variant
    case_variants = defaultdict(list)
    variant_counts = defaultdict(int)
    for case, activities in event_log_df.sort_values(['Case', 'Timestamp']).groupby('Case')['Activity']:
        # Join all activities of a case into a sequence
        variant = '-'.join(activities.tolist())
        case_variants[case] = variant
        # Count each variant occurrence
        variant_counts[variant] += 1

    # Calculation of the number of unique variants (activity sequences)
    num_variants = len(set(case_variants.values()))

    # Results Printing
    print(f"# Events:     {num_events}")
    print(f"# Cases:      {num_cases}")
    print(f"# Activities: {num_activities}")
    print(f"# Variants:   {num_variants}")
    print(f"# Variants:   {num_variants}")

    # Printing each variant with its count
    print("Process Variants and their counts:")
    for variant, count in variant_counts.items():
        print(f"{variant}: {count} Case(s)")


# Function Call with the Event log
process_mining_kpis('bookstore.csv')
