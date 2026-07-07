#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kindle Oasis 3 Facebook Browser - Main Entry Point
Python-based web browser wrapper for Facebook access
"""

import sys
import os
import logging
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from python.browser import KindleBrowser
from python.config import BrowserConfig
from python.facebook_handler import FacebookHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/facebook_browser.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class FacebookBrowserApp:
    """Main application class for Facebook browser on Kindle"""
    
    def __init__(self):
        """Initialize the Facebook browser application"""
        logger.info("Initializing FacebookBrowserApp")
        
        # Load configuration
        self.config = BrowserConfig()
        
        # Initialize browser
        self.browser = KindleBrowser(self.config)
        
        # Initialize Facebook handler
        self.facebook = FacebookHandler(self.config)
        
        logger.info("FacebookBrowserApp initialized successfully")
    
    def run(self):
        """Run the main application"""
        logger.info("Starting Facebook Browser application")
        
        try:
            # Start the browser
            self.browser.start()
            
            # Navigate to Facebook
            facebook_url = self.facebook.get_optimized_url()
            logger.info(f"Navigating to: {facebook_url}")
            
            self.browser.navigate(facebook_url)
            
            # Run event loop
            self.browser.run()
            
        except Exception as e:
            logger.error(f"Error running application: {e}", exc_info=True)
            self.browser.show_error(str(e))
            return 1
        
        return 0
    
    def cleanup(self):
        """Clean up resources"""
        logger.info("Cleaning up resources")
        if self.browser:
            self.browser.shutdown()


def main():
    """Main entry point"""
    app = None
    exit_code = 1
    
    try:
        app = FacebookBrowserApp()
        exit_code = app.run()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        exit_code = 0
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        exit_code = 1
    finally:
        if app:
            app.cleanup()
    
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
