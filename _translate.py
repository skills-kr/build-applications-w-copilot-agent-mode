#!/usr/bin/env python3
"""Translate step files for build-applications-w-copilot-agent-mode."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

files = {}

# Step 1
files[".github/steps/1-preparing.md"] = r"""## Step 1: GitHub Copilot 에이전트 모드 시작하기

**"GitHub Copilot 에이전트 모드로 애플리케이션 빌드하기"** 실습에 오신 것을 환영합니다! :robot:

이 실습에서는 GitHub Copilot 에이전트 모드를 사용하여 피트니스 목표와 진행 상황을 추적하는 애플리케이션을 빌드합니다. 🏋️‍♂️🏃‍♀️💪

### GitHub Copilot 에이전트 모드란?

Copilot 에이전트 모드는 처음부터 앱을 만들고, 여러 파일에 걸쳐 리팩터링하고, 테스트를 작성 및 실행하며, 레거시 코드를 최신 프레임워크로 마이그레이션할 수 있습니다. 자동으로 문서를 생성하고, 새로운 라이브러리를 통합하거나, 복잡한 코드베이스에 대한 질문에 답변하는 것도 가능합니다. Copilot 에이전트 모드는 워크스페이스를 이해하는 AI 협력자를 통해 내부 개발 흐름을 조율하면서 여러분이 제어권을 유지할 수 있게 도와줍니다.

Copilot 에이전트 모드는 원하는 결과를 달성하기 위해 더 자율적이고 동적인 방식으로 작동합니다. 요청을 처리하기 위해 Copilot은 다음 단계를 반복하며 필요에 따라 여러 번 반복합니다:

관련 컨텍스트와 편집할 파일을 자율적으로 결정합니다.
작업을 완료하기 위한 코드 변경과 터미널 명령을 모두 제안합니다. 예를 들어, Copilot은 코드를 컴파일하고, 패키지를 설치하고, 테스트를 실행하는 등의 작업을 수행할 수 있습니다.
코드 편집과 터미널 명령 출력의 정확성을 모니터링하고 문제를 해결하기 위해 반복합니다.

> [!NOTE]
> GitHub Copilot 에이전트 모드에 대해 더 알아보려면 [에이전트 모드 사용하기 문서](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)를 참고하세요.

### :keyboard: 활동: GitHub Copilot 에이전트 모드 개발 환경 익히기

1. 아래 버튼을 우클릭하여 새 탭에서 **Create Codespace** 페이지를 엽니다.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

   - 모든 GitHub 계정에 포함된 무료 Codespaces 티어로 충분합니다(사용 가능한 시간이 남아있다면).
   - 기본 Codespace 설정을 그대로 사용하세요.

1. **Repository** 필드가 원본이 아닌 여러분의 복사본인지 확인한 후 녹색 **Create Codespace** 버튼을 클릭합니다.

   - ✅ 내 복사본: `/{{full_repo_name}}`
   - ❌ 원본: `/skills/build-applications-w-copilot-agent-mode`

1. Visual Studio Code가 로드될 때까지 잠시 기다립니다.

1. 계속하기 전에 프로젝트 폴더를 잠시 살펴보겠습니다.

   - 왼쪽 탐색 바에서 파일 탐색기, 디버거, 검색에 접근할 수 있습니다.
   - 하단 패널(Ctrl+J)에서 디버거 출력을 확인하고, 터미널 명령을 실행하며, 웹 서비스 포트를 구성할 수 있습니다.
   - docs 폴더에는 Copilot 에이전트 모드가 여러분의 앱을 빌드하는 데 참고할 다른 샘플 앱 저장소가 포함되어 있습니다. 이에 대해서는 다음 단계에서 더 자세히 다룹니다!

1. VS Code 상단에서 Copilot 아이콘을 찾아 클릭하여 Copilot Chat 패널을 엽니다.

   <img width="150" alt="image" src="https://github.com/user-attachments/assets/5e64db46-95cb-415d-badc-b6b8677f10c1" />

1. GitHub Copilot을 처음 사용하는 경우 사용 조건에 동의해야 합니다.
    - **Accept** 버튼을 클릭하여 계속합니다.

### :keyboard: 활동: Copilot 에이전트 모드를 사용하여 브랜치를 생성하고 게시하기 🙋

잘 하셨습니다! Copilot에게 브랜치 생성을 도와달라고 요청하여 커스터마이징 작업을 시작해 봅시다.

> [!NOTE]
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 **Continue** 버튼을 누르세요.

