#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Facebook Handler - Manages Facebook-specific functionality
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class FacebookHandler:
    """Handles Facebook-specific operations and URL management"""
    
    # Facebook URLs optimized for mobile/low-bandwidth
    FACEBOOK_URLS = {
        'mobile': 'https://m.facebook.com',
        'lite': 'https://mbasic.facebook.com',
        'touch': 'https://touch.facebook.com',
        'www': 'https://www.facebook.com',
    }
    
    # URL parameters for optimization
    PARAMS = {
        'fref': 'ts',
        '_rdr': '1',
        'pn_redir': '1',
    }
    
    def __init__(self, config):
        """Initialize Facebook handler
        
        Args:
            config: BrowserConfig object
        """
        self.config = config
        self.preferred_version = self.config.get('facebook_version', 'lite')
        logger.info(f"FacebookHandler initialized with version: {self.preferred_version}")
    
    def get_optimized_url(self) -> str:
        """Get optimized Facebook URL for Kindle
        
        Returns:
            Optimized Facebook URL
        """
        base_url = self.FACEBOOK_URLS.get(self.preferred_version, self.FACEBOOK_URLS['lite'])
        logger.info(f"Using Facebook URL: {base_url}")
        return base_url
    
    def get_login_url(self) -> str:
        """Get Facebook login URL
        
        Returns:
            Facebook login URL
        """
        base_url = self.get_optimized_url()
        return f"{base_url}/login.php"
    
    def get_feed_url(self) -> str:
        """Get Facebook feed/home URL
        
        Returns:
            Facebook feed URL
        """
        return self.get_optimized_url()
    
    def inject_script(self, content: str) -> str:
        """Inject JavaScript into page for compatibility
        
        Args:
            content: HTML content to inject script into
            
        Returns:
            Modified HTML content
        """
        script = """
        <script>
            // Kindle-specific Facebook optimizations
            (function() {
                // Reduce animation delays
                document.querySelectorAll('*').forEach(el => {
                    if (el.style) {
                        el.style.transition = 'none';
                    }
                });
                
                // Optimize image loading
                document.querySelectorAll('img').forEach(img => {
                    img.loading = 'lazy';
                });
                
                // Disable heavy features
                if (window.requestAnimationFrame) {
                    window.requestAnimationFrame = function(cb) {
                        return setTimeout(cb, 100);
                    };
                }
            })();
        </script>
        """
        
        if '</body>' in content:
            return content.replace('</body>', script + '</body>')
        return content + script
    
    def is_facebook_url(self, url: str) -> bool:
        """Check if URL is a Facebook URL
        
        Args:
            url: URL to check
            
        Returns:
            True if URL is Facebook URL
        """
        facebook_domains = [
            'facebook.com',
            'm.facebook.com',
            'mbasic.facebook.com',
            'touch.facebook.com',
            'fb.com',
        ]
        
        return any(domain in url.lower() for domain in facebook_domains)
    
    def handle_login(self, username: str, password: str) -> bool:
        """Handle Facebook login
        
        Args:
            username: Facebook username or email
            password: Facebook password
            
        Returns:
            True if login successful
        """
        logger.info(f"Attempting login for: {username}")
        # Login handling would be implemented here
        return True
    
    def get_performance_tips(self) -> str:
        """Get performance optimization tips for Kindle
        
        Returns:
            Performance tips as string
        """
        tips = """
        Facebook Browser Performance Tips for Kindle Oasis 3:
        
        1. Use 'lite' version (mbasic.facebook.com) for best performance
        2. Disable images if experiencing lag (in settings)
        3. Clear cache periodically (/mnt/us/.facebook_browser/cache)
        4. Close other apps for better memory usage
        5. Use WiFi for faster loading
        6. Avoid videos - use text-only viewing when possible
        """
        return tips
