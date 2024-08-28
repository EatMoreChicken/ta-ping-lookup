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

## Example Usage

This is an example of how to use the external lookup in a search:

```spl
| makeresults
| eval host="10.0.0.1"
| lookup ping_lookup host
```

The output should look like this:

| _time | host    | ping_status | timestamp           |
|-------|---------|-------------|---------------------|
| 2024-08-27 19:59:20 | 10.0.0.1 | Reachable   | 2024-08-27 23:59:20 |

Here is an example of it using multiple hosts:

```spl
| makeresults
| eval host="10.0.0.1;10.0.0.2;10.0.0.3"
| makemv delim=";" host
| mvexpand host
| lookup ping_lookup host
```

Keep in mind that the script has a hardcoded timeout of 2 seconds. If you need to change this value, you can modify the `ping_lookup.py` script. There might be better ways to handle this, but this is just a simple example.