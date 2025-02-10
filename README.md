# OPTIMIZATION-MODEL

*COMPANY : CODTECHIT SOLUTIONS

*NAME : SWAPNIL SAHU

*INTERN ID : CT08JDB

*DURATION : 4 WEEKS 

*MENTOR : NEELA SANTOSH

# DESCRIPTION OF TASK 

This project focuses on solving a business optimization problem using Linear Programming (LP). The goal is to maximize profit while considering resource constraints such as labor and material availability. The Simplex Method, a well-known optimization algorithm, is applied to determine the optimal number of products to manufacture.

Python’s PuLP library is used for formulating and solving this linear programming problem. The project uses two datasets—one containing product details (profit per unit, material usage, and labor usage) and another defining resource constraints (total available material and labor hours).

Tools and Technologies Used

Programming Language: Python

Python is chosen for its flexibility and rich ecosystem of libraries for optimization and data analysis.
Libraries:

PuLP: A linear programming library used to define the problem, constraints, and solve it using the Simplex method.

Pandas: For handling and processing data from CSV files.

NumPy: Used for efficient numerical computations if needed.

Platform:

The project is implemented in Jupyter Notebook, Google Colab, VS Code, or any Python IDE.
Datasets are stored as CSV files, making them easy to manipulate and analyze.

Project Workflow

Defining the Business Problem:

The company produces two products (Product A and Product B) and wants to maximize its total profit.
However, production is limited by available material and labor hours.

Loading Data:

Two CSV files are used:

business_data.csv: Contains details about the profit per unit, material usage, and labor usage for each product.

business_constraints.csv: Specifies the total available material and labor resources.

Formulating the Linear Program:

Decision Variables: Represent the number of units to produce for Product A and Product B.

Objective Function: The goal is to maximize total profit by producing the optimal number of each product.

Constraints:
Material Constraint: Ensures that total material consumption does not exceed the available supply.

Labor Constraint: Ensures that the total labor hours required do not exceed the available workforce.

Solving the Optimization Problem:

The problem is solved using the Simplex Method provided by PuLP.
The solver determines the optimal number of units for each product that maximizes profit while staying within the resource limits.

Interpreting Results:

The final output includes:
The optimal production quantity for each product.
The maximum possible profit that can be achieved given the constraints.

Real-World Applications

1. Manufacturing Optimization
   
Factories use LP to decide how many units of different products should be manufactured to maximize profit while staying within resource limits.

Example: A car manufacturing company deciding how many sedans and SUVs to produce, given constraints on factory hours and raw materials.

2. Supply Chain & Logistics

Warehouse optimization: Allocating storage space efficiently to maximize inventory turnover.

Shipping optimization: Determining the best routes for product delivery while minimizing transportation costs.

3. Workforce Scheduling
   
LP helps businesses schedule employees efficiently in hospitals, factories, and customer service centers to minimize labor costs while ensuring smooth operations.

4. Agriculture & Farming
   
Farmers use LP to allocate land and resources efficiently among different crops to maximize yield while staying within constraints such as water and fertilizer availability.

5. Financial Portfolio Optimization
   
Investors use LP to allocate funds across different stocks and assets to maximize returns while managing risk constraints.

Conclusion

This project demonstrates how Linear Programming can be applied to real-world business problems using Python. By leveraging the PuLP library, businesses can make data-driven decisions to optimize production, workforce allocation, and resource management. Whether in manufacturing, logistics, workforce planning, or finance, LP provides a structured approach to maximize efficiency and profitability.

# OUTPUT

