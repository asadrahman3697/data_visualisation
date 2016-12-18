import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.title("Random Walk", fontsize=24)


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    #plt.figure(dpi=128, figsize=(10, 6)) # Control resolution and bg
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.inferno,
        edgecolor='none', s=1)

    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', 
        s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=100)
        
    
    plt.axes().get_xaxis().set_visible(False)    
    plt.axes().get_yaxis().set_visible(False)    
        
    plt.show()
    
    keep_running = input("Another walk? (y to continue, anything else to exit)")
    if keep_running != 'y':
        break
