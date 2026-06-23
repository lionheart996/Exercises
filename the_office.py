def happiness_meter():
    employees_happiness = [int(x) for x in input().split()]
    improvement_factor = int(input())

    happiness = [
        employee * improvement_factor
        for employee in employees_happiness
    ]

    avg_happiness = sum(happiness) / len(happiness)

    happy_employees = [
        employee
        for employee in happiness
        if employee >= avg_happiness
    ]

    if len(happy_employees) >= len(happiness) / 2:
        return f"Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!"

print(happiness_meter())



