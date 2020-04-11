from os import listdir, getcwd
from os.path import isfile, isdir, join
from sklearn.model_selection import train_test_split
from options import SplitOptions


#Global variables for arguments and path
options = SplitOptions()
opts = options.parse()
cwd = getcwd()

def extract_files(path, date, session, device, data_types):
    '''
        Return all the files' name of a directory that matches a data type.
        A Data object is created to store it's path, date, session, device 
    '''
    full_path = join(path, date, session, device, "data")

    return [Data(path, date, session, device, f) for f in sorted(listdir(full_path)) if (isfile(join(full_path, f)) and f.split(".")[-1] == data_types.split(".")[-1])]


def extract_subfolders(path):
    '''
        Returns all the subfolders' name of a directory as a str list.
    '''
    return [f for f in sorted(listdir(path)) if isdir(join(path, f))]

def get_all_files():
    '''
        Function to gather all file names from a set of folders.
        The set is assumed to be organised according to:
        date/
            session/
                data1/
                    data/
                        files...
                data2/
                    data/
                        files...
        
        * Date makes reference to the temporal stamp.
        * Session makes reference to an internal stamp for the same date.
        * The different data folders refer to different sensors (e.g. a set of cameras)
        * Inside every sensor, tere is a data folder and inside it are all the files.
    '''
    dates = []
    files = []

    path = join(cwd, opts.folder)

    print("Extracting from path: {}".format(path))

    dates = extract_subfolders(path)

    print("Found dates: {}".format(dates))

    for date in dates:

        sessions = extract_subfolders(join(path, date))

        print("In date: {} found sessions: {}".format(date, sessions))

        for session in sessions:
            for device in opts.device_list.split(","):

                print("In session: {} extracting device: {}".format(session, device))

                if isdir(join(path, date, session, device, "data")):
                    files.extend(extract_files(
                        path, date, session, device, opts.data_type))

    print("Extracted files: ")
    return files

def write_file(name, data):
    '''
        Writes the Data objects listed in the following format:
            date/session number device
        in a file named with the indicated name.
    '''
    with open(name, "w+") as f:

        print("Openned file: {}".format(opts.split))

        for data_item in data:
            file_path = join(data_item.date, data_item.session)
            file_number = data_item.name.split(".")[0]
            file_data = data_item.data
            print("Writing data: {} {} {}".format(
                file_path, file_number, file_data))
            f.write("{} {} {}\n".format(file_path, file_number, file_data))
    
    f.close()

class Data:
    '''
        Structure to store values about each file gathered.
    '''
    def __init__(self, path, date, session, data, name):
        self.path = path
        self.date = date
        self.session = session
        self.data = data
        self.name = name


if __name__ == "__main__":



    files = get_all_files()
    
    train, test = train_test_split(files, test_size=opts.test_size, random_state=42)

    train_name = "train_" + opts.split
    test_name = "test_" + opts.split

    write_file(train_name,train)
    write_file(test_name,test)


