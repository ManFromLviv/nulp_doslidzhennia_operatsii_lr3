import pulp
from scipy.optimize import linprog

# Відключення виводу від CBC MILP Solver
pulp.LpSolverDefault.msg = False

def maximize_func():
    # Створення моделі задачі лінійного програмування для максимізації
    model_max = pulp.LpProblem("maximization_problem", pulp.LpMaximize)

    # Оголошення змінних рішення
    x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuous')
    x4 = pulp.LpVariable("x4", lowBound=0, cat='Continuous')

    # Оголошення функції цілі
    obj_func = -40 * x1 + 10 * x2 - 60 * x3 - 14 *x4
    model_max += obj_func

    # Оголошення обмежень
    model_max += -8 * x1 - 2 * x2 + 6 * x3 - 2 * x4 <= 3
    model_max += 5 * x1 + 5 * x2 - 5 * x3 - 1 * x4 <= 4

    # Розв'язання задачі лінійного програмування
    model_max.solve()

    # Збереження результатів задачі на максимізацію
    max_value = pulp.value(model_max.objective)
    maximizer = [pulp.value(x1), pulp.value(x2), pulp.value(x3), pulp.value(x4)]
    return [max_value, maximizer]

def minimize_func():
    # Створення моделі задачі лінійного програмування для мінімізації
    model_min = pulp.LpProblem("minimization_problem", pulp.LpMinimize)

    # Оголошення змінних рішення
    y1 = pulp.LpVariable("y1", lowBound=0, cat='Continuous')
    y2 = pulp.LpVariable("y2", lowBound=0, cat='Continuous')
    y3 = pulp.LpVariable("y3", lowBound=0, cat='Continuous')
    y4 = pulp.LpVariable("y4", lowBound=0, cat='Continuous')

    # Оголошення функції цілі
    obj_func = 40 * y1 - 10 * y2 + 60 * y3 + 14 * y4
    model_min += obj_func

    # Оголошення обмежень
    model_min += 8 * y1 - 2 * y2 - 6 * y3 + 2 * y4 >= 3
    model_min += -5 * y1 - 5 * y2 + 5 * y3 + y4 >= 4

    # Розв'язання задачі лінійного програмування
    model_min.solve()

    # Збереження мінімізування
    min_value = pulp.value(model_min.objective)
    minimizer = [pulp.value(y1), pulp.value(y2), pulp.value(y3), pulp.value(y4)]
    return [min_value, minimizer]

if __name__ == "__main__":
    max_values = maximize_func()
    min_values = minimize_func()

    # Виведення результатів розв'язку
    print("Програму розробив Вальчевський П., студент групи ОІ-11 сп для ЛР № 3 з ДО")
    print("=" * 60)
    print("Maximum value:", max_values[0])
    print("Variables:", max_values[1])
    print("=" * 60)
    print("Minimum value:", min_values[0])
    print("Variables:", min_values[1])
