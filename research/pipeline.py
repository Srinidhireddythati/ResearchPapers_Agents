from research.agents import OpenAIChatAgent, ArxivSearchAgent

class Pipeline:
    def __init__(self, api_key):
        self.openai_chat_agent = OpenAIChatAgent(api_key)
        self.arxiv_search_agent = ArxivSearchAgent()

    def execute(self, query):
        # Search arXiv
        papers = self.arxiv_search_agent.search(query)

        # Generate additional insights
        insights = None
        if papers:
            prompt = "Analyze the following research papers:\n" + "\n".join([f"{paper['title']}: {paper['summary']}" for paper in papers])
            insights = self.openai_chat_agent.generate_report(prompt)

        return {'papers': papers, 'insights': insights}