1. 아직 VS Code로 돌아가지 않았다면 돌아갑니다.
1. GitHub Copilot Chat 창이 아직 열려있지 않다면 엽니다.
1. GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 **Ask** 또는 **Edit** 대신 **Agent**를 선택합니다.

   <img src="https://github.com/user-attachments/assets/b9e291be-d835-4de0-ac1c-35a6ec3ea72d" width=30% height=30%>

1. Copilot 에이전트 모드에게 `build-octofit-app` 브랜치를 생성하고 게시하는 명령을 기억하도록 도움을 요청합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
   >
   > ```prompt
   > Please create and publish a new Git branch called build-octofit-app
   > ```

   Copilot 에이전트 모드가 응답하고 명령을 실행하기 위해 **continue**를 누르라고 안내합니다.<br/>

   <img src=https://github.com/user-attachments/assets/d1652fc1-78e5-49c6-9303-b455815eea8f width=40% height=40%>

1. 명령이 마음에 들면 `Continue` 버튼을 눌러 Copilot 에이전트 모드가 실행하도록 합니다. 복사해서 붙여넣을 필요가 없습니다!

1. 잠시 후 VS Code 하단 상태 바 왼쪽을 확인하여 활성 브랜치를 봅니다. `build-octofit-app`으로 표시되면 이 단계가 완료된 것입니다!

1. 브랜치가 GitHub에 푸시되었으므로 Mona가 이미 작업을 확인하고 있을 것입니다. 잠시 기다리며 댓글을 확인하세요. 진행 상황과 다음 레슨이 표시됩니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- 정확히 `build-octofit-app`이라는 이름으로 브랜치를 만들었는지 확인하세요. 접두사나 접미사 없이요.
- 브랜치가 실제로 저장소에 게시되었는지 확인하세요.

</details>
"""

# Step 2
files[".github/steps/2-application-initial-setup.md"] = r"""## Step 2: 초기 애플리케이션 설정: 디렉토리 구조, Python 요구사항, MongoDB

> [!NOTE]
> **비하인드 스토리:** 이 실습은 GitHub Copilot의 응답을 안내하는 커스텀 인스트럭션 파일을 사용합니다. 인스트럭션 파일 `.github/instructions/octofit_tracker_setup_project.instructions.md`에는 프로젝트 구조 가이드라인, Python 패키지 요구사항, MongoDB 구성이 포함되어 있으며 Copilot이 이 단계의 코드를 생성할 때 참조합니다.

이 단계에서 다음을 수행합니다:

- octofit-tracker 애플리케이션 디렉토리 구조를 생성합니다.
- octofit-tracker/backend 및 octofit-tracker/frontend 디렉토리를 생성합니다.
- octofit-tracker/backend/requirements.txt 파일을 생성합니다.

> [!NOTE]
> GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 "Ask" 또는 "Edit" 대신 "Agent"를 선택합니다.
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 `Continue` 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.
> - 에이전트 모드는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제하고, 실수가 발생하면 자동으로 복구하는 능력을 가지고 있습니다.

**Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.**

