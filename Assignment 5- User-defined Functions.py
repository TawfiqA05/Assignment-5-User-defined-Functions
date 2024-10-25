def state_with_highest_death_increase(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    death_increase = {}

    for line in lines:
        data = line.strip().split(',')
        state = data[1]
        try:
            deaths = int(data[10])
        except ValueError:
            deaths = 0

        if state in death_increase:
            death_increase[state] += deaths
        else:
            death_increase[state] = deaths

    max_state = max(death_increase, key=death_increase.get)
    return max_state, death_increase[max_state]

# Example usage
file_path = "/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv"
state, deaths = state_with_highest_death_increase(file_path)
print(f"The state with the highest death increase is {state} with {deaths} deaths.")