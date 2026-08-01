---
title: "Exception Reports: The Power of a Simple Solution"
subtitle: "Exception Report Series, Part 2"
date: 2025-05-13
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/exception-reports-the-power-of-a
audience: everyone
wordcount: 969
reactions: 3
comments: 4
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Exception Reports: The Power of a Simple Solution

*Exception Report Series, Part 2*

![](https://substackcdn.com/image/fetch/$s_!lQXr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb845efc0-c097-4fdd-809a-fada03bb980a_5712x4284.jpeg)
- *This article continues my three-part series on “Exception Reporting,” a counterintuitive approach to improving data quality. Read the first and third installments here: [Exception Reports: An Origin Story](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6) and [Write Business Rules, Not Code](https://zanehall.substack.com/p/write-business-rules-not-code).*

---

As I neared the end of my presentation, speaking to an audience of a hundred IT workers, I suddenly had everyone's full attention.

All-hands meetings for IT teams might be the driest stuff you could ever sit through, so this took me by surprise. I was the last speaker, and I finished my talk by explaining how Exception Reports worked.

I explained that Exception Reports give people a real strategy to fix data permanently. My simple solution didn’t depend on technology; instead, I showed them how to set up an ongoing business process that helped people improve their data every day. We needed this because even though people might care enough to fix the data problems that get in their way, they usually don’t try to fix *all *the bad data in the system.

“They don’t think it will make any difference. They don’t think their work will matter to anyone.” I said.

I think I saw tears in some of their eyes. After all, IT people want their work to make a lasting impact, just like anyone else.

Why don’t people fix bad data? Maybe they're overwhelmed because there’s so much of it. Maybe they’re afraid of unknown consequences or don't know how to fix the problem. Maybe they don’t know who should fix it. And with no plan to fix all of it, they know the truth: nobody cares.

I’ve got a plan, and I know it works: Exception Reports.

An Exception Report takes a business rule, applies it to all the data, notifies the data owner of the errors, and tracks their progress in fixing the data. Last week, I told you the story about how [my boss and I developed this solution](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6), and today, I’ll walk you through the process of creating an Exception Report.

### A Step-by-Step Guide

Here's how the Exception Reporting process works:

**First, somebody states a rule in plain language, usually in one short sentence.** For example, “Every employee should be assigned a department number.” That might sound simple, but beware: this is the hardest part of the process. (I will cover this in part 3 of this series.)

- **Second, identify the rule owner.** Every business rule must be assigned to a specific person who knows how to fix the bad records. If the person asking for the Exception Report can’t name the owner, put the request on hold until they do.

- **Third, translate the rule into a database query.** A data team can easily convert a well-defined business rule into a SQL statement.

- **From this point, the system takes over, emailing the rule owner a list of records that violate the rule every day**. When the number of bad records hits zero, the owner no longer receives emails.

Setting up a new Exception Report like this only takes a few minutes. When people discover a new business rule, they should expect to receive notifications the next day.

You don't need to buy software to set up a good exception reporting capability like this; it's best to create the tool directly in your existing data warehouse. You'll need three tables (rules, subscribers, and logging) and a daily job schedule to run the rule, log the count, and mail the output to the data owner.

### A Sticky Solution

Exception Reports give people a real strategy for making their work stick.

Exception Reporting tracks errors over time (as shown below) and gives executives a view of people’s progress. People get credit for their work. Once they eliminate all the bad data (shown by the green zeroes), their exception report becomes an alert system, helping them recognize and fix new errors before they destroy a report or some other business process.

 ![](https://substackcdn.com/image/fetch/$s_!-q95!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1a4506d-6555-491c-9380-2bd1a06636f1_970x190.png) Think about the power of this “metadata” (data about your data). Measuring hundreds of business rules simultaneously, like Broadcom and Maxim did, creates a brand-new capability: everyone sees (visually) where your company’s overall data quality stands.

My simple solution assumes you have all the data from source systems in a data warehouse, but don't worry if you don't have lots of raw data stored there already. When people recognize how helpful they are, Exception Reports [will make your data warehouse a magnet for more data](https://zanehall.substack.com/p/always-warehouse-the-data-first?r=4chtg6). People ask you to add more data to it because they know their data will get cleaned up, not just stored for later use. IT people call this phenomenon "data gravity."

You might wonder why every company doesn’t use Exception Reports like this. The sad reality is that almost all business leaders just want to spend money to solve data problems. They pitch massive “transformation” projects that replace entire software systems instead of managing the data better. I’ve seen multi-million dollar projects that could have been avoided with Exception Reports. Those leaders fail to enforce business rules and don’t hold people accountable for fixing the data. IT teams install the new system, then move on to the next project and don’t focus on data quality. Again and again.

If you think I’m on a mission to change this situation, you’re right. I was lucky enough to have support from executives at Broadcom and Maxim who saw this vision and cared about data quality. People saw they cared, which didn’t just lead to better data quality but also better quality of life for the people doing the work. Executives with a vision like that are rare.

People need a plan to improve data quality that makes a real difference. What’s the best way to know you’ve changed that story? When people see bad data, they know what to do.

They ask for an Exception Report.

---

Source: [Exception Reports: The Power of a Simple Solution](https://zanehall.substack.com/p/exception-reports-the-power-of-a)
