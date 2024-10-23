![Tests](https://github.com/KhulnaSoft/khulnasoft-graph-api/actions/workflows/tests.yaml/badge.svg)

# KhulnaSoft Graph API

KhulnaSoft Graph API allows you programatically interact with KhulnaSoft dataset.

## Installing the API
Install KhulnaSoft Graph Python API.
```
git clone https://github.com/KhulnaSoft/khulnasoft_graph_api
cd khulnasoft_graph_api
pip install . --user
```

## Verifying the installation

```python
>>> import khulnasoft_graph_api
>>> khulnasoft_graph_api.__version__
X.X.X
```

## Documentation

For more information about how to use **khulnasoft_graph_api** visit the [documentation](https://khulnasoft.github.io/khulnasoft-graph-api/) page.

You may also want to take a look at some of our [example scripts](https://github.com/KhulnaSoft/khulnasoft-graph-api/tree/master/examples),
which besides doing useful work for you can be used as a guidance on how to use **khulnasoft_graph_api**.

In addition, you can find the documentation for the KhulnaSoft Graph REST API at the [API reference](https://developers.khulnasoft.com/v3.0/reference#graphs)

# Test it!

Use tox to test:

```
>>> tox
```

# Changelog

### V2.2.0
- Support for loading Graphs with special relationships (Groups, Intelligence, Livehunt, Retrohunt, Commonalities).
- New method for creating groups of nodes.

### V2.1.0
- Support for setting Graph representation.

### V2.0.0
- Removed `carbonblack_children` and `carbonblack_parent` relationships in File entity.
- Create a Collection from a Graph.
- Added **new entity** types:
  - collection
  - reference
  - whois
  - ssl_cert
- Added **new relationships**:
  - Files: *dropped_files, collections, email_attachments, itw_ips, overlay_children, pe_resource_children, references, urls_for_embedded_js*
  - Domains: *historical_ssl_certificates,
    historical_whois,
    caa_records,
    cname_records,
    mx_records,
    ns_records,
    soa_records,
    collections,
    references.*
  - IP Addresses: *historical_ssl_certificates,
    historical_whois,
    collections,
    references.*
  - Urls: *contacted_domains,
    contacted_ips,
    redirects_to,
    urls_related_by_tracker_id,
    communicating_files,
    referrer_files,
    embedded_js_files,
    collections,
    references*
  - Collections: *files,
    domains,
    ip_addresses,
    urls,
    references.*
  - Whois: *network_location.*

### V1.1.3
- Bug fixing.

### V1.1.2
- Bug fixing.

### V1.1.1
- Bug fixing.
- Fixing documentation.

### V1.1.0
- Added download graph screenshot from KhulnaSoft.

### V1.0.1
- Fixing documentation.

### V1.0.0
---
- Added autosearch algorithm to find links between graph's nodes.
- Accept **MD5** and **SHA1** as valid ID for nodes with **file type**.
- Added **VTIntelligence** search for nodes without any information.
- Accept custom node types.
- Added load graph from KhulnaSoft.
- Added clone graph from KhulnaSoft.
