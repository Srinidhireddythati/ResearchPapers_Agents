import openai
import arxiv

class OpenAIChatAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_report(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that helps with searching and analyzing research papers."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()

class ArxivSearchAgent:
    def search(self, query):
        search = arxiv.Search(
            query=query,
            max_results=5,
            sort_by=arxiv.SortCriterion.Relevance
        )
        results = []
        for result in search.results():
            results.append({
                "title": result.title,
                "summary": result.summary,
                "url": result.entry_id
            })
        return results
