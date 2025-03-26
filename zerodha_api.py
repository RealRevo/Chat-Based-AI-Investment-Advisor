class ZerodhaBridge:
    @staticmethod
    def execute_trade(symbol, amount):
        """Simulate trade execution"""
        return {
            'status': 'success',
            'order_id': f"ZERODHA_{int(time.time())}",
            'symbol': symbol,
            'amount': amount
        }
