Title: The Fuzzer at the Coffee Machine
Date: 2026-10-15 12:00
Category: Blog
Tags: intel,fuzzing,firmware
Summary: Our Intel Security Practices Blog post on fuzzing embedded firmware in simulation-based SoC environments, told as a story.

Together with Eric Alata, Benoît Morgan, and Neer Roggel I wrote about
how we fuzz embedded firmware, on the [Intel Security Practices
Blog](https://www.intel.com/content/www/us/en/security/security-practices/blogs/the-fuzzer-at-the-coffee-machine.html).

The fuzzer runs firmware in a simulator, which gives us parallel
sessions and trace-level visibility that bare metal can't. Taint
tracking identifies which input bits actually influence execution, and
we use that to generate seeds that exercise meaningful firmware
behavior from the start. Crash-trace analysis tooling then connects a
failing input back to what happened inside the firmware — important in
multi-unit SoC environments, where failures show up as hangs,
livelocks, or bad states spread across components rather than a clean
stack trace.

Rather than a conventional technical report, we told it as a story: a
week of conversations at the office coffee machine between a security
lead, a developer, and a product manager who needs a minimum viable
setup, not a six-month program. The format fits, because that is how
the project actually took shape — through discussions, constraints,
and iteration.

[Read it
here](https://www.intel.com/content/www/us/en/security/security-practices/blogs/the-fuzzer-at-the-coffee-machine.html).
