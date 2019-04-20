def main():
	combined = 1
	g = []
	r =  str (input ("Enter numbers separated by a space for each column:  "))
	w = r.split(" ")
	for x in w:
		if x:
			x = int(x)
	return w

def searchTable(g):
	result = {}
	combined_cardinality = []

	with open('cardinality.sql', 'r') as f:
		lines = f.readlines()
		for line in lines:
			columns = line.split('|')
			g = list(map(int, g))

			for column in columns:
				if columns.index(column) in g:
					combined_cardinality.append(column)
			for x in g:
				x = int(x)
				if x > 0:
					x -= 1
				if x in result:
					result[x].append(columns[x])
				else:
					result[x] = [columns[x]]
	line_list = []
	for line in lines:
		line = line.rstrip("\n")
		columns = line.split('|')
		for column in columns:
			line_list.append(column)

	g = list(map(int, g))
	max_cardinality = 1

	for key, value in result.items():
		max_cardinality *= len(set(result[key]))
		print ("Column {0} cardinality: {1}".format(key,len(set(result[key])) ))
	print ("Maximum cardinality: {0}".format(max_cardinality))
	zipped = zip(line_list[0::2], line_list[1::2])
	print ("Combined cardinality: ", len([tuple(x) for x in set(map(frozenset, zipped))]))

if __name__ == "__main__":
	numbers_list = main()
	searchTable(numbers_list)

