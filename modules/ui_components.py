from nicegui import ui

def create_scanner_grid():
    """
    Creates the AgGrid component for the scanner.
    """
    
    # Define Columns
    column_defs = [
        {'headerName': 'Ticker', 'field': 'ticker', 'sortable': True, 'filter': True, 'checkboxSelection': True},
        {'headerName': 'Price', 'field': 'current_price', 'sortable': True},
        {'headerName': 'Regime (Daily)', 'field': 'regime', 'sortable': True, 'cellClassRules': {
            'text-green-600 font-bold': 'x == "TRENDING"',
            'text-gray-400': 'x == "RANGING"'
        }},
        {'headerName': 'Status', 'field': 'status', 'sortable': True, 'cellClassRules': {
            'bg-yellow-200 text-black font-bold': 'x == "SQUEEZE"',
            'bg-green-200 text-green-900 font-bold': 'x == "BULLISH PULLBACK" || x == "RANGE BUY"',
            'bg-red-200 text-red-900 font-bold': 'x == "BEARISH PULLBACK" || x == "RANGE SELL"',
            'text-gray-400': 'x == "WAIT" || x == "RANGING" || x == "TRENDING"'
        }},
        {'headerName': 'RSI (H1)', 'field': 'hourly_rsi', 'sortable': True, 'cellClassRules': {
            'text-red-600 font-bold': 'x > 70',
            'text-green-600 font-bold': 'x < 30'
        }},
         {'headerName': 'Vol (H1)', 'field': 'volatility', 'sortable': True, 'cellClassRules': {
            'text-yellow-600 font-bold': 'x == "SQUEEZE"'
        }},
    ]

    # Create Grid
    grid = ui.aggrid({
        'columnDefs': column_defs,
        'defaultColDef': {
            'flex': 1,
            'resizable': True,
        },
        'rowSelection': 'single',
    }).classes('h-full w-full')

    return grid

