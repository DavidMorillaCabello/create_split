# Create split

Tools to create split files for datasets. This method is deeply focused on obtaining 
results similar to Eigen or Zhou splits for the KITTI datasets.

## Requirements

* python3
* scikit-learn 0.22.2

## Method

The method analyses a folder organised according to the following structure:

    /folder
        /date1
            /session1
                /device1
                    /data
                /device2
                ...

            /session2
            ...

        /date2
        ...

The following parameters should be introduced:

* **`-s / --split`** Split file name.
* **`-f / --folder`** Objective folder.
* **`-d / --device_list`** Delimited list with the aimed devices.
* **`-t / --data_type`** Datatype to extract files from.
* **`-u /--use_size`** Optional parameter to use a proportion of the total data.
* **`--test_size`** Optional training size for the split. The default is set to 0.25.
* **`-e / --exclude`** Optional list with global path for folders to be excluded.
* **`-p / --pop_limits`** Optional parameter to pop the limits (per session) from the list of files.

The code will list all the files' name of the specified datatype in the data folder from each device
and store it in an object with its path, date, session and device.

Then, it will split the data listed in two for training and test and write them in the respective files.

## Usage

Asuming test/ is a folder containing the correct structure, it can simply be used this way:

    python3 create_split.py -s files.txt -f test -d "image_00" -t .png --test_size 0.3 -p True -u 0.1
