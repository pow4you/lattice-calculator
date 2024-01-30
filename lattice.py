import matplotlib.pyplot as plt
import numpy as np
import pickle
import threading



def generate_grid(basis_vectors, check_vectors, modulo):
    visited = []
    grid = []

    for vector in basis_vectors:
        visited.append(tuple(vector % modulo for vector in vector))
        grid.append(tuple(vector % modulo for vector in vector))


    iteration = 0
    while True:
        new_grid = []

        # Spawn multiple threads to generate new points
        for vector in grid:
            for other_vector in basis_vectors:
                new_point = tuple((vector[i] + other_vector[i]) % modulo for i in range(len(vector)))

                # Check if the new point has already been visited
                if new_point not in visited:
                    visited.append(new_point)
                    new_grid.append(new_point)
        
        
        if len(new_grid) <= 0:
            break

        grid.extend(new_grid)
        
        prooven = [is_in_grid(vector,grid) for vector in check_vectors]
        if all(prooven):
            break
        
        
        iteration += 1
        print("iteration:", iteration, "points_visited:", len(new_grid), prooven )
        with open('iterations/i_'+str(iteration)+'_grid.pickle', 'wb') as handle:
            pickle.dump(grid, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return grid




def is_in_grid(vector, grid):
    if vector in grid:
        return True
    return False


## Visualize
def plot4d(grid, check_vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z, c = zip(*grid)
    
    q, w, e, r = zip(*check_vectors)

    img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
    ax.scatter(q,w,e, c=r, cmap=plt.hot(), marker ='^')
    
    
    fig.colorbar(img)
    plt.show()
    
if __name__ == "__main__":
    modulo = 23
    basis_vectors = [(1,4,5,7), (4,4,6,5), (5,13,8,4), (7,9,21,19)]
    check_vectors = [(3,4,5,7),(4,6,21,11),(8,12,21,20)]

    grid = generate_grid(basis_vectors, check_vectors , modulo)
    with open('grid.pickle', 'wb') as handle:
        pickle.dump(grid, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('grid.pickle', 'rb') as handle:
        grid = pickle.load(handle)
    
    for vector in check_vectors:
        print(vector, is_in_grid(vector,grid))
    
    plot4d(grid, check_vectors)