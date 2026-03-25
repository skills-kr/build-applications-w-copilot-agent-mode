## Step 1: GitHub Copilot 에이전트 모드 시작하기

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
