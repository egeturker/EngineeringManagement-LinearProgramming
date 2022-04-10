import cplex

model = cplex.Cplex()

# Lower bounds for X are set as 0.0 since they can be not included in the regimen.
# The minimum dosages are added as a constraint later
objectiveX = [0.0, 2.0, 0.0, 0.0, 2.0, 1.0, 0.0]
lower_boundsX = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
upper_boundsX = [80.0, 50.0, 100.0, 100.0, 70.0, 90.0, 50.0]
variable_namesX = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']
variable_typesX = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
model.variables.add(obj=objectiveX,
                    lb=lower_boundsX,
                    ub=upper_boundsX,
                    names=variable_namesX,
                    types=variable_typesX)

objectiveY = [0.0, 50.0, 0.0, 0.0, 20.0, 30.0, 0.0]
lower_boundsY = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
upper_boundsY = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
variable_namesY = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7']
variable_typesY = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
model.variables.add(obj=objectiveY,
                    lb=lower_boundsY,
                    ub=upper_boundsY,
                    names=variable_namesY,
                    types=variable_typesY)

objectiveD = [1.0, 1.0, 3.0, 1.0]
lower_boundsD = [0.0, 0.0, 0.0, 0.0]
upper_boundsD = [cplex.infinity, cplex.infinity, cplex.infinity, cplex.infinity]
variable_namesD = ['D1', 'D3', 'D4', 'D7']
variable_typesD = ['C', 'C', 'C', 'C']
model.variables.add(obj=objectiveD,
                    lb=lower_boundsD,
                    ub=upper_boundsD,
                    names=variable_namesD,
                    types=variable_typesD)

objectiveR = [25.0, 10.0, 25.0, 40.0]
lower_boundsR = [0.0, 0.0, 0.0, 0.0]
upper_boundsR = [1.0, 1.0, 1.0, 1.0]
variable_namesR = ['R1', 'R3', 'R4', 'R7']
variable_typesR = ['B', 'B', 'B', 'B']
model.variables.add(obj=objectiveR,
                    lb=lower_boundsR,
                    ub=upper_boundsR,
                    names=variable_namesR,
                    types=variable_typesR)

# The variables T and Tnot are for the if-then constraint.
# Tnot = 1 - T.
objectiveT = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
lower_boundsT = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
upper_boundsT = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
variable_namesT = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7']
variable_typesT = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
model.variables.add(obj=objectiveT,
                    lb=lower_boundsT,
                    ub=upper_boundsT,
                    names=variable_namesT,
                    types=variable_typesT)
objectiveTnot = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
lower_boundsTnot = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
upper_boundsTnot = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
variable_namesTnot = ['T1not', 'T2not', 'T3not', 'T4not', 'T5not', 'T6not', 'T7not']
variable_typesTnot = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
model.variables.add(obj=objectiveTnot,
                    lb=lower_boundsTnot,
                    ub=upper_boundsTnot,
                    names=variable_namesTnot,
                    types=variable_typesTnot)

model.objective.set_sense(model.objective.sense.minimize)

# C_Abs constraints are for the linearization of absolute valued variables.
constraint_names = ["C_Total_Dose",
                    "C_Abs_1_1", "C_Abs_1_2",
                    "C_Abs_3_1", "C_Abs_3_2",
                    "C_Abs_4_1", "C_Abs_4_2",
                    "C_Abs_7_1", "C_Abs_7_2",
                    "CQscore",
                    "CR1", "CR2", "CR3", "CR4"]
