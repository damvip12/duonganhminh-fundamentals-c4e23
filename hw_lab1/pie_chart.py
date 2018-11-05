from matplotlib import pyplot

ref_counts = [31 , 12 , 7]

ref_names = ["event", "ads" , "wom"]

pyplot.pie(ref_counts, labels=ref_names, autopct="%.1f%%", shadow=True)
pyplot.axis("equal")
pyplot.title("References of customer")

pyplot.show()