---
title: "How to Avoid Embarrassing Data Failures"
subtitle: "Shaping a Data Team"
date: 2025-02-25
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/how-to-avoid-embarrassing-data-failures
audience: everyone
wordcount: 850
reactions: 5
comments: 0
restacks: 2
ingested_by: EVEglyphDesign eve-substack-archive
---

# How to Avoid Embarrassing Data Failures

*Shaping a Data Team*

![](https://substackcdn.com/image/fetch/$s_!J0J4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8d5a712-9a75-46c3-81f0-364051661a9a_5712x4284.jpeg)
- Data problems show up in some of the most unwelcome places:

You discover that the system sent a blank report to the CEO.

- People start a long email thread to discuss why the daily report showed total sales amounts 50% higher than everyone expected.

- Somebody canceled a review meeting because all the data was under a single customer.

You publish hundreds of thousands of correct numbers every day, but one wrong number destroys the credibility of all the data in the platform. Sometimes, nobody will notice, but other times, everyone will see it. How can you develop confidence that you won’t show up to work tomorrow only to face another embarrassing data problem?

If nagging issues like this sound familiar, I’d like to help.

Most data problems begin with deeper issues in your company’s business processes and system connections. If you don’t [work beneath the surface](https://zanehall.substack.com/p/listen-to-the-messengers?r=4chtg6) to fix the root causes, errors will constantly disrupt everyone’s work. You need a *proactive* solution. But when you’re providing data for a large company, there’s no way you can find and fix all errors before someone else sees them. You also need a *reactive *solution.

I’ve developed three ways to overcome embarrassing data problems:

- Use general ledger data to find business process issues (proactive).

- Use the schedule history to find problems in data pipelines (proactive).

- Use service-level agreements to certify all the data (reactive).

**Finding Business Process Issues**

All data from your company’s business processes flows into your financial reports, but learning how it gets there can help you find systematic data problems.

Imagine that your sales team offers volume discounts to a large customer. If the invoicing system can’t apply the discount terms to that customer’s invoices, the system will record (“post”) an incorrect number in the GL. The financial reports will be incorrect without those discounts, so accountants enter manual adjustments (journal entries) in the GL system.

Manual entries wouldn't be needed at all if every business system applied the proper financial rules, so you can easily find a business process that’s not working correctly by counting the number of manual journal entries in your company’s GL system. Count all the manual entries posted over several periods and categorize them by name, account number, and any other field you think might help you find patterns. There’s a good chance you’ll find a broken business process that everyone working in the daily operations already knows about.

Take that insight to heart and make a case to fix the process instead of trying to patch it up with more reports.

**Finding Data Pipeline Issues**

Few things embarrass a data team more than discovering they issued incorrect numbers because a system process failed to run correctly. Data pipelines move data from one place to another, like the electrical wires and plumbing hidden within the walls of your house. The system that runs those processes (“jobs”) can help you find areas where data isn’t flowing smoothly.

Look for a report that shows how often those jobs run and how frequently they fail. The frequency of these events usually indicates where the problems lie. Data leaders sometimes forget how much a reliable data processing solution helps build confidence for the business teams they support. It’s always worth the time and effort to ensure these processes always run reliably and on time.

**Service Level Agreements**

Don’t just rely on technical solutions to prevent embarrassing data problems. Put in place a business process that certifies the data and sets expectations for data quality for everyone who uses it. IT people call this a “service level agreement (SLA).”

A good SLA should be clear and widely communicated. My data teams committed to “certify” all data daily by 8 a.m. Pacific Time. Because we made that commitment clear, business teams knew we would notify them if we didn’t meet the SLA and give them an estimate for when we expected to certify the data.

How did we certify the data every day? We used high-level summaries of key datasets that we could easily compare to other data points. When the data looks correct at a high level, you get more confidence that all the underlying data is also correct. We also developed a set of non-technical, business-focused audits for the data. We called these “controls” and used our eyes (not the system) to verify the data passed each check. The process took about 3 minutes daily, and we audited data this way every day of the year, including weekends and holidays.

If you’re an IT person, this probably sounds like a terrible idea. That’s why I’m telling you about it: data problems always find new ways to avoid your systematic solutions. If you don’t use a business process (like SLAs) to qualify the data, you’ll continually face embarrassing data problems.

### Proactive and Reactive

Every data worker knows they should solve embarrassing problems by fixing the root causes, but that’s often outside their control. That’s why using a *proactive *and *reactive *approach helps develop trust with business partners and opens the door to making new commitments to solve the underlying problems.

---

Source: [How to Avoid Embarrassing Data Failures](https://zanehall.substack.com/p/how-to-avoid-embarrassing-data-failures)
