from googlesearch import search
import re

# Read the dorks from the file
with open('dorks.txt', 'r') as f:
    dorks = f.read().splitlines()

# Perform Google dorking and extract IP or domain names
results = []
for dork in dorks:
    query = 'site:{} filetype:txt'.format(dork)
    for url in search(query, num_results=10):  # Adjust the number of results as needed
        match = re.search(r'(https?://)?([\da-z.-]+)\.([a-z.]{2,6})[/\w .-]*/?', url)
        if match:
            domain = match.group(2)
            results.append(domain)

# Write the extracted IP or domain names to a file
with open('output.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')
