# Agentic Reports
## A Comprehensive Python Library for Generating Research Reports

Welcome to Agentic Reports, a Python library designed to simplify the process of generating comprehensive research reports. This library leverages the power of FastAPI, Pydantic, Pandas, and Exa to provide users with an efficient and streamlined way to create detailed reports based on various data sources.

### Technical Overview

Agentic Reports uses a multi-step process to deliver detailed research reports from a variety of sources:

1. **User Query Submission**: Users start by submitting a topic they wish to research. This can be done through a simple API request.

2. **Subquery Generation**: The system automatically generates a set of subqueries related to the main topic. These subqueries break down the broad topic into specific areas of focus, ensuring a comprehensive analysis.

3. **Data Collection**: Using the generated subqueries, the system searches for relevant information across various sources, including databases, external APIs, and other repositories. This step ensures the gathering of extensive and pertinent data.

4. **Data Compilation**: The collected data is compiled into a cohesive and structured report. The system organizes the information, providing detailed analysis, insights, and findings based on the initial topic and subqueries.

5. **Report Delivery**: The final report, complete with citations and data sources, is delivered back to the user in a well-organized format. This ensures that users receive a thorough and reliable resource for their research needs.

By following these steps, Agentic Reports provides users with a streamlined and efficient way to generate comprehensive research reports, making it an invaluable tool for in-depth analysis and information gathering.

### Features

- **AI-Enhanced Report Generation**: Harnesses the power of advanced AI models to create detailed and precise reports, ensuring accuracy and depth in every analysis.
- **Robust Data Analysis**: Utilizes Exa's powerful search capabilities combined with Pandas for extensive data manipulation and insightful analysis.
- **Flexible Report Customization**: Provides users with the ability to tailor reports to their specific needs, offering a high degree of customization to fit various requirements.

For more information on how to use Agentic Reports and its capabilities, please refer to the official documentation.


### How to Install

To install Agentic Reports, simply use pip:

```bash
pip install agentic-reports
```

This command will install the library and all its dependencies, making it ready for use in your projects.

### How `Agentic Reports` Works

`Agentic Reports` is designed to make the process of generating detailed research reports seamless and user-friendly.

#### Step 1: Submitting a Topic

1. **Submit a Topic**: The user starts by submitting a topic they want to research. This can be done through a simple API request, where the user provides the main topic of interest. For example, "Latest AI advancements".

#### Step 2: Generating Subqueries

2. **Automatic Subquery Generation**: Once the main topic is submitted, the system automatically generates a set of detailed subqueries related to the main topic. These subqueries help in breaking down the broad topic into specific areas of focus, ensuring a comprehensive analysis.

#### Step 3: Data Collection

3. **Data Gathering**: The system then uses these subqueries to search for relevant information across various sources. This includes fetching data from databases, external APIs, and other repositories. The goal is to gather as much pertinent information as possible.

#### Step 4: Compiling the Report

4. **Report Compilation**: After collecting the data, the system compiles all the gathered information into a cohesive and structured report. This report includes detailed analysis, insights, and findings based on the provided topic and its subqueries.

#### Step 5: Delivering the Report

5. **Report Delivery**: The final report is delivered back to the user in a well-organized format. The user can then review the comprehensive report, which includes citations, data sources, and detailed explanations, providing a thorough understanding of the topic.

### User Experience Highlights

- **Ease of Use**: Users only need to provide a single topic to get started. The rest of the process, including generating subqueries and gathering data, is handled automatically.
- **Comprehensive Analysis**: By breaking down the main topic into subqueries, the system ensures a deep and thorough exploration of the subject matter.
- **Time Efficiency**: Automating the research process saves users significant time and effort, providing them with detailed reports quickly.
- **Detailed Insights**: The final report includes citations and sources, offering users a reliable and informative resource for their research needs.

Agentic Reports, through `Agentic Reports`, streamlines the entire process of creating detailed research reports, making it an invaluable tool for anyone needing comprehensive and accurate information on a specific topic.

### API Reference

Agentic Reports provides several endpoints for generating reports and processing data:

- **/generate-report**: Generates a comprehensive report based on a given topic.
  - Parameters: `topic` (string)
  - Example Request: `{"topic": "Latest AI advancements"}`
  
- **/generate-subqueries**: Generates subqueries from a given topic for detailed analysis.
  - Parameters: `topic` (string), `num_subqueries` (int)
  - Example Request: `{"topic": "Latest AI advancements", "num_subqueries": 5}`
  
