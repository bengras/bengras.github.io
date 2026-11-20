Title: IODyne: precise dataflow tracking in hardware
Date: 2025-10-16 12:00
Category: Blog
Tags: intel,hardware,security,verification
Summary: My Intel Blog post on IODyne, RTL dataflow tracking.

At Intel I have been working on a method for tracking dataflow
in RTL simulations to e.g. track stale date. The project is called
IODyne (named after iodine, the contrast fluid). I wrote about IODyne on the [Intel Security Practices
Blog](https://www.intel.com/content/www/us/en/security/security-practices/blogs/improving-hardware-security-verification-iodyne.html).
It is a a differential dataflow-tracking technique for pre-silicon hardware
security verification.

The question IODyne answers: given a value in any
hardware buffer, where does it go, and which other values does it
influence?  IODyne does this with differential analysis. First
we simulate the design with a baseline. Then we simulate again with the tracked value modified, and diff
the results. See the post for full details.

*Update, October 2026:* the patent on this technique was granted on
October 20, 2026 — [US Patent 12,769,913, "Detecting potential
security issues in a hardware design using register transfer level
(RTL) information flow
tracking"](https://patentsgazette.uspto.gov/week42/OG/html/1551-3/US12769913-20261020.html),
assigned to Intel.
