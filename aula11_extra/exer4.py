def hondt(votes, numseats):
	N = [0] * len(votes)

	while numseats > 0:
		q = []
		for i in range(len(votes)):
			quocient = votes[i] / (N[i] + 1)
			q.append(quocient)

		max_q = max(q)
		max_q_indexes = [i for i, x in enumerate(q) if x == max_q]
		min_q_index = min(max_q_indexes, key=lambda x: votes[x])
		N[min_q_index] += 1
		numseats -= 1

	return N

print(hondt([15300, 12000, 6600, 5100], 6))