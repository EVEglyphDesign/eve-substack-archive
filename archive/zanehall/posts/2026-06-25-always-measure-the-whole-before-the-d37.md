---
title: "Always Measure the Whole Before the Parts"
subtitle: "How to Guarantee Integrity in Large Datasets"
date: 2026-06-25
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/always-measure-the-whole-before-the-d37
audience: everyone
wordcount: 822
reactions: 4
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Always Measure the Whole Before the Parts

*How to Guarantee Integrity in Large Datasets*

![](https://substackcdn.com/image/fetch/$s_!KgpK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8f5a291-9033-4047-a03e-f23a37a89bc5_4032x3024.jpeg)
- ***Frictionless Decisions** brings you counterintuitive, original, jargon-free ideas for connecting data to decisions.  This article is part of my series, [The 00001010 Commandments of Data](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).*

[Share Frictionless Decisions](https://zanehall.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

All the buzz around analytics today might have you convinced that there’s gold buried somewhere in your data. As Billy Beane famously said in *Moneyball *(the story that started the buzz)*, *“We are card counters at the blackjack table. And we're gonna turn the odds on the casino.” But everyone saw the movie, so it’s really a race and you’re worried you might fall behind.

I’ve got news: if you think analytics is mainly about finding "hidden insights," you're wrong.

Business analysts spend a lot more time explaining what happened and why the results don’t match people's expectations rather than finding brilliant ideas. Questions like “We had 1,000 students last year, now we have 1,100. What changed?” or “We booked some big orders this quarter, but our backlog only went up by $100k. What happened?” consume most of their time.

I’ve always used this “Sixth Commandment of Data” to help analysts see *internal integrity* in the numbers. By measuring the grand totals before measuring the different parts of a set of data, you can ensure that the beginning and end points of the numbers agree with (“reconcile”) all the changes in between.

#### Defining "The Whole"

There's no way to explain what changed in your business unless you know how much business you had at the beginning and what you now have at the end. That's what I mean by measuring the "whole": knowing the grand totals of your most important data sets.

For a manufacturing company, it's your customers. What's the value of all the orders on the backlog?

- For a university, it's your students. What's the total number of enrolled students?

- For a SaaS software company, it's your subscribers. What's the value of their active monthly subscriptions?

- If you're managing a warehouse, it's your inventory. What's the value of all the items in stock?

- For any company, it's your people. Measure the total count of employees (headcount).

I call this the "book of business": knowing the total amount (value and quantity) of all the assets you manage. Most analytic questions try to explain what happened between the beginning and ending values of these totals. You can apply this approach to any set of data for your company; the more broadly you define the “whole”, the more questions analysts can answer with the data.

#### Measuring the Change

[When you measure the whole book of business](https://zanehall.substack.com/p/the-pivot-table-that-conquered-the?r=4chtg6),** **you can help analysts answer questions about what changed. You can calculate the amount of the *overall change* before measuring all the different reasons the numbers changed.

 ![](https://substackcdn.com/image/fetch/$s_!cNjC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50a08c1a-89f3-4f07-a67b-5c605ea27df4_1295x641.png)
- Let's say your organization is a university, and you started the year with 1,000 students and ended with 1,100. Take these steps to measure the whole change:

First, calculate the total change: the difference between the total student count at the beginning (1,000) and what you have at the end (in my example, an overall increase of 100).

- Once you know the overall change in the data, you can start to measure the parts and calculate easily defined changes that everyone understands. You added 267 students through new enrollments but lost 128 students through graduation. Everyone agrees on how to measure those numbers.

- But that doesn't explain all the changes; you've got an additional, unexplained drop of 39 students. Maybe that was students who unexpectedly dropped out?

By measuring the whole before measuring the parts, you've "cornered" the unknown changes; you haven’t explained all the changes until all the explanations equal the total change amount.

What I’m showing here is just the normal way analysts think. But embedding that thought process into all the data is how a great data strategy accelerates their work. What's the best explanation for the unknowns? Ask the analysts. Measure the changes like this and they'll figure out what's really happening in the business.

Different industries use different names for the activities that normally change their book of business. In manufacturing, it's "bookings". In SaaS software, it's "churn". In retail, it's customer “retention”. How* *you measure the "whole" depends on your business model, and my simple examples might not describe your industry; a manufacturer can easily measure customer value from hard orders in their system, but measuring customer value for software subscriptions requires more estimation. In any case, following the definitions your company uses to report the financial results usually makes sense.

Defining this "whole" for your company sets the cornerstone for most analytics, and you can apply this approach to almost any type of data. That's why I'm giving you this sixth commandment:

**Always measure the whole before measuring the parts.**

---

 ![](https://substackcdn.com/image/fetch/$s_!J2gz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d684362-3d11-457c-bacc-799a9d9be1fc_900x900.jpeg) To remind you of this week’s data concept, enjoy *[Head over Heels](https://open.spotify.com/track/14zMkyaYN6TGAFwsB69bz6?si=918c4a630e244854)*, by The GoGo’s, from the [Frictionless Data Spotify playlist](https://open.spotify.com/playlist/4PKCEghEMZ7MxCJMwlrnFV?si=b6X-1CP0RXmRNqqQs8AK8A)**.**

---

For the full story about making data flow faster and better, check out *Frictionless Data* on [Amazon](https://www.amazon.com/dp/1637428200?ref=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&ref_=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&social_share=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&bestFormat=true&previewDoh=1&previewDohDeal=1).

 ![](https://substackcdn.com/image/fetch/$s_!RFYI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc83074f5-ac33-4a97-97fc-608268c1c44b_347x522.jpeg)

---

Source: [Always Measure the Whole Before the Parts](https://zanehall.substack.com/p/always-measure-the-whole-before-the-d37)
