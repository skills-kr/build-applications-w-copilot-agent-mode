## Step 4: Django REST Framework 설정, 서버 시작, API 테스트

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