constraintTotalDose = [['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
constraintAbs1_1 = [['X1', 'D1'], [-1.0, -1.0]]
constraintAbs1_2 = [['X1', 'D1'], [1.0, -1.0]]
constraintAbs3_1 = [['X3', 'D3'], [-1.0, -1.0]]
constraintAbs3_2 = [['X3', 'D3'], [1.0, -1.0]]
constraintAbs4_1 = [['X4', 'D4'], [-1.0, -1.0]]
constraintAbs4_2 = [['X4', 'D4'], [1.0, -1.0]]
constraintAbs7_1 = [['X7', 'D7'], [-1.0, -1.0]]
constraintAbs7_2 = [['X7', 'D7'], [1.0, -1.0]]
constraintQscore = [['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7',
                     'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7'],
                    [0.28, 0.30, 0.25, 0.17, 0.31, 0.246, 0.40,
                     -5.0, -6.0, -4.0, -4.0, -8.0, -6.0, -7.0]]
constraintR1 = [['R1', 'Y1'], [1.0, 1.0]]
constraintR3 = [['R3', 'Y3'], [1.0, 1.0]]
constraintR4 = [['R4', 'Y4'], [1.0, 1.0]]
constraintR7 = [['R7', 'Y7'], [1.0, 1.0]]

rhs = [250.0, -20.0, 20.0, -30.0, 30.0, -15.0, 15.0, -35.0, 35.0, 49.0, 1.0, 1.0, 1.0, 1.0]
constraint_senses = ["E", "L", "L", "L", "L", "L", "L", "L", "L", "G", "E", "E", "E", "E"]

constraints = [constraintTotalDose,
               constraintAbs1_1, constraintAbs1_2, constraintAbs3_1, constraintAbs3_2,
               constraintAbs4_1, constraintAbs4_2, constraintAbs7_1, constraintAbs7_2,
               constraintQscore,
               constraintR1, constraintR3, constraintR4, constraintR7]
model.linear_constraints.add(lin_expr=constraints,
                             senses=constraint_senses,
                             rhs=rhs,
                             names=constraint_names)

conditional_constraint_names = ["CT1", "CT2", "CT3", "CT4", "CT5", "CT6", "CT7",
                                "CC1_1", "CC1_2", "CC1_3", "CC1_4", "CC1_5", "CC1_6",
                                "CC2_1", "CC2_2", "CC2_3", "CC2_4", "CC2_5", "CC2_6",
                                "CC3_1", "CC3_2", "CC3_3", "CC3_4", "CC3_5", "CC3_6",
                                "CC4_1", "CC4_2", "CC4_3", "CC4_4", "CC4_5", "CC4_6",
                                "CC5_1", "CC5_2", "CC5_3", "CC5_4", "CC5_5", "CC5_6",
                                "CC6_1", "CC6_2", "CC6_3", "CC6_4", "CC6_5", "CC6_6",
                                "CC7_1", "CC7_2", "CC7_3", "CC7_4", "CC7_5", "CC7_6"
                                ]
constraintT1 = [['T1', 'T1not'], [1.0, 1.0]]
constraintT2 = [['T2', 'T2not'], [1.0, 1.0]]
constraintT3 = [['T3', 'T3not'], [1.0, 1.0]]
constraintT4 = [['T4', 'T4not'], [1.0, 1.0]]
constraintT5 = [['T5', 'T5not'], [1.0, 1.0]]
constraintT6 = [['T6', 'T6not'], [1.0, 1.0]]
constraintT7 = [['T7', 'T7not'], [1.0, 1.0]]

constraintConditional1_1 = [['X1', 'T1not'], [1.0, 9999.0]]
constraintConditional1_2 = [['X1', 'T1'], [1.0, -9999.0]]
constraintConditional1_3 = [['Y1', 'T1not'], [-1.0, -9999.0]]
constraintConditional1_4 = [['Y1', 'T1not'], [1.0, -9999.0]]
constraintConditional1_5 = [['Y1', 'T1'], [-1.0, -9999.0]]
constraintConditional1_6 = [['Y1', 'T1'], [1.0, -9999.0]]

constraintConditional2_1 = [['X2', 'T2not'], [1.0, 9999.0]]
constraintConditional2_2 = [['X2', 'T2'], [1.0, -9999.0]]
constraintConditional2_3 = [['Y2', 'T2not'], [-1.0, -9999.0]]
constraintConditional2_4 = [['Y2', 'T2not'], [1.0, -9999.0]]
constraintConditional2_5 = [['Y2', 'T2'], [-1.0, -9999.0]]
constraintConditional2_6 = [['Y2', 'T2'], [1.0, -9999.0]]

constraintConditional3_1 = [['X3', 'T3not'], [1.0, 9999.0]]
constraintConditional3_2 = [['X3', 'T3'], [1.0, -9999.0]]
constraintConditional3_3 = [['Y3', 'T3not'], [-1.0, -9999.0]]
constraintConditional3_4 = [['Y3', 'T3not'], [1.0, -9999.0]]
constraintConditional3_5 = [['Y3', 'T3'], [-1.0, -9999.0]]
constraintConditional3_6 = [['Y3', 'T3'], [1.0, -9999.0]]

constraintConditional4_1 = [['X4', 'T4not'], [1.0, 9999.0]]
constraintConditional4_2 = [['X4', 'T4'], [1.0, -9999.0]]
constraintConditional4_3 = [['Y4', 'T4not'], [-1.0, -9999.0]]
constraintConditional4_4 = [['Y4', 'T4not'], [1.0, -9999.0]]
constraintConditional4_5 = [['Y4', 'T4'], [-1.0, -9999.0]]
constraintConditional4_6 = [['Y4', 'T4'], [1.0, -9999.0]]

constraintConditional5_1 = [['X5', 'T5not'], [1.0, 9999.0]]
constraintConditional5_2 = [['X5', 'T5'], [1.0, -9999.0]]
constraintConditional5_3 = [['Y5', 'T5not'], [-1.0, -9999.0]]
constraintConditional5_4 = [['Y5', 'T5not'], [1.0, -9999.0]]
constraintConditional5_5 = [['Y5', 'T5'], [-1.0, -9999.0]]
constraintConditional5_6 = [['Y5', 'T5'], [1.0, -9999.0]]

constraintConditional6_1 = [['X6', 'T6not'], [1.0, 9999.0]]
constraintConditional6_2 = [['X6', 'T6'], [1.0, -9999.0]]
constraintConditional6_3 = [['Y6', 'T6not'], [-1.0, -9999.0]]
constraintConditional6_4 = [['Y6', 'T6not'], [1.0, -9999.0]]
constraintConditional6_5 = [['Y6', 'T6'], [-1.0, -9999.0]]
constraintConditional6_6 = [['Y6', 'T6'], [1.0, -9999.0]]

constraintConditional7_1 = [['X7', 'T7not'], [1.0, 9999.0]]
constraintConditional7_2 = [['X7', 'T7'], [1.0, -9999.0]]
constraintConditional7_3 = [['Y7', 'T7not'], [-1.0, -9999.0]]
constraintConditional7_4 = [['Y7', 'T7not'], [1.0, -9999.0]]
constraintConditional7_5 = [['Y7', 'T7'], [-1.0, -9999.0]]
constraintConditional7_6 = [['Y7', 'T7'], [1.0, -9999.0]]

conditional_rhs = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0,
                   0.001, 0.0, -1.0, 1.0, 0.0, 0.0]
conditional_senses = ["E", "E", "E", "E", "E", "E", "E",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L",
                      "G", "L", "L", "L", "L", "L"]

conditionalConstraints = [constraintT1, constraintT2, constraintT3, constraintT4,
                          constraintT5, constraintT6, constraintT7,
                          constraintConditional1_1, constraintConditional1_2, constraintConditional1_3,
                          constraintConditional1_4, constraintConditional1_5, constraintConditional1_6,
                          constraintConditional2_1, constraintConditional2_2, constraintConditional2_3,
                          constraintConditional2_4, constraintConditional2_5, constraintConditional2_6,
                          constraintConditional3_1, constraintConditional3_2, constraintConditional3_3,
                          constraintConditional3_4, constraintConditional3_5, constraintConditional3_6,
                          constraintConditional4_1, constraintConditional4_2, constraintConditional4_3,
                          constraintConditional4_4, constraintConditional4_5, constraintConditional4_6,
                          constraintConditional5_1, constraintConditional5_2, constraintConditional5_3,
                          constraintConditional5_4, constraintConditional5_5, constraintConditional5_6,
                          constraintConditional6_1, constraintConditional6_2, constraintConditional6_3,
                          constraintConditional6_4, constraintConditional6_5, constraintConditional6_6,
                          constraintConditional7_1, constraintConditional7_2, constraintConditional7_3,
                          constraintConditional7_4, constraintConditional7_5, constraintConditional7_6]
model.linear_constraints.add(lin_expr=conditionalConstraints,
                             senses=conditional_senses,
                             rhs=conditional_rhs,
                             names=conditional_constraint_names)

lb_constraint_names = ['LB1', 'LB2', 'LB3', 'LB4', 'LB5', 'LB6', 'LB7']

# Lower bounds for the X variables as explained in the first comment
constraintLB1 = [['X1', 'Y1'], [1.0, -20.0]]
constraintLB2 = [['X2', 'Y2'], [1.0, -10.0]]
constraintLB3 = [['X3', 'Y3'], [1.0, -20.0]]
constraintLB4 = [['X4', 'Y4'], [1.0, -10.0]]
constraintLB5 = [['X5', 'Y5'], [1.0, -10.0]]
constraintLB6 = [['X6', 'Y6'], [1.0, -20.0]]
constraintLB7 = [['X7', 'Y7'], [1.0, -20.0]]

lb_rhs = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
lb_senses = ["G", "G", "G", "G", "G", "G", "G"]

lb_constraints = [constraintLB1, constraintLB2, constraintLB3, constraintLB4,
                  constraintLB5, constraintLB6, constraintLB7]
model.linear_constraints.add(lin_expr=lb_constraints,
                             senses=lb_senses,
                             rhs=lb_rhs,
                             names=lb_constraint_names)

objectiveJKL = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
lower_boundsJKL = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
upper_boundsJKL = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
variable_namesJKL = ['J', 'K', 'L', 'Jnot', 'Knot', 'Lnot']
variable_typesJKL = ['B', 'B', 'B', 'B', 'B', 'B']
model.variables.add(obj=objectiveJKL,
                    lb=lower_boundsJKL,
                    ub=upper_boundsJKL,
                    names=variable_namesJKL,
                    types=variable_typesJKL)

partC_constraint_names = []

constraintJ = [['J', 'Jnot'], [1.0, 1.0]]
constraintK = [['K', 'Knot'], [1.0, 1.0]]
constraintL = [['L', 'Lnot'], [1.0, 1.0]]
constraintPartC1_1 = [['Y1', 'Y2', 'K'], [1.0, 1.0, -9999.0]]
constraintPartC1_2 = [['X1', 'X2', 'Knot'], [1.0, 1.0, -9999.0]]
constraintPartC1_3 = [['X1', 'X2', 'Knot'], [1.0, 1.0, -9999.0]]
constraintPartC2_1 = [['X3', 'L'], [1.0, -9999.0]]
constraintPartC2_2 = [['Y5', 'Lnot'], [-1.0, -9999.0]]
constraintPartC3_1 = [['Y4', 'Y6', 'J'], [1.0, 1.0, -9999.0]]
constraintPartC3_2 = [['Y5', 'Y7', 'Jnot'], [-1.0, -1.0, -9999.0]]

partC_rhs = [1.0, 1.0, 1.0,
             1.0, 50.0, 70.0,
             25.0, -1.0,
             1.0, -1.0]
partC_senses = ["E", "E", "E",
                "L", "L", "L",
                "L", "L",
                "L", "L"]

partC_constraints = [constraintJ, constraintK, constraintL,
                     constraintPartC1_1, constraintPartC1_2, constraintPartC1_3,
                     constraintPartC2_1, constraintPartC2_2,
                     constraintPartC3_1, constraintPartC3_2]
model.linear_constraints.add(lin_expr=partC_constraints,
                             senses=partC_senses,
                             rhs=partC_rhs,
                             names=partC_constraint_names)

model.solve()
print("Obj Value:", model.solution.get_objective_value())
print("Values of Decision Variables:", model.solution.get_values())
print(model.variables.get_names())


