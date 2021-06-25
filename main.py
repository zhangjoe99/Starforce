import numpy as np
from functions import getMatrix, get_costs, translate_goal, translate_result

def calculate(start, goal, level = 160, safeguard = False, event = None, starcatch = False):
    table = getMatrix(safeguard = safeguard, event = event, starcatch = starcatch)

    new_goal = translate_goal(goal)

    A = np.copy(table)
    # Modify table to make goal state the absorbing state
    A = A[0:new_goal+1, 0:new_goal+1]
    A[new_goal] = np.zeros(new_goal+1)
    A[new_goal][new_goal] = 1

    B = np.asmatrix(get_costs(new_goal, level, safeguard = safeguard, event = event))
    B = -B.transpose()

    for i in range(new_goal):
        A[i][i] -= 1

    X = np.linalg.solve(A, B)

    X = translate_result(X)

    print(X)
    return "It will take an expected " + str(float(X[start][0])) + " dollars to go from rank " + str(start) + " to rank " + str(goal)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Parameters (start rank, goal rank, level, event) Add 0 as level if you want to see expected number of steps
    calculate(0, 17, 150, safeguard=False, event=None)
    calculate(0, 17, 150, safeguard=True, event=None)
    calculate(0, 17, 150, safeguard=False, event='fiveten')
    calculate(0, 17, 150, safeguard=True, event='fiveten')
    calculate(0, 17, 160, safeguard=False, event=None)
    calculate(0, 17, 160, safeguard=True, event=None)
    calculate(0, 17, 160, safeguard=False, event='fiveten')
    calculate(0, 17, 160, safeguard=True, event='fiveten')
