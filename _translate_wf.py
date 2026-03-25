#!/usr/bin/env python3
"""Translate workflow files for build-applications-w-copilot-agent-mode.

Changes:
1. Workflow name fields -> Korean
2. skills/exercise-toolkit -> skills-kr/exercise-toolkit
3. exercise-toolkit ref -> kr-v0.6.0
4. Exercise title -> Korean
5. intro-message -> Korean
6. Add workshop tracker events to each workflow
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
WF_DIR = os.path.join(BASE, ".github", "workflows")

SESSION_ID = "256272c5"
TRACK = "build-applications-w-copilot-agent-mode"

TRACKER_START = """
      - name: Workshop Tracker에 시작 보고
        if: success()
        continue-on-error: true
        run: |
          SESSION_ID=$(jq -r '.sessionId' .github/workshop-config.json)
          TRACK=$(jq -r '.track' .github/workshop-config.json)
          API_URL=$(jq -r '.apiUrl' .github/workshop-config.json)
          curl -s -X POST "$API_URL" \\
            -H "Content-Type: application/json" \\
            -d '{
              "sessionId": "'"$SESSION_ID"'",
              "type": "start",
              "step": 0,
              "description": "실습 시작",
              "username": "'"$GITHUB_ACTOR"'",
              "repo": "'"$GITHUB_REPOSITORY"'",
              "track": "'"$TRACK"'",
              "runId": "'"$GITHUB_RUN_ID"'"
            }' || true
"""

def tracker_step(step_num, description, is_end=False):
    event_type = "end" if is_end else "step"
    return f"""
      - name: Workshop Tracker에 {'완료' if is_end else '단계'} 보고
        if: success()
        continue-on-error: true
        run: |
          SESSION_ID=$(jq -r '.sessionId' .github/workshop-config.json)
          TRACK=$(jq -r '.track' .github/workshop-config.json)
          API_URL=$(jq -r '.apiUrl' .github/workshop-config.json)
          curl -s -X POST "$API_URL" \\
            -H "Content-Type: application/json" \\
            -d '{{
              "sessionId": "'"\\"$SESSION_ID\\"'"",
              "type": "{event_type}",
              "step": {step_num},
              "description": "{description}",
              "username": "'"\\"$GITHUB_ACTOR\\"'"",
              "repo": "'"\\"$GITHUB_REPOSITORY\\"'"",
              "track": "'"\\"$TRACK\\"'"",
              "runId": "'"\\"$GITHUB_RUN_ID\\"'""
            }}' || true
"""


# Process workflow files
for filename in sorted(os.listdir(WF_DIR)):
    if not filename.endswith('.yml'):
        continue
    
    filepath = os.path.join(WF_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Change exercise-toolkit references
    content = content.replace(
        'skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.7.0',
        'skills-kr/exercise-toolkit/.github/workflows/start-exercise.yml@kr-v0.6.0'
    )
    content = content.replace(
        'skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.7.0',
        'skills-kr/exercise-toolkit/.github/workflows/find-exercise-issue.yml@kr-v0.6.0'
    )
    content = content.replace(
        'skills/exercise-toolkit/.github/workflows/finish-exercise.yml@v0.7.0',
        'skills-kr/exercise-toolkit/.github/workflows/finish-exercise.yml@kr-v0.6.0'
    )
    content = content.replace(
        'repository: skills/exercise-toolkit',
        'repository: skills-kr/exercise-toolkit'
    )
    content = content.replace(
        'ref: v0.7.0',
        'ref: kr-v0.6.0'
    )
    
    # 2. Translate exercise titles  
    content = content.replace(
        'exercise-title: "Build Applications with GitHub Copilot Agent Mode"',
        'exercise-title: "GitHub Copilot 에이전트 모드로 애플리케이션 빌드하기"'
    )
    
    # 3. Translate intro-message
    content = content.replace(
        '''intro-message: |
        "Welcome to the exciting world of GitHub Copilot agent mode! 🚀
        In this exercise, you'll unlock the potential of this AI-powered
        coding assistant to accelerate your development process. Let's dive in
        and have some fun exploring the future of coding together! 💻✨"''',
        '''intro-message: |
        "GitHub Copilot 에이전트 모드의 흥미진진한 세계에 오신 것을 환영합니다! 🚀
        이 실습에서는 AI 기반 코딩 어시스턴트의 잠재력을 발휘하여
        개발 프로세스를 가속화합니다. 함께 코딩의 미래를
        탐험하며 즐거운 시간을 보내봅시다! 💻✨"'''
    )
    
    # 4. Translate workflow names
    name_translations = {
        'name: Step 0 # Start Exercise build-applications-w-GHCP-agent-mode': 
            'name: Step 0 # 실습 시작 - Copilot 에이전트 모드로 앱 빌드',
        'name: Step 1 # Preparing to use GHCP agent mode':
            'name: Step 1 # Copilot 에이전트 모드 사용 준비',
        'name: Step 2 # octofit-tracker application initial setup':
            'name: Step 2 # octofit-tracker 앱 초기 설정',
        'name: Step 3 # Django project setup and database test data population':
            'name: Step 3 # Django 프로젝트 설정 및 데이터베이스 테스트 데이터 채우기',
        'name: Step 4 # Setup the Django REST API framework':
            'name: Step 4 # Django REST API 프레임워크 설정',
        'name: Step 5 # Setup the REACT framework frontend':
            'name: Step 5 # React 프레임워크 프론트엔드 설정',
        'name: Step 6 # Copilot on GitHub':
            'name: Step 6 # GitHub에서 Copilot 사용하기',
    }
    
    for eng, kor in name_translations.items():
        content = content.replace(eng, kor)
    
    # 5. Translate job names
    job_name_translations = {
        'name: Start Exercise': 'name: 실습 시작',
        'name: Post next step content': 'name: 다음 단계 안내',
        'name: Find Exercise Issue': 'name: 실습 이슈 찾기',
        'name: Check step work': 'name: 작업 확인',
        'name: Post review content': 'name: 리뷰 내용 게시',
        'name: Finish Exercise': 'name: 실습 완료',
    }
    
    for eng, kor in job_name_translations.items():
        content = content.replace(eng, kor)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

print("Done! All workflow files updated.")
