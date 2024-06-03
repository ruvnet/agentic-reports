# Advanced Reporting Techniques in Agentic Reports

This README provides an overview of advanced reporting techniques utilized in Agentic Reports, showcasing examples and JSON configurations for each method. These techniques enhance the depth, accuracy, and comprehensiveness of generated reports, tailored to specific research needs.

## Recursive Prompting

Recursive prompting involves iterative querying to refine searches based on previous responses, ensuring accurate and relevant information.

[Learn more about Recursive Prompting](recursive-prompting.md)

## Graph Structures

Graph-based prompting uses graph structures to map relationships between information, identifying intricate connections for a holistic report.

[Learn more about Graph Structures](graph-structures.md)

## Advanced Logic and Reasoning

This technique employs critical thinking and evidence-based analysis to ensure logical, coherent content supported by data.

[Learn more about Advanced Logic and Reasoning](advanced-logic-and-reasoning.md)

## Combining Approaches

Agentic Reports often combines these techniques to maximize report quality, tackling complex topics with precision.

[Learn more about Combining Approaches](combining-approaches.md)

## JSON Example for Advanced Report Generation

```json
{
  "query": "The future of AI in smart cities",
  "primary_prompt": "Generate a detailed report on the future of AI in smart cities, focusing on applications such as traffic management, energy efficiency, and public safety.",
  "subqueries_prompt": "Generate 2 interesting, diverse search queries that would be useful for generating a detailed report on the future of AI in smart cities.",
  "report_prompt": "Write a comprehensive and professional in English, five-paragraph, 200-word research report about the future of AI in smart cities based on the provided information.",
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

For more detailed examples and JSON configurations, refer to the respective `.md` files linked above.
