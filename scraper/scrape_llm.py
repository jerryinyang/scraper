import json
import os

from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4o",
    },
}


smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the future games and their URLs.",
    source="https://www.betano.ng/",
    config=graph_config,
)

result = smart_scraper_graph.run()


output = json.dumps(result, indent=2)

line_list = output.split("\n")  # Sort of line replacing "\n" with a new line

for line in line_list:
    print(line)
