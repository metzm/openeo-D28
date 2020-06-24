# openeo-D28

This package contains configuration file(s) for the [GO backend validator tool](https://github.com/Open-EO/openeo-backend-validator/tree/master/openeoct).


## Description

The config file(s) allow to test a given openEO back-end against the openEO API specification (v1.0). The GO validtor tool must be installed locally to run the validation.


## Setup

### Installation
First install and build the validator tool following instructions here: https://github.com/Open-EO/openeo-backend-validator/tree/master/openeoct. make sure the executable can be used from other folders too.

### Config file
Copy the `SAMPLE_config.toml` file to e.g. `MYBACKEND_config.toml` and fill the required fields. Do not add username and password fields directly in there, you can save a bash script in the `credentials` folder, which is not under version control.

### Run validation
Run the following command:
```
cd src/openeo_d28
openeoct config openeo_v1.0_endpoints.toml MYBACKEND_config.toml
```

The output will be stored in the current folder as a JSON file.



Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
