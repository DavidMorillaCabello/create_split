from os import listdir, getcwd
import argparse


class SplitOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Arguments for the split generation')

        self.parser.add_argument('-s', '--split', type=str,
                                 help='Split file name', required=True)
        self.parser.add_argument('-f', '--folder', type=str,
                                 help='Objective folder', required=True)
        self.parser.add_argument('-d', '--device_list', type=str,
                                 help='Delimited list with the aimed devices', required=True)
        self.parser.add_argument('-t', '--data_type', type=str,
                                 help='Datatype to extract files from', required=True)
        self.parser.add_argument('--test_size', type=self.coefficient_float,
                                 help='Optional test size for split. Default is 0.25', default=0.25)
        self.parser.add_argument('-e' ,'--exclude', type=str,
                                 help='Optional list with folders to exclude.', default="")

    def coefficient_float(self, x):
        try:
            x = float(x)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "{} not a floating-point literal".format(x))

        if x < 0.0 or x > 1.0:
            raise argparse.ArgumentTypeError(
                "{} not in range [0.0, 1.0]".format(x))
        return x

    def parse(self):
        self.options = self.parser.parse_args()
        return self.options
