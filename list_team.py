#!/usr/bin/env python3
import os
import requests
import sys

def get_team_members():
    """Получить всех участников репозитория через GitHub API"""
    
    # Получаем информацию о репозитории из environment variables GitHub Actions
    github_repo = os.environ.get('GITHUB_REPOSITORY')  # формат: owner/repo
    github_token = os.environ.get('GITHUB_TOKEN')
    
    if not github_repo:
        print("Ошибка: GITHUB_REPOSITORY не найден")
        sys.exit(1)
    
    # GitHub API endpoint для получения contributors
    api_url = f"https://api.github.com/repos/{github_repo}/contributors"
    
    headers = {}
    if github_token:
        headers['Authorization'] = f'token {github_token}'
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        contributors = response.json()
        
        print("Участники команды:")
        print("-" * 50)
        
        for contributor in contributors:
            login = contributor.get('login', 'Unknown')
            contributions = contributor.get('contributions', 0)
            profile_url = contributor.get('html_url', '')
            
            print(f"{login}")
            print(f"  Вклад: {contributions} коммитов")
            print(f"  Профиль: {profile_url}")
            print()
        
        print(f"Всего участников: {len(contributors)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обращении к GitHub API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_team_members()
