# Pega 7 Requestors Monitoring
Pega 7 requestors amount monitoring

## Usage
This tool has two ways to be used

### Import
Import `requestors_monitoring` function to your module
```python
from requestors_monitoring import requestors_monitoring
```

Firs argument of function is your nodes URLs in format like `http://pega:1111`

Second argument is time between monitoring requests in secconds


### Command line
Fill `NODES` list variable with your nodes URLs in format like `http://pega:1111`

Change `PERIOD` variable to change time between monitoring requests in secconds

Then just run from command line
```bash
python requestors_monitoring.py
```

## Pega Infinity
In Pega infinity service `/monitor/pingService/ping` have changed its contract. This tool is only usable for Pega 7.* 

You can also try to test it with earlier versions 
