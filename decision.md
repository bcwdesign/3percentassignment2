# Decision: The Three C's

One or two sentences each. Replace the text after each arrow.

## Level 1 (required)

**Complexity:** Is this job deterministic (rules can do it), semantic (needs to understand meaning), or a judgment call? Did you route it to code or a model, and why?  
→ This job is mostly deterministic, so I routed it to code. The dates follow recognizable patterns, and rules can distinguish the event date from dates associated with things like a presale, RSVP, registration, or deadline. Using a model would add unnecessary complexity for something that can be handled reliably with rules.

**Context:** What did your code need to know to tell the presale date apart from the show date?  
→ The code needed to look at the words surrounding each date, not just the date itself. Words like "presale," "RSVP," "registration," and "deadline" indicate that a date is probably not the show date. The context around the date helps determine which date represents when the actual event happens.

**Criticism:** What would a basic test like `assert len(date) > 0` miss? What should a human still check before the event goes on the calendar?  
→ A test like `assert len(date) > 0` only proves that the code returned a date. It does not prove that it returned the correct date. The code could return a presale or RSVP deadline and still pass that test. A human should still verify that it is the actual event date and check details such as the year, start time, time zone, venue, and whether the event spans multiple days before adding it to the calendar.
→

## Level 2 (optional challenge)

**Order matters:** Why does the human check have to run before the rules check?
→

**Cost:** `python router.py` prints how many messages still reach an LLM. What was it before and after your changes?
→

**Your call:** Pick one message you could argue belongs in a different tier. Where did you put it, and why?
→

## Level 3 (optional bonus)

**Escalation:** Which messages escalated to the heavy model? Was the heavy answer worth the extra tokens?
→

**One change:** What did you change (prompt, escalation rule, or model), and what happened to the token totals?
→
