---
title: "Lessons Learned From America's Massive Data Quality Problem"
subtitle: "Case Study: Musk and Social Security Part 2"
date: 2025-07-01
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/lessons-learned-from-americas-massive
audience: everyone
wordcount: 722
reactions: 0
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Lessons Learned From America's Massive Data Quality Problem

*Case Study: Musk and Social Security Part 2*

![](https://substackcdn.com/image/fetch/$s_!Kh9F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d8b906f-4cf8-4043-bbba-cba4f87be31e_4032x3024.jpeg)
- Wilderness Lodge, Orlando, Florida, June 2025*This article continues my Exception Reporting focus, which you can read [here](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6).*

---

When I wrote last week about the [massive data issues in America’s Social Security system](https://zanehall.substack.com/p/fixing-americas-massive-data-quality?r=4chtg6), I knew I was wading into hot water. Elon Musk [shared a spreadsheet](https://www.newsweek.com/elon-musk-major-social-security-warning-fraud-billion-week-lost-2029244) on television showing some 18.9 million people over 112 years old listed as “alive” in the Social Security system. He then [speculated on X](https://x.com/elonmusk/status/1891350795452654076) that many of these people were still receiving payments.

They weren’t receiving payments, and the unfortunate analyst who shared that data with Musk apparently pulled it from the wrong system. The SSA patched the benefits system years earlier to prevent such payments but didn’t fix the bad data where it started.

The complexities of this problem obviously go way beyond data quality. You’ll find the same thing at most American companies; bad data is usually just the tip of the iceberg. But you need to start somewhere, so I’ll use the chaos in America’s data to show some data quality principles that everyone can understand.

You won’t need any technical knowledge to follow these ideas, and (ironically) that’s the lesson I’ve learned managing technical teams for a few decades. Without applying good business management skills to your data, your technical work could make matters worse.

### Principles for Better Data

Use these simple approaches to manage data quality better:

**Always measure a data problem before solving it**. As I wrote in my Exception Reporting articles, always define the business rules and count the errors before deciding how to fix the data. Data engineers refer to this tactic as "data profiling." It's a discipline that helps you patiently sort through issues and fully understand the sources of bad data. Guessing the causes and their impact (as Elon Musk did) doesn't help people align on the solutions.

Those 18.9 million “exceptions” happened for at least three reasons. DOGE can state each business rule to pinpoint the issues.

People reported “dead” in the government’s Death Master File should not be active in the Social Security system.

- People over 112 years old in the Social Security system should always appear in the Death Master File.

- People reported as “dead” in either system should not receive payments.

**Fix obvious errors first**. Musk rightly followed one of the most basic rules of data quality management: focus on the indisputable issues first. Fixing that data might not solve any immediate problem, but eliminating obvious errors makes the more complex cases easier to find. The real fraud problem in social security is not the 150-year-old people; it's the 77-year-olds who passed into eternity 10 years earlier. Somebody might cleverly adopt their identity and live off their benefits.

Identifying the truly bad data without cleaning out the huge set of harmless data errors is much more difficult.

**Fix the process before modifying the system**. Bad data usually results from a missing or broken business process. Those processes almost always relate to maintaining master data, like people, products, or customers.

Similarly, the Social Security system doesn’t have a process to “reactivate” a person accidentally changed to “dead” in its systems, which creates disincentives to inactivate anyone. If they fix the data but don’t fix this business process gap, the bad data will reappear.

**Beware of confirmation bias. **It's not true that 18.9 million dead people are receiving Social Security payments. Musk fell victim to the common tendency to trust data that confirms your preexisting beliefs. Lots of people think they’re “following the data” without realizing they’ve made a complete leap of faith.

Let the data tell the story instead of assuming it proves your case.

**Collaborate. **Showing bad data on national television makes for good entertainment, but it might not convince the people you need to fix the data to do the work. By capturing good business rules, you can depersonalize data problems and help everyone treat data quality as a shared mission. It might sound quaint, but your most important asset in this effort is the trust of the people you work with. DOGE can’t improve the data permanently without the buy-in from the Social Security teams who manage it.

Like a dentist fixing your cavities, try using these lessons to develop a gentle touch and help your colleagues [fix their data permanently](https://zanehall.substack.com/p/exception-reports-the-power-of-a?r=4chtg6). That’s the secret to avoiding the hot water that bad data can lead you into.

---

 ![](https://substackcdn.com/image/fetch/$s_!Iw-o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1abccc21-f97b-4bbe-9e0e-c34c8695f3eb_2542x463.jpeg) [Buy now on Amazon](https://a.co/d/e7uApb1)

---

Source: [Lessons Learned From America's Massive Data Quality Problem](https://zanehall.substack.com/p/lessons-learned-from-americas-massive)
