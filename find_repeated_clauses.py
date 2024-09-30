import sys

# Read line by line

clauses = []

for line in sys.stdin:
    if not line.startswith("["):
        continue
    clause = line.strip().replace("[", "").replace("]", "").replace(",", "").split()
    clauses.append(clause)

# Find repeated clauses
repeated_clauses = []
for i in range(len(clauses)):
    for j in range(i + 1, len(clauses)):
        if clauses[i] == clauses[j]:
            repeated_clauses.append(clauses[i])

# Print repeated clauses
for clause in repeated_clauses:
    print(clause)