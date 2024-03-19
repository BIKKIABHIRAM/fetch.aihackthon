from agents.summarization_agent import SummarizationAgent
from utils.fetchai_utils import start_agent, fetchai_environment

def main():
    # Create a Summarization Agent
    summarization_agent = SummarizationAgent()

    # Start the agent on Fetch.ai environment
    start_agent(summarization_agent, fetchai_environment)

if __name__ == "__main__":
    main()
