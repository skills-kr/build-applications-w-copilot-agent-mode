## Step 3: octofit_db MongoDB 데이터베이스 초기화 및 생성, Django 프로젝트/앱 구성, Django 프로젝트/앱 파일 업데이트, MongoDB 데이터베이스 채우기

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