### :keyboard: 활동: GitHub Copilot 에이전트 모드에 프롬프트하여 애플리케이션 생성 시작하기

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's take the following step by step execute the commands.
> 
> Follow the instructions
>
> - Follow the OctoFit Tracker App structure
> - Follow the Python virtual environment creation
> - Create the requirements.txt file
> - Install the Python requirements from the file created
>```

1. 앱 디렉토리 구조를 만들고, Python 가상 환경을 설정하고, Copilot 에이전트 모드가 모든 프로젝트 의존성을 설치하는 `requirements.txt`를 작성했으니, 변경사항을 `build-octofit-app` 브랜치에 체크인합니다.

1. 새로운 변경사항이 완료되면 `build-octofit-app` 브랜치로 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- `build-octofit-app` 브랜치에 다음 파일의 커밋 변경사항이 있고 GitHub에 푸시/동기화되었는지 확인하세요:
  - `octofit-tracker/backend/requirements.txt`에 `Django==4.1` 패키지가 포함되어 있어야 합니다.
- Mona가 실수를 발견하면 수정하고 다시 푸시하세요. Mona는 필요한 만큼 여러 번 작업을 확인합니다.

</details>
"""

# Step 3
files[".github/steps/3-django-project-setup.md"] = r"""## Step 3: octofit_db MongoDB 데이터베이스 초기화 및 생성, Django 프로젝트/앱 구성, Django 프로젝트/앱 파일 업데이트, MongoDB 데이터베이스 채우기

> [!NOTE]
> **비하인드 스토리:** 이 실습은 GitHub Copilot의 응답을 안내하는 커스텀 인스트럭션 파일을 사용합니다. 인스트럭션 파일 `.github/instructions/octofit_tracker_setup_project.instructions.md`와 `.github/instructions/octofit_tracker_django_backend.instructions.md`에는 Django 백엔드 가이드라인, MongoDB 구성, 프로젝트 구조가 포함되어 있으며 Copilot이 이 단계의 코드를 생성할 때 참조합니다.

이 단계에서 다음을 수행합니다:

- octofit_db MongoDB 데이터베이스 구조를 설정합니다.
- octofit-tracker/backend/octofit_tracker 앱 파일을 업데이트합니다:
  - settings, models, serializers, urls, views, tests, admin 파일.
- octofit_db 데이터베이스에 테스트 데이터를 채웁니다.
- 테스트 데이터가 octofit_db 데이터베이스에 채워졌는지 확인합니다.

GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> [!NOTE]
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 `Continue` 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.
> - 에이전트 모드는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제하고, 실수가 발생하면 자동으로 복구하는 능력을 가지고 있습니다.

**Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.**

### :keyboard: 활동: Python Django 프로젝트/앱 설정하기

이 활동에서는 VS Code의 프롬프트 파일 기능을 활용합니다. IT 부서에서 Django 프로젝트 애플리케이션을 생성하기 위한 프롬프트 파일이 이미 만들어져 있습니다. GitHub Copilot Chat에 다음 프롬프트를 복사/붙여넣기하고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

프롬프트 파일이란?

프롬프트 파일을 사용하면 일반적이고 반복적인 개발 작업을 위한 재사용 가능한 프롬프트를 마크다운 파일로 정의할 수 있습니다.
프롬프트 파일은 채팅에서 직접 실행할 수 있는 독립형 프롬프트입니다. 작업별 컨텍스트와 작업 수행 방법에 대한 가이드라인을 포함할 수 있습니다.
프롬프트 파일을 커스텀 인스트럭션과 결합하여 복잡한 작업을 일관되게 실행할 수 있습니다.

자세한 내용은 [VS Code 문서: 프롬프트 파일](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files) 페이지를 참고하세요.

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /create-django-project
>```

> [!NOTE]
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 각 명령을 실행하려면 `Continue` 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.

> [!IMPORTANT]
> - GitHub Copilot 에이전트 모드가 제안하는 방식으로 Python Django 앱을 시작하지 **마세요**. 아래 이미지가 보이면 **cancel**을 누르세요.

<img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>

### :keyboard: 활동: octofit_db MongoDB 데이터베이스 초기화, 생성, 채우기

IT 부서에서 octofit_db MongoDB 데이터베이스를 초기화하고 생성하기 위해 만든 프롬프트 파일을 계속 활용합니다. GitHub Copilot Chat에 다음 프롬프트를 복사/붙여넣기하고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
>
> /init-populate-octofit_db
> ```

### :keyboard: 활동: Python Django 프로젝트/앱 파일을 업데이트할 프롬프트 파일 만들기

이제 다른 직원들과 공유하여 octofit-tracker 앱을 개발할 수 있는 프롬프트 파일을 직접 만들어 봅시다. GitHub Copilot Chat에 다음 프롬프트를 복사/붙여넣기하고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's add the following to a prompt file called `update-octofit-tracker-app.prompt.md` in the `.github/prompts` directory and add mode: 'agent' and model: GPT-4.1 to the prompt file.
>
> # Django App Updates
>
> - All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.
>
> 1. Update `settings.py` for MongoDB connection and CORS.
> 2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
> 3. Ensure `/` points to the api and `api_root` is present in `urls.py`.
> ```

> [!TIP]
> 프롬프트 파일을 사용하여 반복 가능한 작업과 워크플로우를 정의하세요.
>
> 프롬프트를 작성할 때는 **무엇을** 해야 하는지에 집중하세요. **어떻게** 하는지는 인스트럭션을 참조할 수 있습니다.

자세한 내용은 [VS Code 문서: 프롬프트 파일](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files) 페이지를 참고하세요.

### :keyboard: 활동: 프롬프트 파일을 사용하여 Python Django 프로젝트/앱 파일 업데이트하기

GitHub Copilot Chat에 다음 프롬프트를 복사/붙여넣기하고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /update-octofit-tracker-app
> ```
>

> [!IMPORTANT]
> - GitHub Copilot 에이전트 모드가 제안하는 방식으로 Python Django 앱을 시작하지 **마세요**. 아래 이미지가 보이면 **cancel**을 누르세요.

<img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>

1. 데이터베이스 구조를 만들고, Django 프로젝트 파일을 업데이트하고, 데이터베이스를 채웠으니, 변경사항을 `build-octofit-app` 브랜치에 체크인합니다.

1. 새로운 변경사항이 완료되면 GitHub에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- `build-octofit-app` 브랜치에 다음 파일의 커밋 변경사항이 있고 GitHub에 푸시/동기화되었는지 확인하세요:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py`
- Mona가 실수를 발견하면 수정하고 다시 푸시하세요. Mona는 필요한 만큼 여러 번 작업을 확인합니다.

