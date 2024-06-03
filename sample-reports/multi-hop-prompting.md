# Multi-Hop Prompting in Advanced Reporting

Multi-Hop Prompting is an advanced prompt engineering technique that breaks down complex topics into manageable subqueries. This approach allows for a more detailed and comprehensive exploration of the subject matter by tackling it in stages.

## Example: The Future of AI in Smart Cities

Generating a report on "The future of AI in smart cities" might involve the following steps:

1. **Initial Query**: Start with a broad query on the role of AI in smart cities.
2. **First Hop**: Break down the initial query into subqueries focusing on specific applications of AI in smart cities, such as traffic management, energy efficiency, and public safety.
3. **Second Hop**: For each application identified in the first hop, generate further subqueries to explore current technologies, ongoing projects, challenges, and future prospects.
4. **Synthesis**: Combine the insights gathered from all hops to construct a comprehensive report that covers the initial query in depth.

This multi-hop approach ensures that each aspect of the complex topic is thoroughly investigated, leading to a report that is both detailed and insightful.

```json
{
  "query": "The future of AI in smart cities",
  "primary_prompt": "Generate a detailed report on the future of AI in smart cities, focusing on applications such as traffic management, energy efficiency, and public safety. The report should include an analysis of current technologies, ongoing projects, challenges, and future prospects. Ensure that the report is well-structured and professional.",
  "subqueries_prompt": "Generate 2 interesting, diverse search queries that would be useful for generating a detailed report on the future of AI in smart cities. These subqueries should cover various aspects of the topic, including current technologies, ongoing projects, challenges, and future prospects.",
  "report_prompt": "Write a comprehensive and professional in English, five-paragraph, 200-word research report about the future of AI in smart cities based on the provided information. Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. Reset the citations index and ignore the order of citations in the provided information.",
  "start_published_date": "2024-01-01",
  "end_published_date": "2024-06-03",
  "highlights": {
    "num_sentences": 5
  },
  "text": {
    "include_html_tags": false
  },
  "num_subqueries": 5
}
```
