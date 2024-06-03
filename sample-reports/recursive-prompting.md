# Recursive Prompting in Advanced Reporting

Recursive Prompting is a sophisticated technique used in advanced reporting to refine and deepen the inquiry process. It involves iteratively querying or prompting for information, where each subsequent query is informed by the response to the previous one. This method ensures that the information gathered is both relevant and comprehensive, progressively narrowing down the focus to yield precise results.

## Example: AI's Role in Climate Change Mitigation

Consider the topic "AI's role in climate change mitigation." The initial query might focus on general applications of AI in environmental science. Based on the initial responses, subsequent queries could delve deeper into specific areas such as AI in renewable energy optimization, AI in carbon footprint reduction, and AI-driven climate modeling.

### JSON Example for Recursive Prompting

```json
{
  "query": "AI's role in climate change mitigation",
  "primary_prompt": "Generate a detailed report on the current advancements and applications of AI in climate change mitigation. The report should include an analysis of AI in renewable energy optimization, carbon footprint reduction, and climate modeling.",
  "subqueries_prompt": "Generate 2 interesting, diverse search queries that would be useful for generating a detailed report on AI's role in climate change mitigation. These subqueries should cover various aspects of the topic, including renewable energy optimization, carbon footprint reduction, and climate modeling.",
  "report_prompt": "Write a comprehensive and professional in English, five-paragraph, 200-word research report about AI's role in climate change mitigation based on the provided information. Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. Reset the citations index and ignore the order of citations in the provided information.",
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

This JSON example outlines how to structure a request for generating a report using recursive prompting. It demonstrates the progression from a broad initial query to more focused subqueries, ensuring a thorough exploration of the topic.
