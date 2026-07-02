Output specification: respond with a single JSON object matching this contract exactly. No prose.

Fields:
- category:    one of ["billing","bug","feature_request","how_to","other"]
- severity:    one of ["low","medium","high","critical"]
- needs_human: boolean
- summary:     string, one neutral sentence, grounded only in the ticket

The machine-enforced JSON Schema for this contract lives beside the demo that uses it
(topics/02-prompt-engineering/demo.py) and is applied via structured outputs.
