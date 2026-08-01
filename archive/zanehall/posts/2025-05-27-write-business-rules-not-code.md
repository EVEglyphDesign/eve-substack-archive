---
title: "Write Business Rules, Not Code"
subtitle: "Exception Reports, Part 3"
date: 2025-05-27
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/write-business-rules-not-code
audience: everyone
wordcount: 1013
reactions: 0
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Write Business Rules, Not Code

*Exception Reports, Part 3*

![](https://substackcdn.com/image/fetch/$s_!ABoN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb42a8904-9e59-4694-b633-2fb313b97090_5389x3400.jpeg)
- North River Ranch, Florida, May 2025*This article is part of a three-part series on “Exception Reporting,” my counterintuitive approach to improving data quality. Follow these links to parts 1 and 2 here: here: [Exception Reports: An Origin Story](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6) and [Exception Reports: The Power of a Simple Solution](https://zanehall.substack.com/p/exception-reports-the-power-of-a).*

---

The CEO was upset. Purchase orders for all kinds of small stuff (like laptops and uniforms) had suddenly filled up his inbox, waiting for approval. Clearly, the purchasing system was broken. However, our CFO (who knew all about my data strategy) saw an opportunity to use our new Exception Reports tool.

The purchasing system wasn’t broken, but the data it used was wrong. When a manager left the company, the HR system didn’t update people’s supervisory relationships; that was a manual task. If the HR person making that update didn’t compare the signature authority level of an employee to their new boss, the system would send requests to the next person up the supervisory chain with a higher level authority. The CEO became the catch-all for approval requests from everyone with an errant signature authority value.

Just as the IT team started writing new code in the purchasing system to fix this, my boss called a quick timeout and asked if an exception report could solve the problem.

When we showed the problem to the HR manager, we’d hardly finished explaining it when she told us the rule: nobody should have a signature authority level greater than their boss. My team translated that rule to a SQL statement, and she got a report the next day. We discovered that another 17 people also had this problem! We were just lucky that they hadn’t used the system to buy anything lately.

That anecdote shows a critical mindset shift: let business people own the data. Give them a way to create and measure business rules. Data engineers want to use their technical skills to improve data quality, but before you write more code and before you fix any more data, understand how to define business rules.

And that’s what I want to show you today.

### Business Rules: The Heart of Exception Reporting

You can't identify bad data unless you first define what good data looks like, and a business rule is a specific definition of how things *should* work.

Business rules are not value statements, like "employees should respect each other." Instead, they’re specific rules about the data with a true or false result. A good rule translates easily into simple Boolean logic, with obvious “IF / THEN” operators that database queries understand.

You can think of business rules like this:

Data should not be missing.

- Data should match a list of acceptable values.

- Data should not be out of date.

- Data should be above or below a threshold.

- Data that should be the same in different systems is the same.

A business rule isn't technical; people should always describe the data problem in plain, concise language. For example...

- Product heat grades should always be stated in Celsius.

- Every customer should be classified by market.

- A customer’s market category in SAP should match the value in Salesforce.

- A film should not be marked as “Family” if it has over a PG-13 rating.

Business rules reflect a fundamental principle of Total Quality Management, the revolutionary, data-driven manufacturing strategy pioneered by W.E. Deming in post-World War II Japan. In his book *Out of the Crisis*, Deming says that understanding variation is the only way to [avoid relying on massive inspections to find quality issues](https://en.wikipedia.org/wiki/W._Edwards_Deming#Key_principles). Just the title of Deming’s book perfectly describes the terrible feeling everyone gets when they don’t have a plan to overcome their data quality problems. They need to find a way out of the mess.

If you don’t define “good” data first, you can only find “bad” data by checking everything manually. You’ll work in crisis mode for a very long time.

### Improve Quality Over the Long Run

That explanation of business rules should sound straightforward, but there’s a twist. You can’t know all of your company’s business rules when you first set up a system. There’s no way software designers can anticipate every situation people using the system will face. Instead, they discover and define business rules over time as their business process matures and their company grows.

And here’s an amazing bonus: business rules don’t just help you fix bad data, they can also help you proactively make mass changes to entire data sets.

Say your business grew to 10,000 customers in the Eastern U.S. sales region. You plan to hire another sales manager, so you’ll need to split that region into two. Instead of handing that data problem over to your IT data team, you can write a business rule that defines which cities and states make up that new sales region and easily see what customers need to move. At first, every single record is an exception to the new business rule. But maybe the number of affected customers is fewer than you guessed, and business people don’t need to wait for IT to write programs to update the data.

Think about how much friction this removes from business decisions. When people need to change a large dataset (like my example), they usually freeze up and wait for IT help. By measuring the business rule first, you discover the scope of the change and help people find easier solutions. Your colleagues may realize they could update the data manually instead of waiting for IT project approvals and development cycles to move forward.

> Most data changes—even updates to whole data sets—shouldn’t have to wait for IT to make software changes.

That’s exactly what happened with the purchase order problem. The business rule showed that the problem was bigger than anyone knew, but not so big that the HR manager couldn’t immediately fix all the data. She fixed not just the HR data but also the purchasing system – all without writing any code.

When people see how data connects the business, they solve problems without IT help. The key to that connection? Business rules that connect the data.

---

Source: [Write Business Rules, Not Code](https://zanehall.substack.com/p/write-business-rules-not-code)
