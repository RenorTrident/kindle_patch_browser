/*
 * Kindle Facebook Browser - C Implementation
 * Main entry point for the lightweight C-based browser
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "browser.h"

/* Global browser context */
browser_context_t *g_browser_ctx = NULL;

/* Signal handler for graceful shutdown */
void signal_handler(int sig) {
    fprintf(stderr, "\n[INFO] Signal %d received, shutting down gracefully...\n", sig);
    if (g_browser_ctx) {
        browser_shutdown(g_browser_ctx);
    }
    exit(0);
}

/* Print usage information */
void print_usage(const char *program_name) {
    printf("Usage: %s [OPTIONS]\n", program_name);
    printf("\nOptions:\n");
    printf("  -u URL           Start with specific URL\n");
    printf("  -c CONFIG_FILE   Use configuration file\n");
    printf("  -v               Verbose output\n");
    printf("  -h               Show this help message\n");
    printf("\nExample:\n");
    printf("  %s -u https://m.facebook.com\n", program_name);
}

/* Parse command line arguments */
int parse_arguments(int argc, char *argv[], char *url, char *config_file) {
    int opt;
    int verbose = 0;
    
    while ((opt = getopt(argc, argv, "u:c:vh")) != -1) {
        switch (opt) {
            case 'u':
                strncpy(url, optarg, 511);
                break;
            case 'c':
                strncpy(config_file, optarg, 255);
                break;
            case 'v':
                verbose = 1;
                break;
            case 'h':
                print_usage(argv[0]);
                exit(0);
            default:
                fprintf(stderr, "Unknown option: -%c\n", opt);
                return -1;
        }
    }
    
    return verbose;
}

/* Main function */
int main(int argc, char *argv[]) {
    char start_url[512] = "https://mbasic.facebook.com";
    char config_file[256] = "/mnt/us/.facebook_browser/config.json";
    int verbose = 0;
    
    printf("=================================================\n");
    printf("  Kindle Oasis 3 Facebook Browser (C)\n");
    printf("  Version 1.0.0\n");
    printf("=================================================\n\n");
    
    /* Parse command line arguments */
    verbose = parse_arguments(argc, argv, start_url, config_file);
    
    if (verbose) {
        fprintf(stderr, "[DEBUG] Start URL: %s\n", start_url);
        fprintf(stderr, "[DEBUG] Config file: %s\n", config_file);
    }
    
    /* Register signal handlers */
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);
    
    /* Initialize browser */
    printf("[INFO] Initializing browser...\n");
    g_browser_ctx = browser_init(config_file);
    if (!g_browser_ctx) {
        fprintf(stderr, "[ERROR] Failed to initialize browser\n");
        return 1;
    }
    
    /* Navigate to start URL */
    printf("[INFO] Navigating to: %s\n", start_url);
    if (browser_navigate(g_browser_ctx, start_url) != 0) {
        fprintf(stderr, "[ERROR] Failed to navigate to URL\n");
        browser_shutdown(g_browser_ctx);
        return 1;
    }
    
    /* Run browser event loop */
    printf("[INFO] Starting browser event loop...\n");
    if (browser_run(g_browser_ctx) != 0) {
        fprintf(stderr, "[ERROR] Browser event loop failed\n");
        browser_shutdown(g_browser_ctx);
        return 1;
    }
    
    /* Shutdown */
    printf("[INFO] Shutting down browser...\n");
    browser_shutdown(g_browser_ctx);
    
    printf("[INFO] Browser closed successfully\n");
    return 0;
}
