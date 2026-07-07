#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kindle Browser - Core browser implementation for Kindle Oasis 3
"""

import logging
import requests
from typing import Optional
from urllib.parse import urljoin

logger = logging.getLogger(__name__)


class KindleBrowser:
    """Core browser implementation for Kindle devices"""
    
    def __init__(self, config):
        """Initialize Kindle browser
        
        Args:
            config: BrowserConfig object with settings
        """
        self.config = config
        self.session = requests.Session()
        self.current_url = None
        self.is_running = False
        self.page_content = None
        self.page_title = None
        
        # Set up session with proper headers
        self._setup_session()
        
        logger.info("KindleBrowser initialized")
    
    def _setup_session(self):
        """Configure requests session for Kindle/Facebook compatibility"""
        
        # User agents optimized for Kindle
        user_agents = [
            # Mobile user agents that Facebook recognizes
            'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SM-T530NU Build/KTU84M) AppleWebKit/534.30',
            'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950 XL)',
            'Mozilla/5.0 (Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        ]
        
        # Use first user agent or from config
        user_agent = self.config.get('user_agent') or user_agents[0]
        
        # Set headers
        self.session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'DNT': '1',
        })
        
        # Configure SSL verification based on config
        self.session.verify = self.config.get('verify_ssl', True)
        
        logger.info(f"Session configured with User-Agent: {user_agent}")
    
    def start(self):
        """Start the browser"""
        self.is_running = True
        logger.info("Browser started")
    
    def navigate(self, url: str) -> bool:
        """Navigate to a URL
        
        Args:
            url: URL to navigate to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Navigating to: {url}")
            
            # Make request
            response = self.session.get(url, timeout=self.config.get('request_timeout', 30))
            response.raise_for_status()
            
            # Store content
            self.current_url = response.url
            self.page_content = response.text
            
            # Extract title
            self._extract_title()
            
            logger.info(f"Successfully navigated to: {self.current_url}")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            return False
    
    def _extract_title(self):
        """Extract page title from content"""
        try:
            import re
            match = re.search(r'<title>(.+?)</title>', self.page_content, re.IGNORECASE)
            if match:
                self.page_title = match.group(1)
            else:
                self.page_title = self.current_url
        except Exception as e:
            logger.warning(f"Failed to extract title: {e}")
            self.page_title = self.current_url
    
    def render(self) -> str:
        """Render current page (simplified)
        
        Returns:
            Rendered HTML content
        """
        if not self.page_content:
            return "<html><body>No content loaded</body></html>"
        return self.page_content
    
    def run(self):
        """Run the browser event loop"""
        logger.info("Starting browser event loop")
        
        try:
            while self.is_running:
                # Handle input events
                self._handle_input()
                
        except KeyboardInterrupt:
            logger.info("Browser interrupted")
        except Exception as e:
            logger.error(f"Error in browser loop: {e}", exc_info=True)
    
    def _handle_input(self):
        """Handle input from Kindle hardware buttons and touch"""
        # Placeholder for input handling
        import time
        time.sleep(0.1)
    
    def show_error(self, message: str):
        """Display error message to user
        
        Args:
            message: Error message to display
        """
        logger.error(f"Showing error to user: {message}")
        print(f"ERROR: {message}")
    
    def shutdown(self):
        """Shut down the browser"""
        self.is_running = False
        self.session.close()
        logger.info("Browser shutdown")
