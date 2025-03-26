class WhatsAppBot:
    def __init__(self):
        self.investment_goals = {
            '1': 'High Returns',
            '2': 'Stable Growth',
            '3': 'Low Risk'
        }

    def start_chat(self, number):
        """Simulate WhatsApp chat initiation"""
        return f"Welcome to InvestAI! Choose your investment goal:\n" + \
               "\n".join([f"{k}️⃣ {v}" for k, v in self.investment_goals.items()])

    def analyze_selection(self, choice):
        """Fake portfolio generation"""
        portfolios = {
            '1': {'Stocks': 70, 'Crypto': 20, 'Bonds': 10},
            '2': {'Stocks': 50, 'ETF': 40, 'Bonds': 10},
            '3': {'Bonds': 60, 'Dividend Stocks': 30, 'Cash': 10}
        }
        return {
            'portfolio': portfolios.get(choice, {}),
            'analysis_link': 'https://investai.app/portfolio/123'
        }
