## Step 6: Pull Request에서 GitHub Copilot 사용하기

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
