**XML-RPC XML Entity Expansion DoS (Legacy PoC)**
![Alt text for the screenshot](/Assets/Screenshot.png)

**Overview**

This repository contains a legacy proof-of-concept (PoC) script demonstrating an XML entity expansion–based Denial of Service (DoS) condition against WordPress and Drupal XML-RPC endpoints that relied on unsafe XML parsing behavior.

The script targets parser-level weaknesses, not application logic, authentication, or authorization.

**Vulnerability Class**

Category: Denial of Service (Availability)

Technique: XML Internal Entity Expansion

Component: XML-RPC (xmlrpc.php)

Attack Layer: XML parser (libxml2 via PHP)

**This is not:**

Remote Code Execution

Authentication bypass

Data exposure

Logic flaw

***Usage***

**Run xmlrpc.py using**
```bash
python3 xmlrpcdos.py https://example.com/xmlrpc.php
```

**Run xmlrpc.sh by**
```bash
chmod +x xmlrpcdos.sh
./xmlrpc.sh https://example.com/xmlrpc.php
```
**How the Script Works**
1. XML Payload Construction

The payload defines an internal XML entity:
```bash
<!DOCTYPE lolz [
 <!ENTITY poc "aaaaaaaaaaaaa">
]>
```

The entity is expanded inside the XML-RPC method name:
```bash
<methodName>aaa&poc;</methodName>
```

During parsing, the XML processor must resolve the entity before any application-level validation occurs.

2. Target Endpoint

The script sends POST requests to:
```bash
/xmlrpc.php
```

This endpoint processes raw XML input and hands it to the XML parser, making it a suitable surface for parser-based DoS testing on legacy systems.

3. Request Flooding Mechanism

Each thread sends 100 XML-RPC requests

Up to 10,000 threads are created

Requests are sent without response handling or backoff

This attempts to overwhelm the target by forcing repeated XML parsing operations.

4. Intended Impact (on vulnerable systems)

**On systems using older libxml / PHP builds, this could cause:**

=> Excessive memory allocation

=> CPU exhaustion during entity resolution

=> Worker process saturation

=> Temporary service unavailability

**Why This Worked Historically**

**This PoC was effective against stacks where:**

=> XML entity expansion was enabled by default

=> No entity size or expansion limits were enforced

=> XML parsing occurred before request validation

=> libxml did not restrict DOCTYPE processing

**Commonly affected environments:**

=> Older PHP versions

=> Legacy WordPress installations

=> Drupal 6 / early Drupal 7

=> Unhardened Apache + PHP-FPM setups

**Why It Usually Does NOT Work Today**

=> Modern environments mitigate this vector at the parser level, not via WAF rules.

**Typical reasons for failure:**

=> libxml enforces entity expansion limits

=> DOCTYPE handling is restricted or ignored

=> XML-RPC parsing is hardened in WordPress core

=> Malformed or unexpected method names are rejected early

=> TLS and OS-level resource limits reduce request throughput

**As a result, the payload is either:**

Ignored

Rejected

Parsed safely with negligible cost

**Important Technical Notes**

XML-RPC being reachable does not imply vulnerability

This PoC does not use recursive or exponential entities

The script is client-heavy and may exhaust local resources first

HTTPS significantly reduces effective request flooding

**Accurate Usage**
=> Valid Use Cases
=> Testing legacy lab environments
=> Studying historical XML parser DoS techniques
=> Verifying XML parsing hardening
=> Blue-team / SOC training and analysis
=> Understanding why older PoCs fail on modern stacks
=> Not Suitable For
=> Modern WordPress exploitation
=> Real-world availability attacks
=> Bug bounty submissions on updated systems
=> Bypassing current mitigations & Limitations
=> Targets obsolete behavior
=> No impact on properly patched systems
=> No detection of vulnerability presence
=> No exploit chaining capability

**Disclaimer**
This code is provided for educational and defensive research purposes only, specifically for understanding legacy XML parsing vulnerabilities and their mitigation.
