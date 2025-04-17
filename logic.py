# logic.py

grade_data = {
    "Worker": (3500, 125, 100),
    "Technician": (4500, 360, 150),
    "Specialized Technician": (6000, 600, 200),
    "employee": (7500, 920, 250),
    "Engineer": (9000, 1350, 300)
}

experience_bonus = {
    "5>": 300,
    "5-10": 500,
    "10-20": 1000,
    "20<": 1300
}

marital_bonus = {
    "Célibataire": 200,
    "Marié": 400
}

def calculate_salary(grade, marital, experience, children):
    try:
        base_salary, ir, cnss = grade_data[grade]
        family_bonus = marital_bonus[marital]
        children_bonus = max(0, int(children)) * 300
        experience_value = experience_bonus[experience]

        gross_salary = base_salary + family_bonus + children_bonus + experience_value
        net_salary = gross_salary - (ir + cnss)

        return {
            "base": base_salary,
            "family": family_bonus,
            "children_bonus": children_bonus,
            "experience": experience_value,
            "ir": ir,
            "cnss": cnss,
            "net": net_salary
        }
    except Exception as e:
        print("Calculation error:", e)
        return None
