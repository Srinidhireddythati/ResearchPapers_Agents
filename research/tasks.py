from research.agents import OpenAIChatAgent, ArxivSearchAgent

class GenerateReportTask:
    def __init__(self, openai_agent):
        self.openai_agent = openai_agent

    def execute(self, prompt):
        # Use OpenAI agent to generate a report
        return self.openai_agent.generate_report(prompt)

class FetchFinancialDataTask:
    def __init__(self, arxiv_agent):
        self.arxiv_agent = arxiv_agent

    def execute(self, query):
        # Use arXiv agent to fetch research papers
        return self.arxiv_agent.search(query)
