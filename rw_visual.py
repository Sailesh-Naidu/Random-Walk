import matplotlib.pyplot as plt
from randomWalk import RandomWalk

#keep making new tracks as long as the program is running
while True:
    user_input = input("Enter the number of random walk points you want, or "
                       "press Enter to use the default (5000): ")

    try:
        randomWalk_points = int(user_input) if user_input else 5000
    except ValueError:
        print("Invalid input. Using default value of 5000.")
        randomWalk_points = 5000
    rw = RandomWalk(randomWalk_points)
    rw.fill_walk()
    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = list(range(rw.num_points))
    ax.scatter(rw.x_values, rw.y_values, s =10, c = point_numbers,
              edgecolors=None, cmap=plt.cm.Blues)
    # Emphasize the start and the end point
    ax.scatter(0,0,s=100, c='green', edgecolors= None)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    ax.set_aspect('equal')
    #Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n):")
    if keep_running.lower() == 'n':
        break

'''fig1, ax1 = plt.subplots(figsize=(10, 6), dpi=128)
ax1.plot(rw.x_values, rw.y_values, color = 'blue')
plt.show()'''
