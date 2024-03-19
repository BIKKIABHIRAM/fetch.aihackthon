from aea_ledger_fetchai import FetchAIApi
from aea.skills.base import Model

def fetchai_environment(model: Model):
    return {"fetchai": FetchAIApi(model.context)}

def start_agent(agent, environment):
    agent.setup()
    agent.set_agent_context(environment(agent))
    agent.connect()
    agent.start()
