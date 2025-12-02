from nicegui import ui
from modules.scanner import Scanner
from modules.ui_components import create_scanner_grid
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Initialize Logic
scanner = Scanner()

def refresh_grid(grid):
    """
    Refreshes the data in the AgGrid.
    """
    try:
        data = scanner.get_matrix()
        if data:
            grid.options['rowData'] = data
            grid.update()
            logging.info(f"Grid updated with {len(data)} rows.")
        else:
            logging.warning("No data found for grid.")
    except Exception as e:
        logging.error(f"Error refreshing grid: {e}")
        ui.notify("Failed to refresh data", type='negative')

@ui.page('/')
def main_page():
    # Header
    with ui.header().classes('bg-slate-900 text-white'):
        ui.label('Project Confluence').classes('text-xl font-bold')
        ui.label('Market Scanner').classes('text-sm opacity-75')

    # Main Layout
    with ui.row().classes('w-full h-[calc(100vh-64px)] no-wrap'):
        
        # Left Panel: Scanner Grid
        with ui.column().classes('w-full h-full p-2'):
            ui.label('Signal Matrix').classes('text-lg font-bold mb-2')
            
            # Create Grid
            grid = create_scanner_grid()
            
            # Initial Load
            refresh_grid(grid)
            
            # Auto Refresh (every 60s)
            ui.timer(60.0, lambda: refresh_grid(grid))
            
            # Manual Refresh Button
            ui.button('Refresh Now', on_click=lambda: refresh_grid(grid)).classes('mt-2')

ui.run(title='Confluence Scanner', dark=True)