</details>
"""

# Step 4
files[".github/steps/4-setup-django-rest-framework.md"] = r"""## Step 4: Django REST Framework 설정, 서버 시작, API 테스트

> [!NOTE]
> **비하인드 스토리:** 이 실습은 GitHub Copilot의 응답을 안내하는 커스텀 인스트럭션 파일을 사용합니다. 인스트럭션 파일 `.github/instructions/octofit_tracker_django_backend.instructions.md`에는 Django REST Framework 구성, URL 패턴, API 엔드포인트 가이드라인이 포함되어 있으며 Copilot이 이 단계의 코드를 생성할 때 참조합니다.

이 단계에서 다음을 수행합니다:

- Django REST Framework를 설정합니다.
- 서버를 시작합니다.
- curl을 사용하여 API를 테스트합니다.

GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> [!TIP]
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 Continue 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.
> - 에이전트 모드는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제하고, 실수가 발생하면 자동으로 복구하는 능력을 가지고 있습니다.

**Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.**

### :keyboard: 활동: Django REST Framework 설정 및 REST API 엔드포인트 테스트

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's setup codespace for the URL, start the server via VS Code launch.json, and test the API.
> 
> - All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.
> - Only update urls in `settings.py` and `urls.py`
> - REST api endpoint format https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
> - example full url: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
> - Do not hard code the `$CODESPACE_NAME` value use the variable
> - Do not update the `views.py`
>
> 1. Update `urls.py` to replace the return for the REST API URL endpoints with the environment variable $CODESPACE_NAME https://$CODESPACE_NAME-8000.app.github.dev for Django and avoid certificate HTTPS issues.
> 2. Make sure the Django backend works on your codespace URL and localhost (i.e., the value of `$CODESPACE_NAME`) by updating `ALLOWED_HOSTS` in `settings.py`.
> 3. Test the API endpoints using curl command.
>```

> [!IMPORTANT]
> GitHub Copilot 에이전트 모드가 제안하는 방식으로 Python Django 앱을 시작하지 **마세요**.
> **cancel**을 누르세요. 대신 다음 활동을 따르세요.

### :keyboard: 활동: Python Django 앱 시작 및 출력 확인

이제 Django 애플리케이션을 실제로 실행해 봅시다! 왼쪽 사이드바에서 `Run and Debug` 탭을 선택한 후 **Start Debugging** 아이콘을 누릅니다.

<img alt="Run Django" src="https://github.com/user-attachments/assets/a6c32898-bbeb-41ed-a8c5-488c8a42d507" width=30% height=30%>

포트 8000에 대한 Django REST API URL 팝업으로 이동합니다:

<img alt="django-rest-api-port" src="https://github.com/user-attachments/assets/627f3cbe-96ae-4a30-b38b-acd3cecf96ee" width=30% height=30%>

웹 브라우저에서 열면 다음과 같은 경고가 표시됩니다:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

`Continue`를 클릭하면 여러분의 codespace 이름과 함께 다음과 비슷하게 표시됩니다:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/45ac98ba-aa7b-4953-81d6-e38bba97ae35" width=50% height=50%>

1. Django 프로젝트를 업데이트하여 URL 엔드포인트에 codespace 이름을 포함시켰으니,
   변경사항을 `build-octofit-app` 브랜치에 체크인합니다.

1. 새로운 변경사항이 완료되면 `build-octofit-app` 브랜치에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- `build-octofit-app` 브랜치에 다음 파일의 커밋 변경사항이 있고 GitHub에 푸시/동기화되었는지 확인하세요:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/views.py`
- Mona가 실수를 발견하면 수정하고 다시 푸시하세요. Mona는 필요한 만큼 여러 번 작업을 확인합니다.

</details>
"""

# Step 5
files[".github/steps/5-setup-frontend-react-framework.md"] = r"""## Step 5: 프론트엔드 React 프레임워크 설정, 컴포넌트 업데이트, OctoFit Tracker 앱 시작

> [!NOTE]
> **비하인드 스토리:** 이 실습은 GitHub Copilot의 응답을 안내하는 커스텀 인스트럭션 파일을 사용합니다. 인스트럭션 파일 `.github/instructions/octofit_tracker_react_frontend.instructions.md`에는 React 프레임워크 설정 명령, Bootstrap 통합, 프론트엔드 구조 가이드라인이 포함되어 있으며 Copilot이 이 단계의 코드를 생성할 때 참조합니다.

