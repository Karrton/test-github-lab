#!/usr/bin/env python3
import os
import subprocess

def get_team_members():
    """Получить всех участников и их группы из git log"""
    result = subprocess.run(
        ['git', 'log', '--pretty=format:%an|%ae'],
        capture_output=True,
        text=True
    )
    
    members = {}
    for line in result.stdout.strip().split('\n'):
        if '|' in line:
            name, email = line.split('|')
            if name not in members:
                members[name] = email
    
    print("Участники команды:")
    print("-" * 50)
    for name, email in members.items():
        print(f"{name} <{email}>")
    print(f"\nВсего участников: {len(members)}")

if __name__ == "__main__":
    get_team_members()