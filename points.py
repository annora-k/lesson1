list_scores = [{'class':4, 'scores':[3, 4, 4, 5, 2]}, {'class':5, 'scores':[5, 5, 5, 2, 3]}]

for classes in list_scores:	
	for key in sorted(classes):
		#print(key, '-', classes[key])
		if key == 'scores':
			for score in key:
				print(key)


			#class_scores = classes[scores]
			#print(class_scores)
	