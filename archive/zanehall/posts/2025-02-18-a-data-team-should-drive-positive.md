---
title: "A Data Team Should Drive Positive Change"
subtitle: "Shaping A Data Team, February 2025"
date: 2025-02-18
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/a-data-team-should-drive-positive
audience: everyone
wordcount: 1072
reactions: 2
comments: 2
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# A Data Team Should Drive Positive Change

*Shaping A Data Team, February 2025*

![](https://substackcdn.com/image/fetch/$s_!9-O1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaa46f57-120c-461a-b456-0cad257b8c3b_4734x3550.jpeg)
- In the IT world, “change management” has a technical definition: making sure nothing breaks when you change a system. Everyone fears the “blue screen of death,” an all-too-familiar experience for Microsoft Windows users. One small code change can crash a whole system and all of a company's operations, like [CrowdStrike did to airline reservations](https://www.techtarget.com/whatis/feature/Explaining-the-largest-IT-outage-in-history-and-whats-next) last year. Good change management matters far more than brilliant ideas in corporate IT.

But for a data team, that’s just the beginning. You’re managing changes to the systems *and *the decisions. People—especially executives—expect you to improve all the decision-making in the company. I’ve heard C-level executives say these very words many times. No other IT team faces such an incredibly challenging and subjective goal.

How will people feel when you tell them what they need to change? I’m more likely to acknowledge my need to change when the advice comes from a trusted friend. That’s a great way to think about your data team’s relationship with your company: you see the changes that will lead to better decisions, and you’re in the best position to communicate the need. I want to challenge you, data team leader, to answer this question: will you remain a service provider like the rest of IT, or will you drive the positive changes that help your company make better decisions?

Here are three examples of changes a data team can drive to help their company make better decisions.

### Working Together

When people working in different parts of a company maintain the same data in different places, it clearly shows that they aren’t working together. Your data team sees that people need to change how they work.

When I started working at Maxim Integrated, the company had four competing product databases. Together, they added up to about 300,000 part numbers (SKUs). Since no one system provided the “answer,” people constantly argued about which system had the correct data. Even the most straightforward fact about a part, like its status, wasn’t clear. Every team used different codes to identify parts as new, old, buildable, or sellable, and that made it hard to do simple things like change the prices or throw away inventory.

People all over the company struggled with this problem for years, but my data team felt the most pain. We were constantly stuck writing complicated rules in reports to answer questions, then defending the data on reports, and then trying to settle differences between competing definitions and department leaders.

Finally, we built consensus around making SAP the system of record (a communication effort), helped the business teams adopt a single report for the data (a collaborative effort), and used exception reports to identify the obsolete parts (an innovation).

We discovered that 60% of those 300,000 SKUs were never used by anyone. Finding easy wins in the data helped us get consensus among every business team to make a change. Once everyone agreed on the data definitions, getting them to adopt SAP as the authoritative system of record for product data was easy.

Nobody asked us to work on this project, and it took two years to complete--not just because of the technical work but also because of the constant need to balance the work with more urgent problems--but ultimately, this seemingly small change removed confusion from thousands of product decisions, year after year.

It helped all of the company’s teams work better together.

### Eliminating Technical Debt

Technical debt accumulates when companies take shortcuts to complete projects. Business and IT teams install new systems all the time but regularly postpone the work to turn off the old system to meet deadlines. This decommissioning work usually falls to the data team to complete.

My data teams encountered this situation every year, from the smallest to the largest systems. Maxim Integrated installed a new SAP system for revenue planning, but when I started at the company two years after that project was completed, the system it was meant to replace was still actively in use by a few people. The IT team had already shifted resources to support the new system, but the business teams needed reports with combined data from both the old and new systems. That’s because the new system didn't support the inputs used to allocate revenue to end-market categories.

The cost to keep that old system running wasn’t just the electricity that powered the server. There wasn’t any license cost associated with it because the IT team created it with custom code years before. No staff members were dedicated to maintaining the software. You can’t calculate an ROI for eliminating technical debt. But technical debt accumulates like rust on a car. Painting over it creates more risk; eventually, you can only get rid of it by scrapping the whole thing.

Business and IT teams don’t always account for disconnecting everything from old systems when they replace them. That’s where a data team makes such a big difference for everyone - staying committed to eliminating technical debt. My teams took this responsibility so seriously that we gave it an acronym: GROSS (Get Rid of Old Stuff Sooner).

### Redirecting Requests

Almost every data problem at your company starts with a call to the data team. They’re the “first responders” of IT. A data team that says “yes” to every request isn’t doing anyone any favors; helping their company might mean explaining the right way to maintain the data.

Someone asks your team to add more logic to a report. Instead, you show them how fixing the data at the source would solve the problem everywhere, and you give them a new exception report to help them easily identify the data fix.

- Someone insists you provide them with access to raw data for an urgent analysis. Instead of just granting permission in the database, you send the data directly to them and help them with their analysis.

- An IT executive wants you to create real-time transaction reports in the data warehouse. Instead, you demonstrate a faster, perfectly real-time approach using the built-in reporting tool in the billing system.

It’s not easy telling a friend that they need to change. They need to trust you, and you need to care enough to help them make the changes. It’s like that when you’re leading a data team. People in your company don’t need more project management; they need change management. When you’re leading a data team, you should make that decision right from the start.

---

Source: [A Data Team Should Drive Positive Change](https://zanehall.substack.com/p/a-data-team-should-drive-positive)
