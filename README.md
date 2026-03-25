# GitHub Copilot 에이전트 모드로 애플리케이션 빌드하기

<!-- ![](../../actions/workflows/0-start-course.yml/badge.svg?branch=main) -->
<img src="https://github.com/user-attachments/assets/1b3ea5df-f18d-4ed8-9ae6-f96dc1861818" alt="octofit-tracker" width="300"/>

_1시간 이내에 GitHub Copilot 에이전트 모드로 애플리케이션을 빌드해 보세요._

## 환영합니다

GitHub Copilot이 더 빠르고 오류 없이 코드를 작성하도록 도와주는 것을 많은 분들이 좋아합니다.
하지만 자연어로 작성된 요구사항을 바탕으로 프레젠테이션, 로직, 데이터 레이어를 갖춘 다중 계층 애플리케이션을 GitHub가 만들어 줄 수 있다면 어떨까요?
이 실습에서는 GitHub Copilot 에이전트 모드를 활용하여 완전한 애플리케이션을 만들어 봅니다.

- **대상**: GitHub Copilot, 기본 GitHub, 기본 웹 개발에 익숙한 중급 개발자
- **배울 내용**: GitHub Copilot 에이전트 모드와 이를 애플리케이션 개발에 활용하는 방법을 소개합니다.
- **만들 것**: GitHub Copilot 에이전트 모드를 사용하여 고등학교 체육 교사로서 피트니스 애플리케이션을 만듭니다.
- **사전 요구사항**: Skills 실습: <a href="https://github.com/skills-kr/getting-started-with-github-copilot">GitHub Copilot 시작하기</a>.
- **소요 시간**: 이 실습은 1시간 이내에 완료할 수 있습니다.

이 실습에서 다음을 수행합니다:

1. 다중 계층 애플리케이션 제작을 위해 미리 구성된 개발 환경을 시작합니다.
1. GitHub Copilot Chat에서 프롬프트를 입력하고, 편집 탭을 선택한 후 편집/에이전트 드롭다운에서 에이전트 모드를 선택합니다.
1. 이 실습에서는 주로 최신 기본 LLM을 사용했습니다.
1. 다른 LLM 모델을 사용해 다른 출력을 확인해 보세요.
1. 각 단계마다 Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.

### 이 실습을 시작하는 방법

실습을 자신의 계정으로 복사한 후, 좋아하는 Octocat(Mona)에게 **약 20초** 정도 첫 번째 레슨을 준비할 시간을 주고 **페이지를 새로고침**하세요.

[![](https://img.shields.io/badge/실습%20복사-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills-kr&template_name=build-applications-w-copilot-agent-mode&owner=%40me&name=skills-build-applications-w-copilot-agent-mode&description=Exercise:+Build+applications+with+GitHub+Copilot+agent+mode&visibility=public)

<details>
<summary>문제가 있나요? 🤷</summary><br/>

실습을 복사할 때 다음 설정을 권장합니다:

- 소유자(owner)는 개인 계정 또는 저장소를 호스팅할 조직을 선택하세요.

- 공개 저장소로 만드는 것을 권장합니다. 비공개 저장소는 Actions 사용 시간을 소모합니다.

20초 후에도 실습이 준비되지 않았다면, 저장소의 "Actions" 탭을 확인해 주세요 (또는 `https://github.com/<YOUR-USERNAME>/<YOUR-REPO>/actions`를 방문).

- 작업이 실행 중인지 확인하세요. 때로는 조금 더 시간이 걸릴 수 있습니다.

- 페이지에 실패한 작업이 표시되면, 이슈를 제출해 주세요. 버그를 발견했네요! 🐛

</details>

> **참고**: 이 실습은 [skills/build-applications-w-copilot-agent-mode](https://github.com/skills/build-applications-w-copilot-agent-mode)를 기반으로 한글화하고, [🏆 GitHub Skills Workshop Dashboard](https://github-skills.studydev.com)와 연계되어 있습니다.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
