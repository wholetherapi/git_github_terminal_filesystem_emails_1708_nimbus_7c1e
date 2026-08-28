# Deployment notes

The emit workers are deployed independently from the ingest workers so that a
routing change does not require draining the ingest queues.
