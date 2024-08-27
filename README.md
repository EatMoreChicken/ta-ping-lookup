# Ping Lookup - An External Lookup Example

This is a simple Splunk app that provides an external lookup that allows users to ping a host and get the response time.

The goal of this app is to be a simple example of how to build an external lookup using a Python script in Splunk.

## Structure

The app is structured as follows:

```
ta-ping-lookup/
├── README.md (You are here)
├── bin/
│   └── ping_lookup.py
├── default/
│   ├── app.conf
│   ├── transforms.conf
│   metadata/
│   └── default.meta
```

- `bin/ping_lookup.py` is the Python script that performs the ping and returns the response time.
- `default/app.conf` is the app configuration file. It contains general information about the app.
- `default/transforms.conf` contains the necessary configuration to define the external lookup.
- `metadata/default.meta` is the metadata file that contains the permissions for the knowledge objects in the app.