import bisect

def main():
	with open('wordlist.txt', 'r') as f:
		wordlist = f.read().split()
		
		firstIndex = bisect.bisect_left(wordlist, 'ea')
		lastIndex = bisect.bisect_left(wordlist, 'eb')

		print(lastIndex - firstIndex)

main()