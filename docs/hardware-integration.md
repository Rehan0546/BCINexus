# Hardware Integration Guide

This guide describes public integration principles for BCI, neuroscience, biosignal, and research hardware.

## Supported Pattern

Hardware integrations should expose data through documented files, streams, or APIs that can be converted into public workflow artifacts. Vendor-specific SDKs and device drivers should remain in separate repositories unless they are explicitly open source and compatible with this repository's license.

## Recommended Metadata

- Device name and manufacturer.
- Sampling rate.
- Channel names and units.
- Sensor layout.
- Timestamp format.
- Calibration steps.
- Filtering performed before export.
- Consent and privacy requirements for human-subject data.

## Safety and Compliance

This repository does not provide medical device certification, clinical validation, or regulatory approval. Integrators are responsible for device safety, consent, data governance, and local compliance.
