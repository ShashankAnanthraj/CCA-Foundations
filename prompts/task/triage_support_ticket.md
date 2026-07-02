Task: read one raw support ticket and triage it.

Steps:
1. Determine the primary category: billing, bug, feature_request, how_to, or other.
2. Assess severity: low, medium, high, or critical — based only on impact stated in the ticket.
3. Decide whether it needs human escalation (true/false).
4. Write a one-sentence summary in neutral language.

Rules:
- Use only information present in the ticket. If a field is unknowable, choose the safest default
  (severity=low, needs_human=false) and keep the summary factual.
- Do not invent customer names, order numbers, or promises.

Few-shot examples:
- Ticket: "I was charged twice for my subscription this month." -> category=billing, severity=medium,
  needs_human=true, summary="Customer reports a duplicate subscription charge this month."
- Ticket: "How do I export my data to CSV?" -> category=how_to, severity=low, needs_human=false,
  summary="Customer asks how to export data to CSV."