이 단계에서 다음을 수행합니다:

- octofit-tracker 프론트엔드 React 프레임워크를 설정합니다.
- 다음 컴포넌트를 React 프레임워크에 맞게 업데이트합니다:
  - src/App.js
  - src/index.js
  - src/components/Activities.js
  - src/components/Leaderboard.js
  - src/components/Teams.js
  - src/components/Users.js
  - src/components/Workouts.js
- React 앱을 시작하고 출력을 확인합니다.

GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> [!NOTE]
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 Continue 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.
> - 에이전트 모드는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제하고, 실수가 발생하면 자동으로 복구하는 능력을 가지고 있습니다.

**Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.**

### :keyboard: 활동: octofit-tracker 프론트엔드 React 프레임워크 설치

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's setup the octofit-tracker frontend React  framework and
> ensure everything is created in the `octofit-tracker/frontend` directory by using `--prefix`
>
> 1. Make sure the the octofit-tracker/frontend directory exists.
> 2. create the react app
> 3. Install react, bootstrap, and react-router-dom
> 4. Import bootstrap css in the src/index.js file.
> 5. Don't change .gitignore file
>```

### :keyboard: 활동: octofit-tracker 프론트엔드 React 컴포넌트 업데이트

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's update the octofit-tracker frontend React components.
>
> - Update the following components to include the React framework to point to the backend REST API:
>   - src/App.js
>   - src/index.js
>   - src/components/Activities.js
>   - src/components/Leaderboard.js
>   - src/components/Teams.js
>   - src/components/Users.js
>   - src/components/Workouts.js
> - In each component replace the fetch url with the codespace url
>   https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/
>   for the Django rest framework backend.
>   make sure all components are pulling data from the REST api endpoint
>   for display in the REACT frontend
> - Make sure to use the correct port and protocol http or https.
> - Update src/App.js to include the main navigation for all components.
> - Make sure react-router-dom is used for the navigation menu.
> - The react app should show the navigation menu and the components.
> - Update all components to log the fetched data and make them compatible with both paginated (.results) and plain array responses.
> - Add console.log statements to each component to log the fetched data and the REST API endpoints.
> ```

### :keyboard: 활동: React 앱 시작 및 출력 확인

이제 React 애플리케이션을 실제로 실행해 봅시다! 왼쪽 사이드바에서 `Run and Debug` 탭을 선택한 후 **Start Debugging** 아이콘을 누릅니다.

<img alt="Run React Frontend" src="https://github.com/user-attachments/assets/b76a8e82-8435-4cbd-9540-8143756d1c60"  width=30% height=30%>

포트 3000에 대한 React Frontend URL 팝업으로 이동합니다:

<img alt="react-frontend-port" src="https://github.com/user-attachments/assets/a0c8b213-ee5f-46dd-8675-686a7ba0818f" width=30% height=30%>

웹 브라우저에서 열면 다음과 같은 경고가 표시됩니다:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

`Continue`를 클릭하면 다음과 비슷하게 표시됩니다:

<img alt="react-frontend-app" src="https://github.com/user-attachments/assets/f7f1a076-c259-49f6-8aa5-9ebcd5f0698d" width=50% height=50%>

### :keyboard: 활동: OctoFit Tracker 앱에 포맷팅, 구조화, 스타일링 추가하기

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's style this like App.css and make it look nice.
>
> - Let's make the App.js and all components javascript files in the app are consistent with the following:
>   - Use bootstrap tables for the data in all javascript components.
>   - Use bootstrap buttons for the buttons.
>   - Use bootstrap headings for the headings.
>   - Use bootstrap links for the links.
>   - Use bootstrap navigation for the navigation menu.
>   - Use bootstrap forms for the forms.
>   - Use bootstrap cards for the cards.
>   - Use bootstrap modals for the modals.
>   - Consistent table layouts for all components data.
>```

### :keyboard: 선택 활동: OctoFit Tracker 앱을 예쁘게 꾸미고 색상 추가하기

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's style this like App.css and make it look nice.
> 
> -  Edit the App.css file to do the following:
>   - Add some color to the background.
>   - Add some color to the text.
>   - Add some color to the tables.
>   - Add some color to the buttons.
>   - Add some color to the headings.
>   - Add some color to the links.
>   - Add some color to the navigation menu.
> - Add the octofitapp-small logo justified to the left to the app and make it look nice.
> - Add a favicon to the app and make it look nice.
>```

