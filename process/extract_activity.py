from json import loads
import csv
import os
import sys

from multiprocessing import log_to_stderr
from logging import INFO

from sensors.activity import Accelerometer

logger = log_to_stderr(INFO)

ACCELEROMETER = 'accelerometer'
JSON = '.json'
FEATURES = '-features.csv'


def extract_features(data_file):
    if all(x in data_file for x in [ACCELEROMETER, JSON]):
        logger.info('Reading: ' + data_file)
        result_file = data_file.replace(JSON, FEATURES)
        written = 0
        with open(data_file, 'r') as lines, open(result_file, 'w') as out:
            rows = csv.writer(out)
            rows.writerow(Accelerometer.features_header())
            for entry in (loads(l) for l in lines):
                sample = Accelerometer(entry)
                rows.writerow(sample.get_features())
                written += 1
                if written % 100 == 0:
                    logger.info('Progress: extracted ' + str(written) + ' rows.')
        logger.info('Finished: ' + data_file)
    else:
        logger.info('Skipping file: ' + data_file)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.info('Missing argument: data file name or directory.')
    else:
        if os.path.isdir(sys.argv[1]):
            for d_file in (os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1])):
                extract_features(d_file)
        else:
            extract_features(sys.argv[1])




