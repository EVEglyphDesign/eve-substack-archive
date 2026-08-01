---
title: "Always Enforce Cell Level Security"
subtitle: "The 00001010 Commandments of Data part 9 of 10"
date: 2025-04-08
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/always-enforce-cell-level-security
audience: everyone
wordcount: 1058
reactions: 0
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Always Enforce Cell Level Security

*The 00001010 Commandments of Data part 9 of 10*

*(This is the ninth article in my series, “The 00001010 Commandments of Data”. You can read the introduction to this [series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).)*

This ninth commandment of data might seem the most technical, but it's not about technology. When I say you should always enforce cell-level security, I’m describing a way to give people access to data in the most precise way possible.

To make your organization’s data the most secure, you’ll need to know two things about the people who use the data: what rows they need to see and what numbers they need to see for all those rows. By combining these two inputs, you can give people the greatest possible access to the data yet make it the most secure.

### Better Access, Better Security

I’ve yet to find a single company that manages data security as effectively as I’m about to explain. Your IT department might tell you they have this under control, but it’s probably not working as I’ll describe. Most data teams say they support RBAC (role-based access control) before admitting that the “all access” job role has the most members. Even if your security policy says all the right things, almost anyone can access all your data.

Digging into a data security solution to find these gaps can get technical quickly, so I’ll give you a few questions to help reveal how well things are working beneath the surface.

- Do people constantly come to your IT team asking for data? If so, you’re probably not using job roles very well.

- How often do people internally email large sets of data to each other? If so, the system probably isn’t giving people easy access to what they need for their jobs.

- Does your team maintain permissions directly on reports? If so, you’re probably not managing access as efficiently as possible.

- Does updating a person’s data or reporting permissions require multiple changes and tickets? If so, you probably haven’t consistently defined people’s roles for your company's different kinds of jobs.

- Is copying one person’s access profile to another person a normal approach for giving people access to data? If so, you probably haven’t given business people full control of the job role definitions.

All these symptoms expose the underlying problem with your security solution: you don’t know what data people need to do their jobs. Providing and protecting data requires understanding the people, not just the data. You need a two-dimensional solution.

### Rows, Columns, and Cells

Business analytics data is two-dimensional - it’s almost always structured in tables, with rows and columns. In IT shorthand, that’s called “tabular” data, and it works a lot like the classic board game *Battleship*. Rows are sometimes called "records," and columns are different facts about the records. A column and row intersection is called a “cell.” Using my example below, if I ask you for the value of cell B2, the correct answer is 26.

 ![](https://substackcdn.com/image/fetch/$s_!m2xr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9efaf3fc-1cac-458a-aecd-ac668263a37e_419x126.png) When I say you should “secure” data at a cell level, I’m explaining that you should give people only the data they need for their job, nothing more and nothing less. If they need to see column B for their job but not column C, don’t give them permission to see both. On the other hand, if they need column B for their job, they should see that information for every row in their business data. That’s the most precise (or granular) security level possible.

Now, let’s use a table of sales order data, for example:

 ![](https://substackcdn.com/image/fetch/$s_!xw5d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43fccf30-0f08-4e3c-b86b-5597c17df7b3_820x163.png) Each order is a row (or record) in the table. Key information like the customer region or the product name helps us know who needs those records for their job. A sales rep responsible for the Central US sales region doesn’t need to see orders from the Western US or Europe. They need to see prices for every order in the Central US, but they don’t need to know the cost of the products.

> That’s what cell-level security does: it controls both the rows and columns people need to see.

Without this awareness of what rows of data people need for their jobs, IT teams find lots of clumsy ways to secure the data. Some grant access to entire tables, while others control access to reports that pull data from the table. The first approach grants too much access to the data (every row and column in a table), while the second grants too little (only the rows and columns included in the report). Cell-level security gives people exactly what they need, no more and no less.

### Success Factors

Surprisingly, a good cell-level security solution makes managing people’s data access much easier. Three factors make the difference: full business ownership of the decisions, good data classification, and a simple, single-point of maintenance.

- **Business ownership.** Cell-level security requires two types of permissions, not one, and that nuance keeps most IT teams from implementing this solution properly. Business people have the management authority to decide what data people in different job roles should see.

- **Good data classification**. As you can see from my example, [a good data warehouse makes data easier to find](https://zanehall.substack.com/p/always-warehouse-the-data-first?r=4chtg6) and easier to secure. Master data is the most straightforward way to identify the data people need for their jobs.

- **Single point of maintenance**. The complexity of assigning permissions at the intersection of columns and rows forces you to manage all the permissions in one place. That “one place” should always be the data warehouse. Using a single point of maintenance also means only allowing one role per person. Cell-level security doesn't work if you allow people to have multiple job roles.

Here’s an irony: the more granularity you use to make data accessible for people inside your company, the more you protect it from outsiders. When everyone gets exactly the data they need for their job - without even asking for it - it’s like creating a thousand layers of security instead of just one. You’re not giving too much or too little access, and because of that, nobody has a reason to circumvent the security.

Today**, **I’ve shown the technical side of this security solution, but you might wonder, “Who makes the decisions about what data people get to see?” Next week, I’ll explain that, showing how this approach helps business and IT leaders partner together in a way that you’ve probably never seen before.

---

Source: [Always Enforce Cell Level Security](https://zanehall.substack.com/p/always-enforce-cell-level-security)
