import pygal
from die import Die

die1 = Die()
die2 = Die()

results = []

for roll in range(1000000):
    result = die1.roll() + die2.roll()
    results.append(result)
    

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [x for x in range(2,13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
