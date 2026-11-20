Title: IODyne: precise dataflow tracking in hardware
Date: 2025-10-16 12:00
Category: Blog
Tags: intel,hardware,security,verification
Summary: My Intel Security Practices Blog post on IODyne, a differential dataflow-tracking technique for pre-silicon hardware security verification, is up.

I wrote about IODyne on the [Intel Security Practices
Blog](https://www.intel.com/content/www/us/en/security/security-practices/blogs/improving-hardware-security-verification-iodyne.html):
a differential dataflow-tracking technique for pre-silicon hardware
security verification.

The question IODyne answers sounds simple: given a value in any
hardware buffer, where does it go, and which other values does it
influence? Answering it precisely is how you catch data leaking across
security boundaries — the class of problem behind vulnerabilities like
Meltdown and MFBDS — before the design ever reaches silicon.

IODyne does this with differential analysis: simulate the design with
a baseline, simulate again with the tracked value modified, and diff
the results. Only true dependencies show up, which eliminates the
false positives that plague the traditional X-injection approach. When
it does flag an issue, it automatically minimizes the test case down
to the single injection needed to reproduce it.

The post walks through the technique from first principles with a
small Verilog example, then shows how it applies to real CPU
vulnerability classes. [Read it
here](https://www.intel.com/content/www/us/en/security/security-practices/blogs/improving-hardware-security-verification-iodyne.html).

*Update, October 2026:* the patent on this technique was granted on
October 20, 2026 — [US Patent 12,769,913, "Detecting potential
security issues in a hardware design using register transfer level
(RTL) information flow
tracking"](https://patentsgazette.uspto.gov/week42/OG/html/1551-3/US12769913-20261020.html),
assigned to Intel.
