# Dataset Handling and Privacy

Electricity-consumption datasets can contain sensitive customer or operational information.

## Repository rules
- Do not commit raw customer-level datasets unless you have explicit authorization and a lawful basis to publish them.
- Do not commit names, phone numbers, addresses, meter numbers, account identifiers, or other identifying information.
- Treat customer identifiers as identifiers, not as consumption measurements.
- Use synthetic, anonymized, or otherwise approved samples when sharing examples.
- Check notebook outputs, plots, logs, and metadata for sensitive information before committing.
- Document dataset provenance, permissions, anonymization, and access restrictions.

The repository .gitignore excludes common dataset formats and data folders by default. Review every file before publishing.
