---
title: "Always Warehouse the Data First"
subtitle: "Minneapolis, February 2025"
date: 2025-02-04
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/always-warehouse-the-data-first
audience: everyone
wordcount: 1095
reactions: 4
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Always Warehouse the Data First

*Minneapolis, February 2025*

![](https://substackcdn.com/image/fetch/$s_!NJVH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fe45e49-0796-45d5-9e6e-33983114eee7_5712x4284.jpeg)
- *(This is the seventh article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).)*

When I say you should “Always warehouse the data first,” I'm making a simple point: a data warehouse is a warehouse. When you manage data in a warehouse, your company gets a lot more value from its data.

It's helpful to think of a "data warehouse" in non-technical terms, just like a physical warehouse. Take an Amazon distribution center, for example. The way the global supply chain makes same-day delivery possible is[nothing short of a modern miracle](https://youtu.be/1KtTAb9Tl6E), fully accelerated by technology. However, the fundamental ingredient that makes all this possible is Amazon’s decision to anticipate what products I'll need, keep them ready in a central location (a warehouse), and make them easy to find and deliver when I need them. That warehouse allows me to live my life differently: I don't carry an extra power supply in my backpack because I know I can get one delivered to my doorstep on the same day I order it.

Just like a physical warehouse makes my own life more productive, a data warehouse changes the way everyone at a company works with data. It keeps data fresh, makes it easy and fast to find, and readily available for many different uses. It’s an upfront investment that accelerates everyone else’s work.

 ![](https://substackcdn.com/image/fetch/$s_!NR8J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4277b9b7-d3d0-4387-a182-b8812ce058ac_296x501.png)

#### Warehouses Add Value

By managing data in a warehouse, you can offer people many more tangible and intangible benefits (“services”) that they value even more than the data itself.

Here are seven services that a good data warehouse provides:

**Data Dictionary. **A data dictionary documents the relationships between systems and declares a winner when they don’t match, reinforcing the system of record for key data points. I call this a “system of record” capability, and it helps everyone at a company by eliminating the need to resolve differences on their own.

- **Cataloging. **A catalog describes and classifies data to help people find what they need, but more importantly, it helps your company secure the data. You can’t secure what you can’t classify.

- **Subscriptions. **The data warehouse syndicates data to other systems, saving work for developers and making master data consistent across all systems. If an employee changes her name (for example), every system in the company will immediately receive that update from the data warehouse, synchronizing master data throughout the company.

- **Exception Reporting. **Exception reports apply business rules to the data and send the bad records to the data owner for correction. This service improves overall data quality across the entire company.

- **Flow Control. **The data warehouse team manages the “service bus,” a term that describes the governance of data movement between systems, databases, and people, both internal and external. This helps standardize which solution should be used in different situations.

- **Retention. **The data warehouse retains data according to policy and maintains continuity across time. Data represents a company's memories, and your data warehouse adds value by keeping those memories safe.

- **Migration**. A data warehouse makes it easy to populate a new system with data from the system it replaces. This service helps a company upgrade or replace its business systems by providing an easy validation capability and insulating reporting solutions from business system changes.

#### Building a Data Warehouse

Have you ever gotten lost at a Costco Warehouse? It’s a huge space with more products than you’ll ever need, but thankfully, they store the items you’re looking for in a logical system of aisles and shelves, which - usually - makes your shopping trip easy. A physical warehouse isn’t just a building where you dump a large pile of goods; it’s also a preset design to *organize and manage *all the inventory.

It’s the same with a data warehouse: it’s not just a database. The value of your data warehouse depends on how effectively you plan and manage it. I don’t expect you to know everything it takes to create a good data warehouse just from my simple advice, but I’ll give you a few high-level “best practices” to guide your thinking on this. Together, these practices form the “aisles and shelves” of a good data warehouse.

- **Store *****all *****the data**. A common mistake in many solutions is storing only the data you need for metrics people request. Similarly, some solutions summarize or eliminate details when they store the data. These obvious shortcuts don’t store the data you’ll need for future projects and decisions.

- **Store the data in its natural form**. This usually means storing data in a structure similar to the source it came from but using standard warehouse naming conventions. A typical data storage mistake is to “flatten” the data. If a customer has three shipping addresses, you should store three records, not one record with three columns. Theorists call this mistake “de-normalizing” the data.

- **Store the data with its natural relationships**. When you store shipment data (for example), each shipment record should reference the sales order it came from. Don’t make people figure that out on their own.

- **Store the data with common master data**. Even though your business systems might keep customer information in four different places, you only serve one customer. That’s a problem data warehouses solve by using a single, overall system to categorize the data. Storing transaction data with references to common master data makes the data easy to find and join with other kinds of data.

- **Use good semantics**. The names, formats, and abbreviations you use for tables, columns, and databases work like the aisles and shelves in a warehouse. Using understandable, standard naming conventions throughout the system makes it easy to find its contents. Using good semantics from the start creates a “self-documenting” process for the warehouse contents.

#### Manage Data Like It’s an Asset

Most people agree that data is an important asset. But if you haven’t experienced working at a company that makes the most of that asset with a good data warehouse, you might not recognize how much it changes how everyone works. A senior executive I worked with told me, "I used to view data only as an input to my department's decisions, something to download to a spreadsheet. But now I'm convinced that data is a strategic asset for decisions throughout the company, not just a raw input for us."

Seeing a good data warehouse in action like this shows the power of a data team that takes responsibility for all the data needs of their company. That’s the point of this Seventh Commandment of Data:

**Always warehouse the data first.**

---

Source: [Always Warehouse the Data First](https://zanehall.substack.com/p/always-warehouse-the-data-first)
