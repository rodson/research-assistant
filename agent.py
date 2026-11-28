from managed_deepagents import define_deep_agent
from tools.metrics import get_product_metrics

agent = define_deep_agent(
    name="research-assistant",
    model="deepseek:deepseek-flash",
    tools=[get_product_metrics],
)
