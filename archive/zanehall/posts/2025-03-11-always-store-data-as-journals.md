---
title: "Always Store Data as Journals"
subtitle: "00001010 Commandments of Data, part 8"
date: 2025-03-11
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/always-store-data-as-journals
audience: everyone
wordcount: 716
reactions: 0
comments: 0
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# Always Store Data as Journals

*00001010 Commandments of Data, part 8*

![](https://substackcdn.com/image/fetch/$s_!MDnW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81e5286e-8f99-4cbd-80ba-deacd101820e_5712x4284.jpeg)
- *(This is the eighth article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).)*

Hundreds, thousands, or even millions of changes occur daily in a large company's data. But which changes matter for your strategic decisions? If you think the answer to that question explains the purpose of all business analytics, you’re not far from the truth. A good analytics solution helps people quickly and easily find the most critical changes in the data - the needles in the haystack.

When I say you should store data as journals, I’m explaining how to use double-entry accounting ([which I just wrote about last week](https://zanehall.substack.com/p/the-ancient-idea-behind-analytics?r=4chtg6)) to make the most important data changes obvious to people. That's the reason for this eighth commandment: a good data strategy should find the changes that matter most and store them.

I want to warn you right up front: this solution might seem like a subtle technical feature that only a data nerd would care to understand. If you think that, you’re right. But if you’re looking for the secret sauce that makes an analytic solution great, this is it.

> Data teams can compare huge sets of data to previous versions and quickly find what changed, and they should use that capability to help analysts make better, faster decisions.

### Journaling What Matters

Every day, I keep notes in a journal, just a few sentences to remind myself of important events. A good analytic solution does the same for your business: it finds the changes that matter most to analysts and makes them easy to access.

Journaling means something different to business analysts than it does to accountants or database administrators. DBAs protect the data by logging every change to a database, no matter the reason or impact. On the other extreme, accountants only care about changes that impact financial history. Analysts don't care about every data change, but they care about a lot more than just the accounting impact. They care about a company's financial history *plus *any change that could impact future business results.

If you don’t use this double-entry approach in the data sets you publish (which I’ll explain next), then every analyst will repeat this effort manually whenever they need to find out what changed in the data. That adds an enormous amount of extra work to every decision - work that a data team can eliminate. If you’re an analyst or a data manager, think through my examples below and see if I’m right.

### Squeezing and Storing

Here’s an example of how your data platform can find and store key changes as journals. I call this process "squeezing" out the changes.

Let's say you have 1,000 orders in your system. On any given day, not all of the orders change. Analysts don't want to wade through 999 orders to find the one that did change. Here’s an example of how storing the changes as journals makes that change easy for analysts to find and use:

 ![](https://substackcdn.com/image/fetch/$s_!jsSg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9562d85-a070-4493-bf7c-4e8cfa4ee2c7_859x377.png)

Here are the steps the data platform uses to highlight those changes for analysts:

Find the record that changed - in my example above, order number 1000456 was updated on 2/5/25.

- Insert a new record to reverse the original order details (updated date 2/5/25).

- Insert a new record with the updated order details (updated date 2/5/25).

- Repeat steps 1 to 3 for every change, as shown for 2/28/25.

The two new records combine to show the net impact on sales amounts. That’s a zero-impact change overall, but it's a big shift to *quarterly *order totals.

People might make a dozen changes in the business system to an order in a single day. But the only change that matters for analysts is the value of the order at the end of the day today compared to the same order at the end of yesterday.

### Make Finding Needles Normal

Squeezing out the changes like this guarantees you'll always get the perfect amount of detail for any changes. Don’t make every analyst at your company spend their days hunting for the changes that matter. Take time to understand what changes they need to see for their decisions. Learn that, and you’re ready to make the most of the data with this eighth commandment:

**Always Store the Data as Journals.**

---

 ![](https://substackcdn.com/image/fetch/$s_!ie9H!,w_56,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e996c26-a2d9-43d3-8ea3-285f7f9635d4_900x900.png) Frictionless DataThe Ancient Idea Behind AnalyticsYou probably don’t realize it, but an obscure 15th-century Italian monk named Luca Pacioli invented the world’s best data strategy, which is still the foundation for analytics today…Read morea year ago · 4 likes · 4 comments · Zane Hall

---

Source: [Always Store Data as Journals](https://zanehall.substack.com/p/always-store-data-as-journals)
