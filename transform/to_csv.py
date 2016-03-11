from json import loads, dumps
from os import path, listdir
import csv
import sys

from multiprocessing import log_to_stderr
import logging

from sensors.sensors import get_sensor

logger = log_to_stderr(logging.INFO)


def flatten_file(input_file, sensor):
    """
    :param input_file: The JSON file
    :param sensor: The sensor
    :return: yields the CSV rows of each sample
    """
    total_written = 0
    with open(input_file, 'r') as lines:
        for line in lines:
            try:
                sample = loads(line)
                written = 0
                for csv_line in sensor.flatten(sample):
                    written += 1
                    yield csv_line
                if written == 0:
                    logger.info('Warning: no rows extracted from: ' + dumps(sample))
                total_written += written
                if total_written % 100 == 0:
                    logger.info('Progress: extracted ' + str(total_written) + ' rows.')
            except ValueError:
                raise
    if total_written == 0:
        raise Exception('Error: no rows extracted from '+input_file)


def get_data_type(input_file):
    if '.json' in input_file:
        data_type = path.split(input_file)[1]
        data_type = data_type[data_type.index('_')+1:data_type.rindex('_')]
        if len(data_type) == 0:
            logger.info('File names are expected to be *_sensor_*.json')
            raise Exception('No sensor type in file name: '+input_file)
        logger.info('Parsing file with sensor type: ' + data_type)
        return get_sensor(data_type)
    else:
        logger.info('Not a JSON file: ' + input_file + ', skipping.')


def file_to_csv(input_file):
    """
    :param input_file: The JSON data file, named [*]_[datatype]_[*].json
    """
    logger.info('Reading: ' + input_file)
    sensor = get_data_type(input_file)
    if sensor is not None:
        output_file = input_file.replace('.json', '.csv')
        logger.info('Writing output to: ' + output_file)
        with open(output_file, 'w') as out:
            rows = csv.writer(out)
            rows.writerow(sensor.header())
            map(rows.writerow, flatten_file(input_file, sensor))
        logger.info('Finished flattening: ' + input_file)


if __name__ == '__main__':
    if path.isdir(sys.argv[1]):
        for f in (path.join(sys.argv[1], f) for f in listdir(sys.argv[1])):
            file_to_csv(f)
    else:
        file_to_csv(sys.argv[1])





