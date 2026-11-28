import httpx
from langchain.tools import tool


@tool
def get_product_metrics(product: str, quarter: str) -> str:
    """Look up usage metrics for one of our products.

    Use this when the user asks how a product is performing.
    """
    mock_data = {
        "ChatApp": {
            "2024-Q1": '{"product": "ChatApp", "quarter": "2024-Q1", "dau": 1250000, "mau": 5400000, "api_calls": 98000000, "revenue_usd": 450000}',
            "2024-Q2": '{"product": "ChatApp", "quarter": "2024-Q2", "dau": 1380000, "mau": 6100000, "api_calls": 112000000, "revenue_usd": 520000}',
            "2024-Q3": '{"product": "ChatApp", "quarter": "2024-Q3", "dau": 1500000, "mau": 6800000, "api_calls": 135000000, "revenue_usd": 610000}',
        },
        "DataSync": {
            "2024-Q1": '{"product": "DataSync", "quarter": "2024-Q1", "dau": 32000, "mau": 89000, "sync_jobs": 450000, "revenue_usd": 88000}',
            "2024-Q2": '{"product": "DataSync", "quarter": "2024-Q2", "dau": 38000, "mau": 102000, "sync_jobs": 520000, "revenue_usd": 105000}',
        },
        "AnalyticsPro": {
            "2024-Q1": '{"product": "AnalyticsPro", "quarter": "2024-Q1", "dau": 8500, "mau": 24000, "reports_generated": 120000, "revenue_usd": 35000}',
        }
    }
    
    return mock_data.get(product, {}).get(quarter, '{"error": "No data found", "product": "' + product + '", "quarter": "' + quarter + '"}')