## Step 2: 초기 애플리케이션 설정: 디렉토리 구조, Python 요구사항, MongoDB

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
