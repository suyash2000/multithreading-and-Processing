# SuperFastPython.com
# create a large number of data files concurrently with threads
from os import makedirs
from os.path import join
from concurrent.futures import ThreadPoolExecutor

# save data to a file
def save_file(filepath, data):
    # open the file
    with open(filepath, 'w') as handle:
        # save the data
        handle.write(data)

# generate a csv file with v=10 values per line and l=5k lines
def generate_file(identifier, n_values=10, n_lines=5000):
    # generate many lines of data
    data = list()
    for i in range(n_lines):
        # generate a list of numeric values as strings
        line = [str(identifier+i+j) for j in range(n_values)]
        # convert list to string with values separated by commas
        data.append(','.join(line))
    # convert list of lines to a string separated by new lines
    return '\n'.join(data)

# generate and save a file
def generate_and_save(path, identifier):
    # generate data
    data = generate_file(identifier)
    # create a unique filename
    filepath = join(path, f'data-{identifier:04d}.csv')
    # save data file to disk
    save_file(filepath, data)
    # report progress
    print(f'.saved {filepath}')

# generate many data files in a directory
def main(path='tmp', n_files=5000):
    # create a local directory to save files
    makedirs(path, exist_ok=True)
    # create the thread pool
    with ThreadPoolExecutor(100) as exe:
        # submit tasks to generate files
        _ = [exe.submit(generate_and_save, path, i) for i in range(n_files)]

# entry point
if __name__ == '__main__':
    main()