- **/search-subqueries**: Searches for information based on provided subqueries.
  - Parameters: `subqueries` (list of strings)
  - Example Request: `{"subqueries": ["AI in healthcare", "AI in finance"]}`
  
- **/advanced-search**: Performs an advanced search with customizable parameters.
  - Parameters: `query` (string), `start_published_date` (string), `end_published_date` (string), etc.
  - Example Request: `{"query": "AI", "start_published_date": "2021-01-01", "end_published_date": "2021-12-31"}`
  
- **/find-similar-links**: Finds similar links to a provided URL.
  - Parameters: `url` (string), `num_results` (int)
  - Example Request: `{"url": "https://cnn.com", "num_results": 10}`

### Advanced Uses

Agentic Reports can be used in a variety of advanced scenarios, such as:

- **Automated Generation of Research Papers and Articles**: Automatically generate in-depth research papers and articles by leveraging AI models that create comprehensive and well-structured content based on user-defined topics.

- **Data Analysis and Visualization for Business Intelligence**: Utilize the library to perform sophisticated data analysis and create visualizations that aid in business decision-making and strategy formulation.

- **Custom Report Generation for Specific Industries or Topics**: Tailor reports to meet the unique needs of different industries or specific research topics, providing highly relevant and targeted information.

### Advanced Overview: Prompt Engineering Approaches

Agentic Reports incorporates advanced prompt engineering techniques to enhance the quality and depth of generated reports. These approaches include multi-hop prompting, recursive strategies, graph structures, and advanced logic and reasoning.

#### Multi-Hop Prompting

Multi-hop prompting involves breaking down complex queries into a series of intermediate steps or subqueries. Each subquery aims to gather specific pieces of information that, when combined, provide a comprehensive answer to the original query. This approach ensures that the final report is detailed and well-supported by relevant data.

**Example**: To generate a report on "The impact of AI in healthcare," the system might break it down into subqueries such as:
1. Historical development of AI in healthcare.
2. Current applications of AI in diagnostics and treatment.
3. Case studies on AI-driven healthcare improvements.
4. Future trends and potential of AI in healthcare.

#### Recursive Prompting

Recursive prompting involves iterative querying, where the system refines its queries based on previous responses. This technique ensures that the gathered information is accurate and relevant, progressively narrowing down the search to provide precise and comprehensive results.

**Example**: For a topic like "AI's role in climate change mitigation," the initial query might focus on general applications of AI. Based on the gathered data, subsequent queries will delve deeper into specific areas such as AI in renewable energy optimization, AI in carbon footprint reduction, and AI-driven climate modeling.

#### Graph Structures

Graph-based prompting leverages graph structures to map relationships between different pieces of information. By creating a network of interconnected data points, the system can identify and explore intricate connections, providing a more holistic and nuanced report.

**Example**: When researching "AI in financial markets," a graph structure can help map out the relationships between AI technologies, market trends, regulatory impacts, and economic outcomes. This interconnected approach allows for a comprehensive analysis of how AI influences various aspects of financial markets.

#### Advanced Logic and Reasoning

Advanced logic and reasoning techniques are used to enhance the depth and accuracy of the reports. These techniques involve critical thinking, hypothesis testing, and evidence-based analysis to ensure that the generated content is logical, coherent, and well-supported by data.

**Example**: For a report on "Ethical implications of AI," the system uses advanced reasoning to weigh different ethical considerations, analyze case studies, and provide balanced arguments. It critically examines various perspectives, ensuring a thorough and unbiased analysis.

### Combining Approaches

Agentic Reports often combines these prompt engineering techniques to maximize the quality and comprehensiveness of the generated reports. By integrating multi-hop prompting, recursive strategies, graph structures, and advanced logic and reasoning, the system can tackle complex topics with precision and depth.

**Example**: Generating a report on "The future of AI in smart cities" might involve:
- **Multi-hop prompting** to break down the topic into subqueries like AI in traffic management, AI in energy efficiency, and AI in public safety.
- **Recursive prompting** to iteratively refine these subqueries based on initial findings.
- **Graph structures** to map out the relationships between different AI applications and their impacts on smart city development.
- **Advanced logic and reasoning** to critically analyze the data and provide well-rounded insights and projections.

By leveraging these advanced prompt engineering techniques, Agentic Reports ensures that users receive highly detailed, accurate, and insightful reports tailored to their specific research needs.