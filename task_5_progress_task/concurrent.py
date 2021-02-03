import concurrent.futures

x = 'aman'
def prin(x):
    print(x)
    print(x)
with concurrent.futures.ProcessPoolExtractor() as executor:
    executor.map(prin, x)
    