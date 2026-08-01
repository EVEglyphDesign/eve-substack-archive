---
title: "Use Hierarchies to Help People Understand Data"
subtitle: "00001010 Commandments of Data"
date: 2025-04-22
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/use-hierarchies-to-help-people-understand
audience: everyone
wordcount: 851
reactions: 1
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Use Hierarchies to Help People Understand Data

*00001010 Commandments of Data*

![](https://substackcdn.com/image/fetch/$s_!OdI8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65311cf9-cc25-4870-b4b2-ebae79f55810_4032x3024.jpeg)
- Brooklyn, NY, Easter 2025*(This is the final article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).)*

Have you ever seen the massive spreadsheets some companies use to manage their data?

I’ve seen situations where incredibly important reports came from workbooks with 40 or more tabs. Their huge file sizes (sometimes over 50 megabytes) and thousands of formulas made them unbearably slow. They also tortured the underappreciated analysts who put them together manually. Usually, someone downloads mountains of transaction data into one spreadsheet tab and uses the rest of the workbook to categorize the data with custom lists and lookup formulas.

Why do people do this? Because their data team forces them to.

When nobody takes responsibility for managing the categories used to summarize the data, people create them independently. They work in silos.

### Vertical Data

I want to help you connect your data to your company's decision-making processes. Data leaders - CIOs, CFOs, data architects, and analysts – need to understand how their company thinks and then shape their data to match it. That’s why I’m giving you this tenth commandment:

> **Always use data hierarchies to align the business.**

People analyze data from different points of view. Take geography, for example. A “hierarchy” creates totals and subtotals within that perspective, like city, county, state, country, and continent. The city where I live has a population of 57,000 people, and that’s part of the 23 million people in Florida and the 340 million in the USA. When people discuss the population data, they share a common understanding of what these groups mean.

Similarly, the hierarchy levels you build for products (like product lines, business units, and divisions) shape how people in your company think about your business. Unlike the geography of the United States, however, decisions about how to use hierarchies in your company often get ignored, creating chaos for everyone.

If you don’t help them, people design their own hierarchies with massive spreadsheets.

The image below shows how a manufacturing company can use a hierarchy to group products:

 ![](https://substackcdn.com/image/fetch/$s_!FDzi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe951d0f3-4260-4f9f-a062-dc80a8033f42_1075x526.png) Business processes (like purchasing and shipping) use *horizontal *product data for manufacturing. In contrast, decision-makers use *vertical* hierarchies to understand what’s happening in the business at a higher level. The vertical levels aggregate data into larger buckets: product IDs group into product families, product families fold into product lines, and product lines roll up to business units.

### **Taking Ownership**

When I started working in analytics 25 years ago, I knew that making sense of different types of customers was critical for decisions. So, every Friday, I spent two hours sorting all of my company’s customer data alphabetically and grouping all the locations of large customers (like Cisco) into a single “parent” customer record. Of course, this simple idea grew into more sophisticated designs for analyzing customer data, [which I wrote about recently](https://zanehall.substack.com/p/sales-teams-need-data-not-reports?r=4chtg6).

My team applied these parent mappings to all the data. These hierarchies worked great for subtotaling data on executive reports; the output looked like magic to decision-makers. Nobody had to do this sub-totaling independently, and everyone benefited from consistent views of customer data across all the data and every executive's view of it.

I did this manually for a few years until the Customer Service team took ownership of the master data hierarchies. They made linking customers to their parent customer ID part of their normal “onboarding” process. That allowed us to start adding new categories to the parent records themselves. Many business processes (like new product introductions) started using those higher-level customer names in their workflows, massively accelerating the planning process.

### **Shaping Thought**

Here are some important “best practices” I’ve learned about data hierarchies:

**Listen**. The categories executives use to discuss the business are usually the best for management reporting, so listen to how they publicly describe their business and apply that to the data. Once, in an all-hands meeting at my company, the CEO explained a new customer service strategy that recognized the differences between “whales, tunas, and anchovies.” Suddenly, my team saw the best way to group our customer data.

- **Consolidate**. Strictly limit the number of hierarchies you use for the same data (like products or customers). Sometimes, IT teams make things worse by creating new “alternate” hierarchies whenever their business partners ask for a new view of the data. That defeats the purpose of hierarchies: aligning how everyone understands the business.

- **Share**. Publish the data for everyone to use. Make master data hierarchy data easy to access, not just for people creating reports, but also for IT applications. My teams created a database table for the data that anyone could access, then published an MS Excel report (updated daily) for spreadsheet users.

You can help your company by managing how people understand the data. It’s one of the most powerful ways a data leader influences company decisions – streamlining the thought processes of the entire company. Software alone can’t translate the thoughts of your leaders and managers into data. That’s why I’m giving you this tenth (and last!) commandment:

**Always use hierarchies to help people understand data and align the business.**

---

Source: [Use Hierarchies to Help People Understand Data](https://zanehall.substack.com/p/use-hierarchies-to-help-people-understand)
