# Agentic Reports
```                                                                                                              
    _   ___ ___ _  _ _____ ___ ___   ___ ___ ___  ___  ___ _____ ___ 
   /_\ / __| __| \| |_   _|_ _/ __| | _ | __| _ \/ _ \| _ |_   _/ __|
  / _ | (_ | _|| .` | | |  | | (__  |   | _||  _| (_) |   / | | \__ \
 /_/ \_\___|___|_|\_| |_| |___\___| |_|_|___|_|  \___/|_|_\ |_| |___/
                                                                     
    A Comprehensive Python Library for Generating Research Reports

```
Welcome to Agentic Reports, a Python library designed to simplify the process of generating comprehensive research reports. This library leverages the power of FastAPI, Pydantic, Pandas, and Exa to provide users with an efficient and streamlined way to create detailed reports based on various data sources. Agentic Reports uses real data from the internet, considering parameters such as time, source, domain, and other relevant factors to ensure the information is current and accurate.

### Technical Overview

Agentic Reports uses a multi-step process to deliver detailed research reports from a variety of sources:

1. **User Query Submission**: Users start by submitting a topic they wish to research. This can be done through a simple API request.

2. **Subquery Generation**: The system automatically generates a set of subqueries related to the main topic. These subqueries break down the broad topic into specific areas of focus, ensuring a comprehensive analysis.

3. **Data Collection**: Using the generated subqueries, the system searches for relevant information across various sources, including databases, external APIs, and other repositories. Web data features include filtering by time, source, domain, and other parameters to ensure the information is current and relevant.

4. **Data Compilation**: The collected data is compiled into a cohesive and structured report. The system organizes the information, providing detailed analysis, insights, and findings based on the initial topic and subqueries.

5. **Report Delivery**: The final report, complete with citations and data sources, is delivered back to the user in a well-organized format. This ensures that users receive a thorough and reliable resource for their research needs.

By following these steps, Agentic Reports provides users with a streamlined and efficient way to generate comprehensive research reports, making it an invaluable tool for in-depth analysis and information gathering.

### Features

- **AI-Enhanced Report Generation**: Harnesses the power of advanced AI models to create detailed and precise reports, ensuring accuracy and depth in every analysis.
- **Robust Data Analysis**: Utilizes powerful search capabilities combined with Pandas for extensive data manipulation and insightful analysis.
- **Web Data Features**: Incorporates real-time data from the internet, allowing filtering by time, source, domain, and other parameters to ensure the most current and relevant information.
- **Flexible Report Customization**: Provides users with the ability to tailor reports to their specific needs, offering a high degree of customization to fit various requirements.

### How to Install

To install Agentic Reports, simply use pip:

```bash
pip install agentic-reports
```

This command will install the library and all its dependencies, making it ready for use in your projects.

### Setting Up API Keys for Agentic Reports

To use Agentic Reports, you need to set your OpenAI and Exa API keys. These keys can be set from the command line or will be prompted the first time you start the library.

#### Obtaining API Keys

- **OpenAI API Key**: To get your OpenAI API key, visit the [OpenAI API page](https://platform.openai.com/account/api-keys) and follow the instructions to create and retrieve your API key.
- **Exa API Key**: To get your Exa API key, visit the [Exa API page](https://docs.exa.ai/) and follow the instructions to sign up and obtain your API key.

#### Automatic Prompt on First Start

When you first start the Agentic Reports library, it will check for the necessary API keys. If they are not set, it will prompt you to enter them:

```bash
agentic-reports
```

You will see prompts like:

```plaintext
Enter your OPENAI_API_KEY:
Enter your EXA_API_KEY:
```

This ensures that you have the required keys set up before the application starts. Once entered, these keys will be used for subsequent runs of the application.

By following these steps, you can easily set up and use your API keys to get the most out of Agentic Reports. For more detailed information, refer to the official documentation provided with the library.

#### Alternative Command Line Setup

1. **Set API Keys Manually**: You can manually set your API keys using the `export` command in your terminal:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export EXA_API_KEY="your_exa_api_key"
   ```

2. **Check if API Keys are Set**: To verify that your API keys are set, you can use the `echo` command:

   ```bash
   echo $OPENAI_API_KEY
   echo $EXA_API_KEY
   ```

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

- **/generate-report-advanced**: Generates an advanced, comprehensive report based on detailed subqueries and provided prompts.
  - Parameters: 
    - `query` (string): The main topic for the report.
    - `primary_prompt` (string): The primary prompt for the report generation.
    - `subqueries_prompt` (string): The prompt for generating subqueries.
    - `report_prompt` (string): The detailed prompt for generating the final report.
    - `start_published_date` (string, optional): The start date for filtering published articles.
    - `end_published_date` (string, optional): The end date for filtering published articles.
    - `include_domains` (list of strings, optional): Domains to include in the search.
    - `exclude_domains` (list of strings, optional): Domains to exclude from the search.
    - `highlights` (dict, optional): Parameters for highlighting text.
    - `text` (dict, optional): Parameters for including HTML tags in the text.
    - `num_subqueries` (int): The number of subqueries to generate.
    - `batch_size` (int, optional): The size of each batch for processing subqueries.

### Sample Request JSON

```
{
  "query": "string",  // The main topic for the report
  "primary_prompt": "string",  // The primary prompt for the report generation
  "subqueries_prompt": "string",  // The prompt for generating subqueries
  "report_prompt": "string",  // The detailed prompt for generating the final report
  "start_published_date": "string (YYYY-MM-DD)",  // Optional: The start date for filtering published articles
  "end_published_date": "string (YYYY-MM-DD)",  // Optional: The end date for filtering published articles
  "include_domains": ["string"],  // Optional: Domains to include in the search
  "exclude_domains": ["string"],  // Optional: Domains to exclude from the search
  "highlights": {
    "num_sentences": "int"  // Optional: Parameters for highlighting text
  },
  "text": {
    "include_html_tags": "boolean"  // Optional: Parameters for including HTML tags in the text
  },
  "num_subqueries": "int",  // The number of subqueries to generate
  "batch_size": "int"  // Optional: The size of each batch for processing subqueries
}

```
- remove "// descriptions"

### Advanced Uses

Agentic Reports can be used in a variety of advanced scenarios, such as:

- **Automated Generation of Research Papers and Articles**: Automatically generate in-depth research papers and articles by leveraging AI models that create comprehensive and well-structured content based on user-defined topics.

- **Data Analysis and Visualization for Business Intelligence**: Utilize the library to perform sophisticated data analysis and create visualizations that aid in business decision-making and strategy formulation.

- **Custom Report Generation for Specific Industries or Topics**: Tailor reports to meet the unique needs of different industries or specific research topics, providing highly relevant and targeted information.

### Advanced Report Generation

The `@router.post("/generate-report-advanced")` endpoint is designed for generating comprehensive and detailed reports based on advanced queries and parameters. This endpoint allows for a high degree of customization, enabling users to specify detailed prompts, subqueries, and other parameters to tailor the report generation process to their specific needs.

#### Endpoint Purpose and Functionality

The endpoint aims to provide users with the ability to generate reports that require a deeper level of analysis and customization than standard reports. It supports a wide range of parameters that can be used to define the scope, focus, and structure of the generated report.

#### Parameters

- `query` (string): The main query or topic for the report.
- `primary_prompt` (string): The primary prompt guiding the report's focus.
- `subqueries_prompt` (string): Prompts for generating subqueries related to the main topic.
- `report_prompt` (string): The prompt for structuring the final report.
- `start_published_date` (string, optional): The start date for filtering published data.
- `end_published_date` (string, optional): The end date for filtering published data.
- `include_domains` (list of strings, optional): Domains to include in the search.
- `exclude_domains` (list of strings, optional): Domains to exclude from the search.
- `highlights` (dict, optional): Parameters for highlighting key sentences.
- `text` (dict, optional): Parameters for text content retrieval.
- `num_subqueries` (int): The number of subqueries to generate.

#### Example JSON Request

```json
{
  "query": "AI Stocks",
  "primary_prompt": "Generate a detailed report on the current advancements, performance, and market trends of AI stocks. The report should include an analysis of recent developments, major players, market performance, challenges faced by AI stocks, and future prospects. Ensure that the report is well-structured and professional.",
  "subqueries_prompt": "Generate 2 interesting, diverse search queries that would be useful for generating a detailed report on AI stocks. These subqueries should cover various aspects of the topic, including recent advancements, market performance, major players, challenges, and future prospects.",
  "report_prompt": "Write a comprehensive and professional in English, five-paragraph, 200-word research report about AI stocks based on the provided information. Include citations in the text using footnote notation ([citation #]), for example [2]. First provide the report, followed by a single `References` section that only lists the URLs (and their published date) used, in the format [#] <url>. For the published date, only include the month and year. Reset the citations index and ignore the order of citations in the provided information.",
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

#### Expected Response

The response will include a structured report based on the provided parameters. The report will be comprehensive, including analysis, insights, and findings as specified in the prompts and subqueries. The response structure will also include any highlights or specific text content retrieval parameters as requested.

By utilizing this advanced report generation feature, developers and researchers can create detailed and customized reports tailored to their specific research needs and interests.

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

Here's the updated README with the link pointing to `./sample-reports/`:

# Advanced Reporting Techniques in Agentic Reports

This README provides an overview of advanced reporting techniques utilized in Agentic Reports, showcasing examples and JSON configurations for each method. These techniques enhance the depth, accuracy, and comprehensiveness of generated reports, tailored to specific research needs.

## Recursive Prompting

Recursive prompting involves iterative querying to refine searches based on previous responses, ensuring accurate and relevant information.

[Learn more about Recursive Prompting](./sample-reports/recursive-prompting.md)

## Graph Structures

Graph-based prompting uses graph structures to map relationships between information, identifying intricate connections for a holistic report.

[Learn more about Graph Structures](./sample-reports/graph-structures.md)

## Advanced Logic and Reasoning

This technique employs critical thinking and evidence-based analysis to ensure logical, coherent content supported by data.

[Learn more about Advanced Logic and Reasoning](./sample-reports/advanced-logic-and-reasoning.md)

## Combining Approaches

Agentic Reports often combine these techniques to maximize report quality, tackling complex topics with precision.

[Learn more about Combining Approaches](./sample-reports/combining-approaches.md)

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

## Sample Outputs
```
Starting report generation for topic: Agentic Engineering and the coming agent landscape
🌿 Generating subqueries from topic: Agentic Engineering and the coming agent landscape

Raw response content: Certainly! Below are ten diverse and interesting search queries that can help you generate a comprehensive report on "Agentic 

Engineering and the coming agent landscape":

1. **"Agentic Engineering: Definitions and Key Concepts"**
   - Understand the foundational ideas and terminologies related to agentic engineering.

2. **"Historical Evolution and Milestones in Agentic Engineering"**
   - Explore the development and significant breakthroughs in the field.

3. **"Agentic Engineering in Artificial Intelligence and Robotics"**
   - Investigate the application of agentic engineering within AI and robotics.

4. **"Ethical Considerations and Challenges in Agentic Engineering"**
   - Delve into the ethical implications and potential societal impacts.

5. **"Future Landscape of Autonomous Agents in Industry and Everyday Life"**
   - Analyze future projections and the expected integration of autonomous agents in various sectors.

6. **"Case Studies of Successful Implementation of Agentic Engineering"**
   - Look at real-world examples and their outcomes to understand practical applications.

7. **"Agentic Engineering: Innovations and Upcoming Technologies"**
   - Identify the latest innovations and technologies that are shaping the field.

8. **"Comparative Analysis of Agentic Engineering vs Traditional Engineering"**
   - Compare and contrast agentic engineering with other engineering disciplines.

9. **"Regulatory Frameworks and Policies Around Agentic Engineering"**
   - Investigate the current and proposed regulations governing the development and deployment of autonomous agents.

10. **"Impact of Agentic Engineering on Employment and Workforce Dynamics"**
    - Examine how agentic engineering and autonomous agents are transforming job markets and skills requirements.

These queries should provide a well-rounded basis for your research and reporting on the subject.
Parsed subqueries: 

['**"Agentic Engineering: Definitions and Key Concepts"**', '**"Historical Evolution and Milestones in Agentic Engineering"**', '**"Agentic Engineering in Artificial Intelligence and Robotics"**', '**"Ethical Considerations and Challenges in Agentic Engineering"**', '**"Future Landscape of Autonomous Agents in Industry and Everyday Life"**', '**"Case Studies of Successful Implementation of Agentic Engineering"**', '**"Agentic Engineering: Innovations and Upcoming Technologies"**', '**"Comparative Analysis of Agentic Engineering vs Traditional Engineering"**', '**"Regulatory Frameworks and Policies Around Agentic Engineering"**', '**"Impact of Agentic Engineering on Employment and Workforce Dynamics"**']

⌛ Searching each subquery
🔍 Searching for subquery: **"Agentic Engineering: Definitions and Key Concepts"**
🔍 Searching for subquery: **"Historical Evolution and Milestones in Agentic Engineering"**
🔍 Searching for subquery: **"Agentic Engineering in Artificial Intelligence and Robotics"**
🔍 Searching for subquery: **"Ethical Considerations and Challenges in Agentic Engineering"**
🔍 Searching for subquery: **"Future Landscape of Autonomous Agents in Industry and Everyday Life"**
🔍 Searching for subquery: **"Case Studies of Successful Implementation of Agentic Engineering"**
🔍 Searching for subquery: **"Agentic Engineering: Innovations and Upcoming Technologies"**
🔍 Searching for subquery: **"Comparative Analysis of Agentic Engineering vs Traditional Engineering"**
🔍 Searching for subquery: **"Regulatory Frameworks and Policies Around Agentic Engineering"**
🔍 Searching for subquery: **"Impact of Agentic Engineering on Employment and Workforce Dynamics"**
✅ Search successful for subquery: **"Agentic Engineering: Definitions and Key Concepts"**
✅ Search successful for subquery: **"Historical Evolution and Milestones in Agentic Engineering"**
✅ Search successful for subquery: **"Agentic Engineering in Artificial Intelligence and Robotics"**
✅ Search successful for subquery: **"Ethical Considerations and Challenges in Agentic Engineering"**
✅ Search successful for subquery: **"Future Landscape of Autonomous Agents in Industry and Everyday Life"**
✅ Search successful for subquery: **"Case Studies of Successful Implementation of Agentic Engineering"**
✅ Search successful for subquery: **"Agentic Engineering: Innovations and Upcoming Technologies"**
✅ Search successful for subquery: **"Comparative Analysis of Agentic Engineering vs Traditional Engineering"**
✅ Search successful for subquery: **"Regulatory Frameworks and Policies Around Agentic Engineering"**
✅ Search successful for subquery: **"Impact of Agentic Engineering on Employment and Workforce Dynamics"**
🏁 Completed search for all subqueries
Generating report from Exa results for topic: Agentic Engineering and the coming agent landscape
⌨️  Formatting Exa results for LLM
```

## Sample Report
### Research Report: Agentic Engineering and the Coming Agent Landscape

Agentic Engineering is an evolving field that seeks to integrate principles of agency into engineered systems, emphasizing attributes such as autonomy, functionality, intentionality, and meaning. Foundational concepts in naturalized accounts of agency highlight the interrelation of these attributes and their evolution over time, showcasing the complex properties that constitute autonomous agents[1]. This approach recognizes the importance of scientific inquiry and continuous formulation of questions to advance the understanding and capabilities of agentic systems. Autonomy and interaction are particularly emphasized as key drivers in developing robust and adaptable agents capable of significantly enhancing human-machine collaboration[1].

Recent advancements in AI and machine learning have catalyzed the development of agentic systems capable of implementing complex workflows and multi-agent collaborations. A course by Andrew Ng and collaborators showcases AutoGen, a framework that enables the creation of specialized agents designed for tasks such as multi-agent collaboration, tool use, and planning[2]. By leveraging such tools, developers can build conversational agents with capabilities ranging from playing chess to generating detailed financial reports with minimal manual intervention. These innovations are not merely confined to digital realms; they are poised to revolutionize physical tasks through integrations with robotics, as seen with AI systems that can autonomously manage real-world tasks such as self-driving cars[3].

One of the most significant impacts of Agentic Engineering is on the workforce and employment dynamics. While there is concern about the potential for AI to displace human jobs, there is also a significant opportunity for enhancing productivity and innovation. AI employees, like the Ema multi-agent system, are designed to augment human roles by automating repetitive and complex tasks[4]. These AI personas integrate with various enterprise applications, enabling users to deploy AI-driven workflows with minimal setup. This shift not only promises to optimize operational efficiency but also necessitates new regulatory frameworks and training programs to ensure that human workers can effectively collaborate with AI counterparts while maintaining data security and ethical standards[4][5].

### References

[1] https://www.sciencedirect.com/science/article/pii/S0732118X09000464 (Published: November 2140)

[2] https://x.com/AndrewYNg/status/1795845101979406490 (Published: May 2024)

[3] https://gizmodo.com/ai-agents-openai-chatgpt-google-gemini-reality-sci-fi-1851500474 (Published: May 2024)

[4] https://medium.com/emaunlimited/the-guide-to-ai-employees-how-ema-is-revolutionizing-enterprise-automation-with-agentic-systems-16df43d8e8d8 (Published: May 2024)

[5] https://superagi.com/autonomous-software-development/ (Published: May 2024)