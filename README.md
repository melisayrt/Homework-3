# Homework-3
![Network Structure](![image](https://github.com/user-attachments/assets/9c6beee3-2dd7-49de-8298-7e7c2fb6e1ae)
)

![Ekran görüntüsü 2025-05-25 140250](https://github.com/user-attachments/assets/efc21e98-b03e-47b0-9a87-34bd58a01294)


📌 Project Overview
This study analyzes different vaccination strategies to prevent disease spread in social networks, comparing their effectiveness through mathematical modeling and simulations.

🔬 Key Components
Optimal Vaccination: Identifying the highest-degree node

Random Vaccination: Basic random selection simulation

Friendship Paradox Strategy: Advanced neighbor-based approach

📂 Files
vaccination_strategies.ipynb: Complete analysis with visualizations

assignment.py: Core vaccination functions

📊 Results
Strategy	Expected Immunized Edges
Random	4.59
Indirect	7.25 (+58% efficacy)
💡 Key Findings
The indirect vaccination strategy proves significantly more effective due to the Friendship Paradox phenomenon, where random neighbors tend to have higher connectivity than random nodes.

🛠️ Implementation Notes
NetworkX library used for graph operations

All code has been executed and verified

Results reproducible with random seed set

To replicate:

from assignment 

import random_vaccine, indirect_random_vaccine
import networkx as nx
G = nx.karate_club_graph()
print(f"Random: {random_vaccine(G):.2f}, Indirect: {indirect_random_vaccine(G):.2f}")
Academic Integrity Statement:
All work is original and completed in accordance with course guidelines. Collaboration references: Friendship Paradox Paper
