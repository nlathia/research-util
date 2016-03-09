# Data Processing

Python scripts to extract features from [ES Android Library](http://emotionsense.github.io/sensors.html) JSON data.

They assume that each data file is named \*_data-type_\*.json and contains a single JSON object per line.

## Usage

Extracting activity scores (standard deviation of the magnitude vector)

$ python extract_activity.py /path/to/your/data_file.json

OR (for multiple files)

$ python extract_activity.py /path/to/your/files/




