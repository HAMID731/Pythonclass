current_population = 8000000000
growth_rate = 0.0105  
double_population = current_population * 2
quadruple_population = current_population * 4
double_population_reached = False

print(f"{'Year':<5} {'Population':<25} {'Annual Increase':<20}")

for year in range(1, 101):
    annual_increase = current_population * growth_rate
    current_population += annual_increase
    print(f"{year:<5} {current_population:<25.2f} {annual_increase:<20.2f}")

    if double_population_reached == False and current_population >= double_population:
        print("Population doubles by year:", year)
        double_population_reached = True

    if current_population >= quadruple_population:
        print("Population quadruples by year:", year)
        break
