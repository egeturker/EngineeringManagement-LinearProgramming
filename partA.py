import cplex

model = cplex.Cplex()

objective = [0.28, 0.25, 0.17, 0.4]
lower_bounds = [20.0, 20.0, 10.0, 20.0]
upper_bounds = [80.0, 100.0, 100.0, 50.0]
variable_names = ['X1', 'X3', 'X4', 'X7']
variable_types = ['C', 'C', 'C', 'C']

model.variables.add(obj=objective,
                    lb=lower_bounds,
                    ub=upper_bounds,
                    names=variable_names,
                    types=variable_types)

model.objective.set_sense(model.objective.sense.maximize)

constraint_names = ["C1"]
constraint1 = [['X1', 'X3', 'X4', 'X7'], [1.0, 1.0, 1.0, 1.0]]

rhs = [100.0]
constraint_senses = ["E"]

constraints = [constraint1]
model.linear_constraints.add(lin_expr=constraints,
                             senses=constraint_senses,
                             rhs=rhs,
                             names=constraint_names)
model.solve()
print("Obj Value:", model.solution.get_objective_value())
print("Values of Decision Variables:", model.solution.get_values())
