#!/usr/bin/env python3
"""Main entry point for the Fast Food Simulator."""

def lobby_filter(lobbies, criteria):
    """Filters lobbies based on minimum players."""
    return [lobby for lobby in lobbies if lobby['player_count'] > criteria['min_players']]

def main():
    """Entry point that displays welcome message."""
    print('Welcome to Fast Food Simulator!')

if __name__ == '__main__':
    main()
