---
title: "Always Define the System of Record"
subtitle: "Orlando, Florida, November 2024"
date: 2024-11-19
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/always-define-the-system-of-record
audience: everyone
wordcount: 980
reactions: 4
comments: 2
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# Always Define the System of Record

*Orlando, Florida, November 2024*

![](https://substackcdn.com/image/fetch/$s_!w7Vq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee09c9ae-3376-4275-88ab-d7cc68bec3da_3767x1791.jpeg)
- *(This is the fourth article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).) *

Each of these “Data Commandments” I’m sharing with you reorients your company’s thinking. But this Fourth Commandment – “Always Define the System of Record” – goes the furthest in changing your overall business system landscape for the better.

I want to push you, the data leader, to see your role as a hands-on partner with all the business people you support; I want you to own the *entire* *flow *of data through your company’s decision-making. Don’t use reports to do something business systems should do. Instead, develop your awareness of how business processes and data work together. For you, the data strategist, that means leading “system of record” decisions for your company.

I’ll explain this approach in three parts:

Asking the right questions to your business partners.

- Keeping a record of the answers for them.

- Helping them use the results.

That’s a high set of expectations, and I’ll do my best to help develop your vision.

The greatest cause of confusion in a company’s decision processes is a lack of clarity about ownership. Business teams need your help to know **who **owns the data, **where **that data came from, **what **good data looks like, **how **that data relates to other systems, and **when **other systems don’t match. I call these “system of record” questions.

### Secret Sauce

At Maxim Integrated, we managed part numbers in four systems and customer IDs in three, and nobody knew which system was the master for either one. Finally, we discovered that a spreadsheet was the most authoritative source for part numbers. It took about two years working with the business teams to solve that problem and make the SAP ERP (Enterprise Resource Planning) system the single source of truth for part numbers. 

For customer IDs, we successfully made the distribution system the single source of truth after another two years.

If you ask me for the “secret sauce” of good, overall data quality at your company, I’ll answer with “Always define the system of record.” Every client I’ve worked with struggles with this in some way. 

### Asking the Right Question

I want you to appreciate the consequences of not following this Fourth Commandment.

When there’s no system of record for a data point, everyone tries to resolve data disconnects with reporting logic. Simple disagreements between systems go unresolved, making the reports themselves the “correct” answer for key numbers. That forces everyone to pick which report they trust. Without a system of record for master data, trying to align metrics is a losing battle.

Use these three overall guidelines to help establish systems of record for all your data:

***Always ask the question.***** **

“What’s the system of record for that data?” Any time you’re discussing a question about the logic for a metric, asking this question leads to a better decision. 

When Maxim started working to make SAP the system of record for part numbers, we found that both SAP and the quality control (QC) system tracked “heat grade”, and the systems didn’t always agree. Instead of writing report logic to decide which value to use, the product maintenance team agreed to make SAP the system of record for that field. Then they agreed to use an exception report to fix every value in the QC system that didn’t match SAP. 

That made it so reports could simply take the value from SAP. If someone found an incorrect value, they discussed it with the QC team. Writing report logic to interpret data will always take less time, but it never solves the underlying problem. Whatever the final decision, you’ve helped everyone by at least considering the root cause.

***Keep a record of the answers*****. **

Maybe you’ve heard the term “data dictionary”. That’s exactly what you’re creating when you document the decisions you make about the system of record for your data. We documented that “heat grade” decision by showing which field the reporting system would use when the source systems disagreed. 

A good data dictionary declares a winner, and that’s what makes a system of record decision effective. A data dictionary doesn’t simply give you a description of the data, it tells you which system, table, and field is the authoritative source. Everyone who works with data at your company benefits from this reference document. They will thank you for it because someone finally took responsibility for getting business alignment at a detailed level. 

This opens the door to a world of good data quality management. Once you’ve started documenting the rules like this, you can immediately start using “exception reports” to help business teams close the data gaps between systems.

***Materialize the data.***** **

People will embrace your solution because you’re making their job easier. Instead of writing piles of code to resolve conflicts between source data, they will adopt the source you provide that uses all the rules from the dictionary. At Maxim, the most popular reports we ever wrote were simply the lists of parts and customers. Everyone knew that those reports weren’t simply useful but that they reflected all the decisions they’d made about the system of record and data quality rules.

By “materializing” the data, I mean that you create a data source (a table) that everyone can use and reference. Make this source available to all the business teams at your company, with no security limitations. Publish this data in the most accessible format available. Encourage IT teams to use it in all their applications. By doing this, you save work for people across the company. Educate people, listen to their use cases, and help them use it for all the reports they write.

That’s how a good data strategy makes all the difference: helping people understand – and use – the “system of record” for all the data.

---

Source: [Always Define the System of Record](https://zanehall.substack.com/p/always-define-the-system-of-record)
