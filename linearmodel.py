import pulp
import pandas as pd

# DEFINING THE LINEAR PROGRAMMING PROBLEM AS A MAXIMIZATION PROBLEM7
model = pulp.LpProblem("Maximization_Profit",pulp.LpMaximize)

# DEFINING DECISION VARIABLES REPRESENTING THE NUMBER OF UNITS TO PRODUCE FOR EACH PRODUCT
Product_A = pulp.LpVariable("Product_A",lowBound=0, cat = 'Continous')
Product_B = pulp.LpVariable("Product_B",lowBound=0, cat = 'Continous')

# LOADING THE DATASETS CONTAINING PRODUCT INFORMATION AND CONSTRAINTS

# contains product-wise profit and resource usage
data = pd.read_csv(r"C:\Users\mamun\Downloads\business_data.csv")

# contains available resource limits
constraints = pd.read_csv(r"C:\Users\mamun\Downloads\business_constraints.csv")

# EXTRACTING RESOURCE CONSTRAINTS (MATERIAL AND LABOUR AVAILABILITY)
material_limit = constraints.loc[constraints['Constraint'] == 'Material','Limit'].values[0]
labor_limit = constraints.loc[constraints['Constraint'] == 'Labor','Limit'].values[0]

# EXTRACTING PROFIT AND RESOURCE USAGE VALUES FOR EACH PRODUCT
profit_A = data.loc[data['Product'] == 'A', 'Profit'].values[0]
profit_B = data.loc[data['Product'] == 'B', 'Profit'].values[0]
material_A = data.loc[data['Product'] == 'A', 'Material Usage'].values[0]
material_B = data.loc[data['Product'] == 'B', 'Material Usage'].values[0]
labor_A = data.loc[data['Product'] =='A', 'Labor Usage'].values[0]
labor_B = data.loc[data['Product'] =='B', 'Labor Usage'].values[0]

# DEFINING THE OBJECTIVE FUNCTION : MAXIMIZING TOTAL PROFIT
model += profit_A * Product_A + profit_B * Product_B, 'Total Profit'

# DEFINING CONSTRAINTS BASED ON AVAILABLE RESOURCES
model += material_A * Product_A + material_B * Product_B <= material_limit, "Material Constraint"
model += labor_A * Product_A + labor_B * Product_B <= labor_limit, "Labor Constraint"

# SOLVING THE PROBLEM USING THE SIMPLEX METHOD SOLVER
model.solve(pulp.PULP_CBC_CMD(msg=False))

# EXTRACTING OPTIMAL VALUES FOR DECISION VARIABLES
result = {
    "variable" : [var.name for var in model.variables()],
    "optimal value" : [var.varValue for var in model.variables()]
}

result_df = pd.DataFrame(result)

# DISPLAYING THE OPTIMAL PRODUCTION PLAN AND TOTAL PROFIT
print("Optimal Productin Plan:")
print(result_df)
print("\nTotal Profit:",pulp.value(model.objective))