### :keyboard: 선택 활동: 외관을 반복 개선하고 다른 모델 사용해 보기

> [!TIP]
> - 직접 프롬프트를 작성하여 앱의 외관을 변경하고, 기능을 추가하며, 다른 모델을 사용해 보세요.

1. 모든 애플리케이션 컴포넌트의 React 프론트엔드를 만들었으니, 변경사항을 `build-octofit-app` 브랜치에 체크인합니다.

1. 새로운 변경사항이 완료되면 `build-octofit-app` 브랜치에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- `build-octofit-app` 브랜치에 다음 파일의 커밋 변경사항이 있고 GitHub에 푸시/동기화되었는지 확인하세요:
  - `octofit-tracker/frontend/src/components/Activities.js`에 `-8000.app.github.dev/api/activities/`가 포함
  - `octofit-tracker/frontend/src/components/Leaderboard.js`에 `-8000.app.github.dev/api/leaderboard/`가 포함
  - `octofit-tracker/frontend/src/components/Teams.js`에 `-8000.app.github.dev/api/teams/`가 포함
  - `octofit-tracker/frontend/src/components/Users.js`에 `-8000.app.github.dev/api/users/`가 포함
  - `octofit-tracker/frontend/src/components/Workouts.js`에 `-8000.app.github.dev/api/workouts/`가 포함
- Mona가 실수를 발견하면 수정하고 다시 푸시하세요. Mona는 필요한 만큼 여러 번 작업을 확인합니다.

</details>
"""

# Step 6
files[".github/steps/6-copilot-on-github.md"] = r"""## Step 6: Pull Request에서 GitHub Copilot 사용하기

축하합니다! 이 실습의 코딩 부분이 완료되었습니다 (VS Code도요). 이제 작업을 머지할 차례입니다. :tada: 마무리로, 풀 리퀘스트를 가속화할 수 있는 두 가지 제한 접근 Copilot 기능에 대해 배워봅시다!

#### Copilot Pull Request 요약

일반적으로 노트와 커밋 메시지를 검토한 후 풀 리퀘스트 설명을 요약합니다. 커밋 메시지가 일관되지 않거나 코드가 잘 문서화되지 않은 경우 시간이 많이 걸릴 수 있습니다. 다행히 Copilot은 풀 리퀘스트의 모든 변경사항을 고려하여 중요한 하이라이트를 참조와 함께 제공할 수 있습니다!

> [!NOTE]  
> **Copilot Free** 티어에서는 사용할 수 없습니다. [[문서]](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot)

#### Copilot 코드 리뷰

더 많은 눈으로 작업을 확인하는 것은 항상 유용하니, 일반적인 피어 리뷰 프로세스 전에 Copilot에게 첫 번째 검토를 요청해 봅시다. Copilot은 간단한 조정으로 고칠 수 있는 일반적인 실수를 잘 잡아내지만, 책임감 있게 사용하는 것을 기억하세요.

### :keyboard: 활동: Copilot으로 PR 요약 및 리뷰하기

1. 웹 브라우저에서 다른 탭을 열고 실습 저장소로 이동합니다.

1. 새 풀 리퀘스트를 생성하라는 **알림 배너**가 표시될 수 있습니다. 그것을 클릭하거나 상단의 **Pull Requests** 탭을 사용하여 새 풀 리퀘스트를 만듭니다. 다음 세부 사항을 사용하세요:

   - **base:** `main`
   - **compare:** `build-octofit-app`
   - **title:** `Add registration validation and more activities`

1. (선택) **Add a description** 영역에서 필요 시 편집 모드로 진입한 후 **Copilot actions** 아이콘과 **Summary** 액션을 클릭합니다. 잠시 후 Copilot이 설명을 추가합니다. :memo:

   <img alt="Copilot summarize button " width="300px" src="https://github.com/user-attachments/assets/3fc5fab4-db03-4ab8-8a16-cdd71ec2ded0">

1. (선택) 오른쪽 정보 패널 상단에서 **Reviewers** 섹션을 찾고 **Copilot 아이콘** 옆의 **Request** 버튼을 클릭합니다. Copilot이 풀 리퀘스트에 리뷰 댓글을 추가할 때까지 잠시 기다립니다!

   <img alt="Copilot review button" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

   > 🪧 **참고:** Copilot이 리뷰를 요청받았다는 로그 항목을 확인하세요.

1. 하단에서 **Merge pull request** 버튼을 누릅니다. 잘 하셨습니다! 모두 완료되었습니다! :tada:

