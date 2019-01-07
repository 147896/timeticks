# Python script to monitor timeticks network interface for changes.
# Used as nagios monitoring plugin. To know how to import and configure it in Nagios, see the Nagios Documentation: https://assets.nagios.com/downloads/nagios-network-analyzer/docs/Understanding-Alerting-In-Nagios-Network-Analyzer.pdf

# Example of how to use the script.: python timeticks.py --help
usage: python timeticks.py [--help] [-c <community>] [-i <ipaddr>] [-o <oid>]
