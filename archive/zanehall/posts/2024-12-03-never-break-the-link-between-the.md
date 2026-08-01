---
title: "Never Break the Link Between the Business Activity and the Metrics"
subtitle: "Huntington Beach, CA, December 2024"
date: 2024-12-03
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/never-break-the-link-between-the
audience: everyone
wordcount: 703
reactions: 3
comments: 2
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# Never Break the Link Between the Business Activity and the Metrics

*Huntington Beach, CA, December 2024*

![](https://substackcdn.com/image/fetch/$s_!QXAJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0abdd640-9bdb-4272-ba4b-293f26c5cca7_5712x3456.jpeg) *(This is the fifth article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).)*

A good data strategy helps people make better decisions by making it clear what’s really happening in their business. It draws a direct line between the decision-making data and the operational data.

I call this “good lineage”.

You’d be surprised how easily metrics get disconnected from actual business activity. Good lineage doesn’t happen naturally, so you’ll need a plan to help everyone stay on course. That’s why I’m giving you this Fifth Commandment:

*Never break the link between the business activity and the metrics.*

### More Logic, Less Clarity

One client had a metric that measured daily sales. In the minds of the customer service manager and the sales team, the definition was simple: daily sales equaled the total dollar value of all new orders entered into the sales system during the prior day (Pacific Time). That’s how the reporting system measured things, way-back-when. By the time I got involved years later, that relationship was no longer clear.

We discovered that, a few years earlier, a customer placed a large order a year before they wanted it delivered. That confused the finance team, because they used the data to forecast the next-quarter’s revenue.

Instead of reacting to this unexpected data by forecasting further into the future, the finance team told IT to “improve” the logic for the sales metric. They only wanted to count orders with delivery dates within the next thirteen weeks. That logic caused new, large orders to disappear from the sales metric, only to reappear unexpectedly when the calendar changed and the delivery date fell into that thirteen-week range.

That confused the sales team, because the metric mysteriously recalculated, even when they hadn’t entered any new orders.

Imagine if your bank account balance dropped unexpectedly when you hadn’t spent any money, or jumped up dramatically when you didn’t expect it. Unexpected changes are fine when you’re playing Monopoly; at least you can see that you landed in jail or on “Go”. But in this case (years later), nobody remembered the logic “enhancement” and nobody could explain why the metric changed. Untangling that logic was especially difficult because the programmer who created the knot in the first place left the company a decade before. Making matters worse, the source data passed through half a dozen systems before it got to the dashboard.

Eventually the sales team lost trust in the data and created their own reporting system.

### Good Lineage

The real challenge for a good data strategy is keeping people from constantly “improving” the metrics. Metric definitions usually trend toward meaninglessness when people add more and more logic to the system.

I used the terms “metric” and “data” interchangeably as I explained this problem, because data easily gets disconnected at any and all points as it moves from the source system to the dashboard.

In my first job as an analyst at Disneyland, the most important data was theme park attendance. The CFO had an LED display on his desk that measured attendance in real-time: every time someone walked through a turnstile, the number would change like a slot machine. There’s no better picture of good lineage than that.

Later at Broadcom, Ken Venner (CIO) wrote this principle as a formula on a whiteboard:

> **Operational Change = Metric Effect**

This equation explains how good lineage makes decisions flow smoothly through a company.

Once at Maxim Integrated, a customer service agent entered too many zeros for the price of an order ($1,000.00 instead of $1.00). When the system delivered the sales metric to executives a few hours later, some people got excited that the company just had its biggest sales day ever (by a factor of 1,000). But the CFO contacted the customer service manager, who had already found and corrected the mistake. Things got fixed quickly and nobody contacted IT.

That’s good data lineage.

Adding more logic to the metrics might sound appealing, but if you’re not careful, that could unintentionally set decision-making alignment back a few steps for your company.

Instead, stick to this Fifth Commandment of Data:

**Never break the link between the business activity and the metrics.**

---

Source: [Never Break the Link Between the Business Activity and the Metrics](https://zanehall.substack.com/p/never-break-the-link-between-the)