1. Mona가 작업을 확인하고 피드백을 제공하며 이 레슨의 최종 리뷰를 게시할 때까지 잠시 기다립니다!
"""

# Review
files[".github/steps/x-review.md"] = r"""## 리뷰

_축하합니다, 이 실습을 완료하고 GitHub Copilot 에이전트 모드에 대해 많은 것을 배웠습니다!_

<img src="https://octodex.github.com/images/jetpacktocat.png" alt=celebrate width=200 align=right>

여러분이 달성한 것을 정리하면:

- GitHub Codespace와 환경을 설정했습니다.
- Copilot 인라인 제안, Chat, Edits 사용법을 배웠습니다.
- Copilot을 사용하여 커밋 메시지와 풀 리퀘스트 요약을 생성했습니다.
- Copilot에게 코드 리뷰를 요청하는 방법을 배웠습니다.

### 다음 단계

- 프로젝트를 계속 작업해 보세요
  - Copilot을 사용하여 로그인 및 인증 기능을 추가하세요.
  - app.css를 통해 앱의 외관을 계속 발전시키세요.
  - Copilot을 사용하여 풀 리퀘스트 리뷰 중 발견된 문제를 수정하세요.
  - Copilot을 사용하여 테스트와 문서를 생성하세요.
  - 다른 모델에서 Copilot을 사용해 보세요.
- 다른 [GitHub Skills 실습](https://learn.github.com/skills)을 확인해 보세요.
- [GitHub Copilot으로 레거시 코드 현대화](https://github.com/skills/modernize-your-legacy-code-with-github-copilot)를 시도해 보세요.

GitHub Copilot에 대해 더 알아보려면 다음 리소스를 확인하세요:

- GitHub Copilot 에이전트 모드에 대한 블로그 [GitHub Copilot 마스터하기: AI 에이전트 모드를 사용할 때](https://github.blog/ai-and-ml/github-copilot/mastering-github-copilot-when-to-use-ai-agent-mode/)
- Copilot에서 원하는 응답을 받지 못하나요? [프롬프트 엔지니어링 배우기](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)
- GitHub Copilot [슬래시 명령](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode)을 탐색해 보세요.
- 다른 기능도 확인하세요 [GitHub Copilot 기능](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features).
- [GitHub Copilot 문서](https://docs.github.com/en/copilot)를 살펴보세요.
"""

# docs/octofit_story.md
files["docs/octofit_story.md"] = r"""# GitHub Copilot 에이전트 모드로 피트니스 앱 만들기 - Mergington 고등학교

## Mergington 고등학교 OctoFit Tracker 앱 스토리

Paul Octo는 8년 넘게 Mergington 고등학교에서 체육 교사로 근무해 왔습니다. 열정적이고 창의적인 체육 수업 방식에도 불구하고, 학생들이 학교를 벗어나면 신체 활동이 줄어드는 것에 대해 점점 더 걱정하게 되었습니다. 많은 학생들이 필수 체육 수업 외에는 거의 운동하지 않는다고 인정했습니다.

"체육 교육에서의 기술 통합"에 관한 전문 개발 컨퍼런스에 참석한 후, Paul은 솔루션을 만들겠다는 영감을 받았습니다. 그가 원한 것은:

1. 피트니스 추적을 재미있고 매력적으로 만들기
2. 친선 경쟁을 통한 긍정적인 동료 압력 만들기
3. 원격으로 학생 진행 상황 모니터링하기
4. 개인별 체력 수준에 따른 맞춤형 가이던스 제공하기

## OctoFit Tracker의 탄생

Paul은 처음에 점심시간에 메모장에 아이디어를 스케치했습니다. 학생들이 운동을 기록하고, 업적 배지를 획득하며, 월간 피트니스 챌린지에서 경쟁하는 앱을 구상했습니다. 그러나 기본적인 코딩 지식만 가진 체육 교사로서 기술적인 측면은 어려워 보였습니다.

그래서 Mergington 고등학교 IT 부서장인 Jessica Cat에게 도움을 요청했습니다. Jessica는 저장소 인스트럭션과 프롬프트를 사용할 것을 권장했습니다.

### 기술 기획 단계

개발을 시작하기 전에 Paul과 Jessica는 OctoFit Tracker의 인스트럭션과 프롬프트를 꼼꼼히 검토했습니다. 이는 OctoFit Tracker를 위한 견고한 기반을 제공하여 기술 표준 준수와 검증된 디자인 패턴 활용을 보장했습니다.
Paul과 IT 팀은 함께 OctoFit Tracker의 핵심 요구사항을 파악했습니다:

### 사용자 경험 목표

- 십대를 위해 특별히 설계된 간단하고 직관적인 인터페이스
- 마찰을 최소화하는 빠른 활동 기록
- 학생 개인정보를 존중하는 소셜 기능
- 참여를 유지하기 위한 게이미피케이션 요소

## 현재 개발 현황

Paul과 Jessica는 GitHub Codespace 환경을 설정하고 GitHub Copilot 에이전트 모드로 놀라운 진척을 보이고 있습니다. OctoFit Tracker 프로토타입에는 다음이 포함됩니다:

- 기능적인 사용자 등록 시스템
- 달리기, 걷기, 근력 운동을 위한 기본 활동 기록
- 팀 경쟁을 위한 시작 프레임워크
- 학생 진행 상황을 보여주는 간단한 대시보드

## Paul의 다음 단계

기본 인프라가 구축된 상태에서 Paul은 현재 다음에 집중하고 있습니다:

1. 다양한 유형의 활동을 공정하게 비교하는 매력적인 포인트 시스템 개발
2. 다양한 학생 관심사에 호소하는 동기 부여 챌린지 만들기
3. 방해가 되지 않으면서 꾸준함을 장려하는 알림 시스템 구축
4. 추가 지원이나 동기 부여가 필요한 학생을 파악하는 데 도움이 되는 보고서 설계

IT 부서는 GitHub Copilot 에이전트 모드가 개발을 가속화하여 Paul이 교육적 측면에 집중할 수 있게 하면서 AI가 대부분의 기술적 구현을 처리하는 것에 깊은 인상을 받았습니다. Jessica Cat은 OctoFit Tracker가 커스텀 인스트럭션과 프롬프트 파일을 활용하는 방식에 특히 만족했습니다.

### 워크숍 개요

이 워크숍에서는:

1. **GitHub Codespaces**를 사용하여 개발 환경을 설정합니다
2. **GitHub Copilot**을 사용하여 여러 기술에 걸쳐 개발을 가속화합니다
3. Copilot 에이전트 모드의 도움으로 **OctoFit Tracker** 앱의 주요 컴포넌트를 빌드합니다
4. **GitHub Copilot 에이전트 모드**와 함께 작업하기 위한 모범 사례와 프롬프팅 기법을 배웁니다

### 애플리케이션 기능

**OctoFit Tracker**에는 다음이 포함됩니다:

- 사용자 프로필
- 활동 기록 및 추적
- 팀 생성 및 관리
- 경쟁 리더보드
- 맞춤형 운동 제안

### GitHub Copilot Chat

- [GitHub Copilot Chat 시작하기](https://docs.github.com/en/copilot/how-tos/use-chat/get-started-with-chat?tool=vscode)
- [IDE에서 Chat 사용하기](https://docs.github.com/en/copilot/how-tos/use-chat/use-chat-in-ide?tool=vscode)

#### LLM 모델 참고

- [GitHub Copilot에서 지원하는 AI 모델](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
- [AI 모델 비교](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [GitHub Copilot Chat의 AI 모델 변경하기](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model?tool=vscode)
- [GitHub Copilot 코드 완성의 AI 모델 변경하기](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model?tool=vscode)

#### 프롬프트 엔지니어링

- [GitHub Copilot Chat을 위한 프롬프트 엔지니어링](https://docs.github.com/en/copilot/concepts/prompt-engineering)
- [GitHub Copilot 사용법: 프롬프트, 팁, 사용 사례](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [IDE에서 GitHub Copilot 사용하기: 팁, 트릭, 모범 사례](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)

### OctoFit Tracker 피트니스 앱 기술 스택

최신 웹 애플리케이션 스택을 사용합니다:

- **프론트엔드**: React.js
- **백엔드**: Python + Django REST API Framework
- **데이터베이스**: MongoDB
- **개발 환경**: GitHub Codespaces

### 워크숍 구조

1. **소개**
   - OctoFit Tracker 앱 컨셉 개요
   - GitHub Copilot Chat 모델
"""

# .devcontainer/welcome-message.txt
files[".devcontainer/welcome-message.txt"] = r"""👋 GitHub Copilot 에이전트 모드로 다중 계층 피트니스 트래커 앱을 빌드하는 실습에 오신 것을 환영합니다!
Copilot의 기능을 탐색하게 되어 정말 기쁩니다!
🏋🏽🔥💪🏼🎧 Mergington 고등학교의 체육 교사로서 학생들을 위한 피트니스 앱을 만드는 임무를 받았습니다.
📃 GitHub Copilot 문서: https://docs.github.com/en/copilot
"""

for path, content in files.items():
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))
    print(f"Wrote {path}")

print("Done! All step files translated.")
